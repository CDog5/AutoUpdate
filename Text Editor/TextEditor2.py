from tkinter import *
from tkinter import filedialog, messagebox
import subprocess
from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.formatters import TerminalFormatter
theme = 'light'
compiler = Tk()
compiler.title('Untitled - SimpliText')
compiler.resizable(False, False)
compiler.iconphoto(False, PhotoImage(file='icon.png'))
file_path = ''
process = None
fnt = ("Arial",10)
def chg_theme():
    global theme
    if theme == 'light':
        compiler.config(bg='#777')
        editor.config(bg='#777',fg='#fff')
        menu_bar.config(bg='#777',fg='#fff')
        theme = 'dark'
    else:
        compiler.config(bg='#fff')
        editor.config(bg='#fff',fg='#000')
        menu_bar.config(bg='#fff',fg='#000')
        theme = 'light'
def on_exit():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        compiler.destroy()
def kill_process():
    if process:
        process.terminate()
def set_file_path(path):
    global file_path
    file_path = path
def clear_textwins():
    editor.delete('1.0', END)
    code_output.delete('1.0', END)
def open_file():
    path = filedialog.askopenfilename(title = "Open",filetypes = (("All Files","*.*"),))
    if path == '':
        return
    with open(path, 'r') as file:
        code = file.read()
        clear_textwins()
        editor.insert('1.0', code)
        set_file_path(path)
        compiler.title(f'{path.split("/")[-1]} - SimpliText')


def save_as():
    if file_path == '':
        path = filedialog.asksaveasfilename(title="Save As",filetypes = (("All Files","*.*"),))
    else:
        path = file_path
    if path == '':
        return
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

def text_changed():
    code = editor.get('1.0', END)
    out = highlight(code,guess_lexer(code),TerminalFormatter())
    editor.delete('1.0', END)
    editor.insert('1.0', out)
def run_py():
    if file_path == '':
        save_as()
    if file_path == '':
        return
    command = f'python "{file_path}"'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.delete('1.0', END)
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)

compiler.bind('<F5>',lambda x: run_py())

compiler.bind("<Control-s>", lambda x: save_as())
editor = Text(undo=True,maxundo=-1)
editor.config(font=fnt)
editor.pack()
menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Exit', command=on_exit)
menu_bar.add_cascade(label='File', menu=file_menu)
options_menu = Menu(menu_bar, tearoff=0)
options_menu.add_command(label='Light Mode', command=chg_theme)
menu_bar.add_cascade(label='Options', menu=options_menu)
run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run .py', command=run_py)

menu_bar.add_cascade(label='Run', menu=run_bar)



compiler.config(menu=menu_bar)


code_output = Text(height=10)
code_output.config(font=fnt,bg='#222',fg='#fff')
code_output.bind("<Key>", lambda e: "break")
code_output.bind("<Control-c>", lambda x: kill_process())
#editor.bind('<KeyRelease>', lambda *args: text_changed())
code_output.pack()
compiler.protocol("WM_DELETE_WINDOW", on_exit)
chg_theme()
compiler.mainloop()


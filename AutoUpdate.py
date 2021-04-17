import requests,zipfile,os,shutil
dirpath = os.getcwd()
#CLEAR CURRENT 'LATEST' FOLDER. 
#Comment out if you want a failsafe
old = os.path.join(dirpath,'Latest')
if os.path.exists(old):
    shutil.rmtree(old)
#AUTOUPDATE REPO URL
url = 'https://github.com/CDog5/AutoUpdate/archive/refs/heads/main.zip'
#GET JUST FILE NAME
fname = url.split('/')[-1]
r = requests.get(url)
fpath = os.path.join(dirpath,fname)
#ZIP FILE MUST BE READ AS BYTES
with open(fpath,'wb') as f:
    f.write(r.content)
#EXTRACT EVERYTHING EXCEPT MARKDOWN AND THIS FILE
with zipfile.ZipFile(fpath,'r') as myzip:
    for f in myzip.namelist():
        if not f.endswith('.md') and f != 'AutoUpdate.py':
            myzip.extract(f,dirpath)
#CLEANUP BY REMOVING ZIP AND RENAMING FOLDER
os.remove(fpath)            
os.rename(os.path.join(dirpath,'AutoUpdate-main'),os.path.join(dirpath,'Latest'))
#DISPLAY VERSION INFO THEN DELETE THAT FILE
info = os.path.join(dirpath,'Latest','Version.txt')
with open(info,'r') as f:
    print(f'Info:\n{f.read()}')
os.remove(info)

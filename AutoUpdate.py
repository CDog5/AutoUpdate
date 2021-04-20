import zipfile,os,shutil
from urllib import request
dirpath = os.getcwd()
#CLEAR CURRENT 'LATEST' FOLDER
old = os.path.join(dirpath,'Latest')
if os.path.exists(old):
    shutil.rmtree(old)
#AUTOUPDATE REPO URL
#REPLACE WITH YOUR OWN REPO URL
url = 'https://github.com/CDog5/AutoUpdate/archive/refs/heads/main.zip'
#GET JUST FILE NAME AND REPO NAME
repo_name = url.split('/archive')[0].split('/')[-1]
fname = url.split('/')[-1]
with request.urlopen(url) as rs:
    r = rs.read()
fpath = os.path.join(dirpath,fname)
#ZIP FILE MUST BE READ AS BYTES
with open(fpath,'wb') as f:
    f.write(r)
#EXTRACT EVERYTHING EXCEPT MARKDOWN AND THIS FILE
with zipfile.ZipFile(fpath,'r') as myzip:
    for f in myzip.namelist():
        if 'Version.md' in f or not f.endswith('.md'):
            myzip.extract(f,dirpath)
#CLEANUP BY REMOVING ZIP AND RENAMING FOLDER
os.remove(fpath)            
os.rename(os.path.join(dirpath,f'{repo_name}-{fname.replace(".zip","")}'),os.path.join(dirpath,'Latest'))
#DISPLAY VERSION INFO THEN DELETE THAT FILE
info = os.path.join(dirpath,'Latest','Version.md')
with open(info,'r') as f:
    print(f'Info:\n{f.read()}')
os.remove(info)

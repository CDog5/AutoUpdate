import json,os,shutil
def check_exist(path,mk=False):
    if not os.path.exists(path):
        if mk:
            open(path, 'a').close()
        return False
    return True
if not os.path.exists(os.path.join(os.getcwd(),'TEMP')):
    os.makedirs(os.path.join(os.getcwd(),'TEMP'))

class Config:
    def __init__(self):
        self.temp = os.path.join(os.getcwd(),'TEMP')
        self.path = os.path.join(self.temp,'config.json')
    def read(self):
        if not check_exist(self.path,mk=True):
            with open(self.path,'w') as f:
                json.dump({"config":{}},f)
        
        with open(self.path,'r') as f:
            self.data = json.load(f)
        return self.data['config']
    def write(self,data):
        with open(self.path,'w') as f:
            final = {"config":data}
            json.dump(final,f)
        return final
class TempWriter:
    def __init__(self):
        self.temp = os.path.join(os.getcwd(),'TEMP')
    def mkdir(self,relpath,ow=False):
        full_path = os.path.join(self.temp,relpath)
        if not os.path.exists(full_path):
            os.makedirs(full_path)
        if ow == True:
            shutil.rmtree(full_path)
            os.makedirs(full_path)
        return full_path
    def rmdir(self,relpath):
        full_path = os.path.join(self.temp,relpath)
        shutil.rmtree(full_path)
    def clearall(self):
        shutil.rmtree(self.temp)
    def write(self,relpath,data,fmode='w'):
        full_path = os.path.join(self.temp,relpath)
        with open(full_path,fmode) as f:
            f.write(data)
    def read(self,relpath):
        full_path = os.path.join(self.temp,relpath)
        if check_exist(full_path):
            with open(full_path,'r') as f:
                return f.read()
        return None


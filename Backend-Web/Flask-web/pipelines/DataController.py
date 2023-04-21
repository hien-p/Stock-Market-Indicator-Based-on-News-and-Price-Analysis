import os
import pandas as pd
from shutil import make_archive, move

## Set parameters ##
class DataController:

    def __init__(self, repoName):
        self.repoName = repoName
        self.RawDataFolder = f'data/{self.repoName}/dataset/'
        self.PrepDataFolder = f'data/{self.repoName}/data/'
        self.PrepDataTarget = f"prep_ds"
        self.ReadyDataFolder = f"data/ready/"

    def list_all_raw_dataset(self)->list:
        files = os.listdir(self.RawDataFolder)
        return files

    def list_all_prep_dataset(self)->list:
        files = os.listdir(self.PrepDataFolder)
        return files

    def read_as_dicts(self, fileName:str, ext:str='csv')->dict:
        path = os.path.join(self.RawDataFolder,fileName)
        if(ext == 'csv'):
            data = pd.read_csv(path)
        else:
            data = pd.read_excel(path)
        return data.to_dict("split")

    def compress_prepData_target(self, dsName:str, method:str='zip'):
        fullPath = os.path.join(self.PrepDataFolder, dsName)
        msg = "Your files are ready!"
        ## TODO : check dsName and check is valid fullPath
        make_archive(fullPath, method, root_dir=self.ReadyDataFolder)
        print("Begin")
        move(f"{fullPath}.{method}", f"{self.ReadyDataFolder}/{dsName}.{method}")
        print(msg)
        return True



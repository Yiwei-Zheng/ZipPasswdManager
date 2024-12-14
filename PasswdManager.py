# Author https://github.com/Yiwei-Zheng

import hashlib
import zipfile36 as zipfile
import pickle
from typing import List


def sha256(binary_data) -> str:
    h = hashlib.sha256()
    h.update(binary_data)
    return h.hexdigest()


def zipExtract(raw_path: str, target_path: str, passwd: str):
    '''
        raw_path: The location of the zip file
        target_path: The location that the file will be extracted to
    '''
    # print(passwd)
    with zipfile.ZipFile(raw_path, 'r') as zip_ref:
        # extract the file to a given dir
        zip_ref.extractall(target_path, pwd=passwd.encode("utf-8"))
    return

class ZipPkg(object):
    def  __init__(self, abs_path: str, passwd: str):
        with open(abs_path, "rb") as f:
            # Save the sha 256 of the binary code of the file
            self.label: str = sha256(f.read())
        
        # Save the passwd of the file
        self.passwd = passwd

        # Try to testify if the passwd is legal
        try:
            zipExtract(abs_path, "tmp/"+ f"{self.label[0:10]}", self.passwd)

        except Exception as e:
            print(e)
        return
    




ZipPkgList: List[ZipPkg] = []

def addZipPkg(z: ZipPkg):
    if z not in ZipPkgList:
        ZipPkgList.append(z)
    try:
        with open("passwd.pkl", "wb") as f:
            pickle.dump(ZipPkgList, f)
    except:
        pass
    return


# If needed, the search can be switch to binary search in the future
def searchZipPkgPasswd(abs_path: str) -> str:
    try:
        with open("passwd.pkl", "rb") as f:
            ZipPkgList = pickle.load(f)
    except Exception as e:
        raise Exception("No passwd.pkl found!")


    with open(abs_path, "rb") as f:
        # Save the sha 256 of the binary code of the file
        z_label: str = sha256(f.read())
    
    label_list = [z.label for z in ZipPkgList]
    for i in range(len(label_list)):
        if z_label == label_list[i]:
            return ZipPkgList[i].passwd
    raise Exception("PasswdNotFound!")

    
import hashlib
import zipfile36 as zipfile

def sha256(binary_data) -> str:
    h = hashlib.sha256()
    h.update(binary_data)
    return h.hexdigest()


def zipExtract(raw_path: str, target_path: str, passwd: str):
    '''
        raw_path: The location of the zip file
        target_path: The location that the file will be extracted to
    '''
    print(passwd)
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

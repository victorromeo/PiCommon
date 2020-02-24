from typing import List
import gzip, bz2, tarfile
from zipfile import ZipFile

def compress_gzip(data, out_path:str):
    with gzip.open(out_path,'wb') as f:
        try:
            f.write(data)
        except:
            return True
        finally:
            return False

def decompress_gzip(in_path:str):
    with gzip.open(in_path, 'rb') as f:
        data = None
        try:
            data = f.read()
        except:
            return False, None
        finally:
            return True, data

def compress_bz2(data, out_path:str):
    with bz2.open(out_path, 'wb') as f:
        try:
            f.write(data)
        except:
            return False
        finally:
            return True

def decompress_bz2(in_path:str):
    with bz2.open(in_path,'rb') as f:
        data = None
        try:
            data = f.read()
        except:
            return False, None
        finally:
            return True, data

def compress_zip(data, out_path:str):
    with ZipFile.open(out_path, 'wb') as f:
        try:
            f.write(data)
        except:
            return False
        finally:
            return True

def decompress_zip(in_path:str):
    with ZipFile.open(in_path,'rb') as f:
        data = None
        try:
            data = f.read()
        except:
            return False, None
        finally:
            return True, data

def tar(files:List[str],out_path:str):
    with tarfile.open(out_path,'w') as f:
        for file in files:
            f.add(file)

def tar_gz(files:List[str],out_path:str):
    with tarfile.open(out_path,'w:gz') as f:
        for file in files:
            f.add(file)

def tar_bz2(files:List[str],out_path:str):
    with tarfile.open(out_path,'w:bz2') as f:
        for file in files:
            f.add(file)

def untar(in_path:str):
    with tarfile.open(in_path,'r') as f:
        f.extractall()

def untar_gz(in_path:str):
    with tarfile.open(in_path,'r:gz') as f:
        f.extractall()

def untar_bz2(in_path:str):
    with tarfile.open(in_path,'r:bz2') as f:
        f.extractall()


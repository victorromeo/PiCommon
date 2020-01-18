import os
from Log import logging as log

def clean_path(path:str) -> str:
    return path.strip()

def make_dir(path:str):
    try:
        os.mkdir(clean_path(path))
    except:
        log.error('Failed to make directory: {0}'.format(path))
        return False
    finally:
        return True

def remove_dir(path:str):
    try:
        os.rmdir(clean_path(path))
    except:
        log.error('Failed to remove directory {0}'.format(path))
        return False
    finally:
        return True

def read(path:str):
    with open(clean_path(path), 'r') as file:
        try:
            data = file.read(data)
        except:
            log.error('Failed to read from {0}'.format(path))
            return None
        finally:
            return data

def write(path:str, data):
    with open(clean_path(path), 'w') as file:
        try:
            file.write(data)
        except:
            log.error('Failed to write to {0}'.format(path))
            return None
        finally:
            return data

def file_exists(path:str):
    return os.path.isfile(clean_path(path))

def directory_exists(path:str):
    return os.path.isdir(clean_path(path))

def exists(path:str):
    return os.path.exists(clean_path(path))

def owner_id(path:str):
    return os.stat(clean_path(path)).st_uid

def group_id(path:str):
    return os.stat(clean_path(path)).st_gid

def size(path:str):
    return os.stat(clean_path(path)).st_size

def access_time(path:str):
    return os.stat(clean_path(path)).st_atime

def modification_time(path:str):
    return os.stat(clean_path(path)).st_mtime

def create_time(path:str):
    return os.stat(clean_path(path)).st_ctime

def protection(path:str):
    return os.stat(clean_path(path)).st_mode

def inode(path:str):
    return os.stat(clean_path(path)).st_ino

def hard_links(path:str):
    return os.stat(clean_path(path)).st_nlink

def create_symbolic_link(src_path:str, link_path:str):
    if exists(clean_path(src_path)):
        try:
            os.symlink(clean_path(src_path), clean_path(link_path))
        except:
            return False
        finally:
            return True

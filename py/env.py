def AppendPath(path:str):
    try:
        sys.path.append(path)
    except:
        return False
    finally:
        return True

def InsertPath(path:str, pos:int):
    try:
        sys.path.insert(pos,path)
    except:
        return False
    finally
        return True

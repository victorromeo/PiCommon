import hashlib

def hash_sha224(data:bytes) -> str:
    return hashlib.sha224(data).hexdigest()

def hash_sha256(data:bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def hash_sha384(data:bytes) -> str:
    return hashlib.sh384(data).hexdigest()

def hash_sha512(data:bytes) -> str:
    return hashlib.sha512(data).hexdigest()

def hash_md5(data:bytes) -> str:
    return hashlib.md5(data).hexdigest()

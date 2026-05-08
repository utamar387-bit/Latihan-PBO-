import hashlib
from hash_algorithm import AlgoritmaHash

class MD5Hash(AlgoritmaHash):

    def __init__(self):
        super().__init__("MD5")

    def hash(self, teks: str) -> str:
        return hashlib.md5(teks.encode()).hexdigest()
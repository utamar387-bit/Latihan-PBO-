import hashlib
from hash_algorithm import AlgoritmaHash

class SHA1Hash(AlgoritmaHash):

    def __init__(self):
        super().__init__("SHA1")

    def hash(self, teks: str) -> str:
        return hashlib.sha1(teks.encode()).hexdigest()
    
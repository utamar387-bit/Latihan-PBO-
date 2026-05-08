import hashlib
from hash_algorithm import AlgoritmaHash

class SHA512Hash(AlgoritmaHash):

    def __init__(self):
        super().__init__("SHA512")

    def hash(self, teks: str) -> str:
        return hashlib.sha512(teks.encode()).hexdigest()
import hashlib
from hash_algorithm import AlgoritmaHash

class SHA256Hash(AlgoritmaHash):

    def __init__(self):
        super().__init__("SHA256")

    def hash(self, teks: str) -> str:
        return hashlib.sha256(teks.encode()).hexdigest()
    
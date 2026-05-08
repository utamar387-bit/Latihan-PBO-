from hash_algorithm import AlgoritmaHash

class ManajerHash:

    def __init__(self):
        self.algoritma = None

    def set_algoritma(self, algoritma: AlgoritmaHash):
        self.algoritma = algoritma

    def buat_hash(self, teks: str) -> str:

        if self.algoritma is None:
            return "Algoritma hash belum dipilih"

        return self.algoritma.hash(teks)
    
from abc import ABC, abstractmethod

class AlgoritmaHash(ABC):

    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def hash(self, teks: str) -> str:
        pass
from hash_manager import ManajerHash

from md5_hash import MD5Hash
from sha1_hash import SHA1Hash
from sha256_hash import SHA256Hash
from sha512_hash import SHA512Hash

def main():

    manajer = ManajerHash()

    teks = input("Masukkan teks: ")

    print("\nPilih algoritma hash:")
    print("1. MD5")
    print("2. SHA1")
    print("3. SHA256")
    print("4. SHA512")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        manajer.set_algoritma(MD5Hash())

    elif pilihan == "2":
        manajer.set_algoritma(SHA1Hash())

    elif pilihan == "3":
        manajer.set_algoritma(SHA256Hash())

    elif pilihan == "4":
        manajer.set_algoritma(SHA512Hash())

    else:
        print("Pilihan tidak valid")
        return

    hasil = manajer.buat_hash(teks)

    print("\nAlgoritma :", manajer.algoritma.nama)
    print("Hash      :", hasil)

if __name__ == "__main__":
    main()
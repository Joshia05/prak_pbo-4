class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=False):
        self.__nim = nim
        self.__nama = nama
        self.__angkatan = angkatan
        self.__isMahasiswa = isMahasiswa

    def set_nama(self, nama_baru):
        self.__nama = nama_baru

    def set_nim(self, nim_baru):
        self.__nim = nim_baru

    def get_nama(self):
        return self.__nama

    def get_nim(self):
        return self.__nim

    def perkenalan_diri(self):
        return f"Perkenalkan nama saya {self.__nama}, dengan nim {self.__nim}, dari angkatan {self.__angkatan}"

    def mahasiswa_kampus(self):
        if self.__isMahasiswa == True:
            if self.__angkatan < 2014:
                return "Mahasiswa Lama"
            else:
                return "Bukan Mahasiswa"
        else :
            return "Mahasiswa Baru"
    def hitung_jumlah_huruf(self):
        return len(self.__nama)

mahasiswa1 = Mahasiswa(nim="121140171", nama="Yohana Aritonang", angkatan=2015)
mahasiswa2 = Mahasiswa(nim="121140172", nama="Maharani Pujiastuti", angkatan=2013, isMahasiswa=True)

print(f"Mahasiswa 1: Nama = {mahasiswa1.get_nama()}, NIM = {mahasiswa1.get_nim()}")
print(f"Mahasiswa 2: Nama = {mahasiswa2.get_nama()}, NIM = {mahasiswa2.get_nim()}")
print(f"Perkenalan Mahasiswa 1 : {mahasiswa1.perkenalan_diri()}")
print(f"Perkenalan Mahasiswa 2 : {mahasiswa2.perkenalan_diri()}")
print(f"Apakah Mahasiswa 1 mahasiswa lama/baru ? : {mahasiswa1.mahasiswa_kampus()}")
print(f"Apakah Mahasiswa 2 mahasiswa lama/baru ? : {mahasiswa2.mahasiswa_kampus()}")
print(f"Jumlah huruf nama Mahasiswa 1: {mahasiswa1.hitung_jumlah_huruf()}")
print(f"Jumlah huruf nama Mahasiswa 2: {mahasiswa2.hitung_jumlah_huruf()}")

mahasiswa1.set_nama("Joshia Fernandes Sectio Purba")
mahasiswa1.set_nim("122140170")

print(f"Mahasiswa 1: Nama = {mahasiswa1.get_nama()}, NIM = {mahasiswa1.get_nim()}")
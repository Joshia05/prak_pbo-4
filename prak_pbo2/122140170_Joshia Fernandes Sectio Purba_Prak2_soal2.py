import random
class Bitcoin:

    def __init__(self):
        self.__number = random.randint(1, 25)
        self.__tries = 0
        print("Selamat datang di tebakan bitcoin!")
        print("Saya telah memilih sebuah tebakan kemenangan bitcoin antara 1 dan 25.")
        print("Anda memiliki 5 kesempatan untuk menebaknya.")

    def __del__(self):
        print("Terima kasih telah bermain tebak bitcoin!")

    def limit_tries(func):
        def wrapper(self, *args):
            if self.__tries < 5:
                return func(self, *args)
            else:
                print("Anda telah kehabisan kesempatan. Anda kalah.")
                print(f"Tebakan yang saya pilih adalah {self.__number}.")
        return wrapper

    def start(self):
        while True:
            guess = input("Masukkan tebakan Anda: ")
            try:
                guess = int(guess)
            except ValueError:
                print("Input tidak valid. Masukkan angka.")
                continue
            if guess < 1 or guess > 25:
                print("Input tidak valid. Masukkan tebakan antara 1 dan 25.")
                continue
            
            self.check(guess)
            if self.__tries == 5 or guess == self.__number:
                break

    @limit_tries
    def check(self, guess):
        self.__tries += 1
        if guess == self.__number:
            print(f"Selamat! Anda menebak dengan benar dalam {self.__tries} kali.")
            print("Anda menang!")
        elif guess < self.__number:
            print("Tebakan Anda terlalu rendah.")
            print(f"Anda masih memiliki {5 - self.__tries} kesempatan.")
        else:
            print("Tebakan Anda terlalu tinggi.")
            print(f"Anda masih memiliki {5 - self.__tries} kesempatan,")
           
bitcoin = Bitcoin()

bitcoin.start()

del  bitcoin
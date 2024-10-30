cass Fraccion:
    def __init__(self, num=0, den=1):
        self.__num = num
        self.__den = den

    def set(self, num, den):
        self.__num = num
        self.__den = den

    def set_num(self, x):
        self.__num = x

    def set_den(self, x):
        if x == 0:
            self.__den = 1
        else:
            self.__den = x

    def get_num(self):
        return self.__num

    def get_den(self):
        return self.__den

# Programa principal
def main():
    fr = Fraccion()
    fs = Fraccion(3, 5)
    fr.set_num(1)
    fr.set_den(0)
    fr.__den = 0
    print(f"{fr.get_num()}/{fr.get_den()}")
    print(f"{fs.get_num()}/{fs.get_den()}")
    fs.set(8, 9)
    print(f"{fs.get_num()}/{fs.get_den()}")

if __name__ == "__main__":
    main()

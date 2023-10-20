import string


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        print(f"Количество букв в алфавите: {len(self.letters)}")

class EngAlphabet(Alphabet):

    def __init__(self):
        super().__init__(lang = "Eng",  letters = string.ascii_uppercase)



        self.__letters_num = len(string.ascii_uppercase)



    def is_en_letter(self,letter):
        engletters = set(string.ascii_letters)
        isFound = False
        for el in engletters:
            if letter == el:
                isFound = True

        if isFound:
            print(f"Буква {letter} принадлежит английскому алфавиту")
        else:
            print(f"Буква {letter} не принадлежит английскому алфавиту")

    def letters_num(self):
        print(f"Количество букв в алфавите: {self.__letters_num}")

    @staticmethod
    def example():
        print("This string on english language")

alph = EngAlphabet()
print(alph.letters)
alph.is_en_letter("a")
alph.letters_num()
alph.example()
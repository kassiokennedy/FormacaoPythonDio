class Animal:
    def __init__(self, qntpatas):
        self.qntpatas = qntpatas


class Mamifero(Animal):
    def __init__(self, qntpatas):
        self.qntpatas = qntpatas


class Ave(Animal):
    pass


class Cachorro(Mamifero):
    pass


class Gato(Mamifero):
    pass


class Leao(Mamifero):
    pass


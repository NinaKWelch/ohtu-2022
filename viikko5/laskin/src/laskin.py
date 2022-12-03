class Summa:
    def __init__(self, sovellus):
        self._sovellus = sovellus

    def suorita(self, syote):
        print(f"Value of arvo is: {syote}")
        self._sovellus.plus(syote)


class Erotus:
    def __init__(self, sovellus):
        self._sovellus = sovellus

    def suorita(self, syote):
        self._sovellus.miinus(syote)


class Nollaus:
    def __init__(self, sovellus):
        self._sovellus = sovellus

    def suorita(self, syote):
        self._sovellus.nollaa(syote)


class Kumoa:
    def __init__(self, sovellus):
        self._sovellus = sovellus

    def suorita(self):
        pass
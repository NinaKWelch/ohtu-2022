class Summa:
    def __init__(self, sovellus):
        self._sovellus = sovellus
        self._arvo = 0

    def suorita(self, syote, arvo):
        self._arvo = arvo
        self._sovellus.plus(syote)

    def kumoa(self):
        self._sovellus.aseta_arvo(self._arvo)

class Erotus:
    def __init__(self, sovellus):
        self._sovellus = sovellus
        self._arvo = 0

    def suorita(self, syote, arvo):
        self._arvo = arvo
        self._sovellus.miinus(syote)

    def kumoa(self):    
        self._sovellus.aseta_arvo(self._arvo)      

class Nollaus:
    def __init__(self, sovellus):
        self._sovellus = sovellus
        self._arvo = 0

    def suorita(self, syote, arvo):
        self._arvo = arvo
        self._sovellus.nollaa()

    def kumoa(self):
        self._sovellus.aseta_arvo(self._arvo)

class Kumoa:
    def __init__(self, sovellus):
        self._sovellus = sovellus


class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError("Kapasiteetin on oltava positiivinen kokonaisluku") 
        self.kapasiteetti = kapasiteetti
        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise ValueError("Kasvatuskoon on oltava positiivinen kokonaisluku") 
        self.kasvatuskoko = kasvatuskoko
        self.taulukko = [0] * self.kapasiteetti
        self.alkioidenLkm = 0
      
    def kuuluu(self, luku):
        if not isinstance(luku, int):
            raise ValueError("Lisattavan arvon on oltava kokonaisluku") 

        return True if luku in self.taulukko else False

    def lisaa(self, luku):
        if not isinstance(luku, int):
            raise ValueError("Lisattavan arvon on oltava kokonaisluku") 

        if not self.kuuluu(luku):
            self.taulukko[self.alkioidenLkm] = luku
            self.alkioidenLkm += 1

            if self.mahtavuus() == len(self.taulukko):
                self.kasvata_taulukkoa()

    def poista(self, luku):
        if not isinstance(luku, int):
            raise ValueError("Lisattavan arvon on oltava kokonaisluku") 

        if self.kuuluu(luku):
            muutettu_taulukko = filter(lambda x: (x != luku), self.taulukko)
            self.taulukko = list(muutettu_taulukko)
            self.alkioidenLkm -= 1

    def kasvata_taulukkoa(self):
        uusi_taulukko = []
        uusi_taulukko.extend(self.taulukko)
        uusi_taulukko.extend([0] * self.kasvatuskoko)
        self.taulukko = uusi_taulukko

    def mahtavuus(self):
        return self.alkioidenLkm

    def to_int_list(self):
        alkio_taulukko = filter(lambda x: (x != 0), self.taulukko)
        self.taulukko = list(alkio_taulukko)
        return self.taulukko

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioidenLkm == 0:
            return "{}"
        elif self.alkioidenLkm == 1:
            return "{" + str(self.taulukko[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioidenLkm - 1):
                tuotos = tuotos + str(self.taulukko[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.taulukko[self.alkioidenLkm - 1])
            tuotos = tuotos + "}"
            return tuotos

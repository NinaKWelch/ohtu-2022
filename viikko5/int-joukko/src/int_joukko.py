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
            self.taulukko = list(filter(lambda x: (x != luku), self.taulukko))
            self.taulukko.extend([0] * 1)
            self.alkioidenLkm -= 1

    def kasvata_taulukkoa(self):
        uusi_taulukko = []
        uusi_taulukko.extend(self.taulukko)
        uusi_taulukko.extend([0] * self.kasvatuskoko)
        self.taulukko = uusi_taulukko

    def mahtavuus(self):
        return self.alkioidenLkm

    def to_int_list(self):
        alkio_taulukko = list(filter(lambda x: (x != 0), self.taulukko))
        alkio_taulukko.sort()
        return alkio_taulukko

    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        yhdiste_joukko = IntJoukko()

        for luku in joukko_a.to_int_list():
            yhdiste_joukko.lisaa(luku)

        for luku in joukko_b.to_int_list():
            yhdiste_joukko.lisaa(luku)

        return yhdiste_joukko

    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        leikkaus_joukko = IntJoukko()

        for luku in joukko_a.to_int_list():
            if luku in joukko_b.to_int_list():
                leikkaus_joukko.lisaa(luku)
       
        return leikkaus_joukko

    @staticmethod
    def erotus(joukko_a, joukko_b):
        erotus_joukko = IntJoukko()

        for luku in joukko_a.to_int_list():
            if not luku in joukko_b.to_int_list():
                erotus_joukko.lisaa(luku)
        
        return erotus_joukko

    def __str__(self):
        if self.alkioidenLkm == 0:
            return "{}"
        elif self.alkioidenLkm == 1:
            return "{" + str(self.taulukko[0]) + "}"
        else:
            string = ", ".join(str(x) for x in self.to_int_list())
            return "{" + string + "}"

from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._ostokset = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2
        tavaramaara = map(lambda o: o.lukumaara(), self._ostokset)
        
        return sum(tavaramaara)
 
    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        hinnat = map(lambda o: o.hinta(), self._ostokset)

        return sum(hinnat)

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        for ostos in self._ostokset:
            if lisattava == ostos.tuote:
                ostos.muuta_lukumaaraa(1)
                return

        self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for ostos in self._ostokset:
            if poistettava == ostos.tuote:
                if ostos.lukumaara() > 1:
                    ostos.muuta_lukumaaraa(-1)
                    return

                if ostos.lukumaara() == 1 and len(self._ostokset) > 1:
                    muokattu_lista = filter(lambda o: o.tuote != poistettava, self._ostokset)
                    self._ostokset = list(muokattu_lista)
                    return
                
                self.tyhjenna()

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self._ostokset = []
    
    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return self._ostokset


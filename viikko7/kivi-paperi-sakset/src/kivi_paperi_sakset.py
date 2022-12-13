from tuomari import Tuomari


class KiviPaperiSakset:
    def __init__(self):
        self._tuomari = Tuomari()

    def pelaa(self):
        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self._kirjaa_siirto(ekan_siirto, tokan_siirto)
            self._nayta_tulos()

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        print("Kiitos!")
        self._nayta_tulos()

    def _ensimmaisen_siirto(self):
      return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, ensimmaisen_siirto):
        # metodin oletustoteutus
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

    def _kirjaa_siirto(self, ekan, tokan):
        self._tuomari.kirjaa_siirto(ekan, tokan)

    def _nayta_tulos(self):
        print(self._tuomari)

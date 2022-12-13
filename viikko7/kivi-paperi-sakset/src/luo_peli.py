from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class LuoPeli:
    def __init__(self, tyyppi: str):
        self._tyyppi = tyyppi

    def peliohjeet(self, text):
        print(text)

    def pelaa(self):
        match self._tyyppi:
            case "a":
                self.peliohjeet(
                    "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
                )

                kaksinpeli = KPSPelaajaVsPelaaja()
                kaksinpeli.pelaa()
            case "b":
                self.peliohjeet(
                    "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
                )

                yksinpeli = KPSTekoaly()
                yksinpeli.pelaa()
            case "c":
                self.peliohjeet(
                    "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
                )

                haastava_yksinpeli = KPSParempiTekoaly()
                haastava_yksinpeli.pelaa()

            case _:
                return
  
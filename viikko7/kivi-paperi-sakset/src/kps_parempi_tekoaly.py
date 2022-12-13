from kivi_paperi_sakset import KiviPaperiSakset
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        super().__init__()
        self._tekoaly = TekoalyParannettu(10)
    
    def _tekoaly_siirto(self):
        return self._tekoaly.anna_siirto()

    def _aseta_tekoaly_siirto(self, siirto):
        self._tekoaly.aseta_siirto(siirto)

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._tekoaly_siirto()
        
        print(f"Tietokone valitsi: {tokan_siirto}")
        self._aseta_tekoaly_siirto(ensimmaisen_siirto)

        return tokan_siirto

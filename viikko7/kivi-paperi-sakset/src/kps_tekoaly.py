from kivi_paperi_sakset import KiviPaperiSakset
from tekoaly import Tekoaly


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        super().__init__()
        self._tekoaly = Tekoaly()

    def _tekoaly_siirto(self):
        return self._tekoaly.anna_siirto()

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._tekoaly_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")
        
        return tokan_siirto
    

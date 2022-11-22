import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        # laitetaan Mock-olio toteuttamaan Viitegeneraattori-luokan metodit
        self.viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())

        # palautetaan aina arvo 42
        # self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 5
            if tuote_id == 3:
                return 0
            
        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(1, "leipa", 3)
            if tuote_id == 3:
                return Tuote(1, "voi", 7)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_oston_tilisiirto_tapahtuu_oikeilla_tiedoilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla asiakkaalla, tilinumeroilla ja summalla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)
    
    def test_kahden_eri_tuotteen_maksaminen_tapahtuu_oikeilla_tiedoilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla asiakkaalla, tilinumeroilla ja summalla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 8)
    
    def test_kahden_saman_tuotteen_maksaminen_tapahtuu_oikeilla_tiedoilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla asiakkaalla, tilinumeroilla ja summalla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 6)
    
    def test_maksaminen_tapahtuu_oikeilla_tiedoilla_jos_yksi_tuotteista_on_loppuunmyyty(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla asiakkaalla, tilinumeroilla ja summalla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)

    def test_uuden_asioinnin_aloittaminen_nollaa_edellisen_ostoksen_tiedot(self):
        # tehdään ensimmaiset ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikealla summalla
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 5)

        # tehdään toiset ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että edellisen ostoksen hinta ei näy uuden ostoksen hinnassa
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 3)

    def test_pyydetaan_uusi_viite_jokaiselle_maksutapahtumalle(self):
        # tehdään ensimmaiset ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # tarkistetaan että tässä vaiheessa viitegeneraattorin metodia uusi on kutsuttu kerran
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)

        # tehdään toiset ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # tarkistetaan että tässä vaiheessa viitegeneraattorin metodia uusi on kutsuttu kaksi kertaa
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

        # tehdään kolmannet ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        # tarkistetaan että tässä vaiheessa viitegeneraattorin metodia uusi on kutsuttu kolme kertaa
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 3)
    
    def test_tuotteen_poisto_korista_tapahtuu_onnistuneesti(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että poistettua tuotetta ei lisätä ostoksiin
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 5)
from src.rezervacije.models import Rezervacija
from src.rezervacije.reservation_service import ServisRezervacija


class FakeIzvor:
    def __init__(self, rezervacije):
        self.rezervacije = rezervacije

    def ucitaj_rezervacije(self):
        return self.rezervacije


class FakeIzvjestaj:
    def __init__(self):
        self.tekst = ""

    def prikazi(self, tekst):
        self.tekst = tekst


def napravi_servis(rezervacije):
    izvor = FakeIzvor(rezervacije)
    izvjestaj = FakeIzvjestaj()

    servis = ServisRezervacija(izvor, izvjestaj)

    return servis, izvjestaj


def test_ukupan_prihod_i_broj_nocenja():
    rezervacije = [
        Rezervacija("Ana", 3, 80),
        Rezervacija("Marko", 5, 65),
    ]

    servis, izvjestaj = napravi_servis(rezervacije)
    servis.obradi_rezervacije()

    assert "Ukupan prihod: 565.00 EUR" in izvjestaj.tekst
    assert "Ukupan broj noćenja: 8" in izvjestaj.tekst


def test_prepoznavanje_skupih_rezervacija():
    rezervacije = [
        Rezervacija("Ana", 3, 80),
        Rezervacija("Marko", 5, 65),
    ]

    servis, izvjestaj = napravi_servis(rezervacije)
    servis.obradi_rezervacije()

    assert "Skupe rezervacije: Marko" in izvjestaj.tekst


def test_prazna_lista_rezervacija():
    servis, izvjestaj = napravi_servis([])
    servis.obradi_rezervacije()

    assert "Ukupan prihod: 0.00 EUR" in izvjestaj.tekst
    assert "Ukupan broj noćenja: 0" in izvjestaj.tekst
    assert "Prosječna cijena rezervacije: 0.00 EUR" in izvjestaj.tekst
    assert "Skupe rezervacije:" in izvjestaj.tekst

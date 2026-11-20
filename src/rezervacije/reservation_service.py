from .protocols import Izvjestaj, IzvorRezervacija


class ServisRezervacija:
    def __init__(self, izvor: IzvorRezervacija, izvjestaj: Izvjestaj):
        self.izvor = izvor
        self.izvjestaj = izvjestaj

    def obradi_rezervacije(self) -> None:
        rezervacije = self.izvor.ucitaj_rezervacije()

        ukupan_prihod = 0
        ukupan_broj_noci = 0
        skupe_rezervacije = []

        for rezervacija in rezervacije:
            ukupan_prihod += rezervacija.ukupna_cijena
            ukupan_broj_noci += rezervacija.noci

            if rezervacija.ukupna_cijena > 240:
                skupe_rezervacije.append(rezervacija.gost)

        prosjecna_cijena = ukupan_prihod / len(rezervacije) if rezervacije else 0

        tekst = (
            f"Ukupan prihod: {ukupan_prihod:.2f} EUR\n"
            f"Ukupan broj noćenja: {ukupan_broj_noci}\n"
            f"Prosječna cijena rezervacije: {prosjecna_cijena:.2f} EUR\n"
            f"Skupe rezervacije: {', '.join(skupe_rezervacije)}"
        )

        self.izvjestaj.prikazi(tekst)

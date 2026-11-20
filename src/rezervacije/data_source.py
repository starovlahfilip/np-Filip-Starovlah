from .models import Rezervacija


class ListaRezervacija:
    def __init__(self, rezervacije: list[Rezervacija]):
        self.rezervacije = rezervacije

    def ucitaj_rezervacije(self) -> list[Rezervacija]:
        return self.rezervacije

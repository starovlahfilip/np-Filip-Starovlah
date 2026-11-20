from typing import Protocol

from .models import Rezervacija


class IzvorRezervacija(Protocol):
    """Definiše način učitavanja rezervacija."""

    def ucitaj_rezervacije(self) -> list[Rezervacija]: ...


class Izvjestaj(Protocol):
    """Definiše način prikazivanja izvještaja."""

    def prikazi(self, tekst: str) -> None: ...

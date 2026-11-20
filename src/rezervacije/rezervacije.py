from .data_source import ListaRezervacija
from .models import Rezervacija
from .reporter import KonzolniIzvjestaj
from .reservation_service import ServisRezervacija


def main():
    rezervacije = [
        Rezervacija("Ana", 3, 80),
        Rezervacija("Marko", 5, 65),
        Rezervacija("Ivana", 2, 120),
        Rezervacija("Petar", 4, 90),
    ]

    izvor = ListaRezervacija(rezervacije)
    izvjestaj = KonzolniIzvjestaj()

    servis = ServisRezervacija(izvor, izvjestaj)
    servis.obradi_rezervacije()


if __name__ == "__main__":
    main()

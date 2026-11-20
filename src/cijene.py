from collections.abc import Iterable


def prosjecna_cijena(cijene: Iterable[float]) -> float:
    """Vraca aritmeticku sredinu cijena.

    Prazan skup cijena nije moguce prosjeciti, pa se u tom slucaju
    podize ValueError. Negativne cijene nijesu dozvoljene.
    """
    vrijednosti = list(cijene)

    if not vrijednosti:
        raise ValueError("Lista cijena ne smije biti prazna.")

    if any(
        not isinstance(cijena, (int, float)) or isinstance(cijena, bool)
        for cijena in vrijednosti
    ):
        raise TypeError("Sve cijene moraju biti brojevi.")

    if any(cijena < 0 for cijena in vrijednosti):
        raise ValueError("Cijene ne mogu biti negativne.")

    return sum(vrijednosti) / len(vrijednosti)

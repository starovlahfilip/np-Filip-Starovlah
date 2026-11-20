from dataclasses import dataclass


@dataclass
class Rezervacija:
    gost: str
    noci: int
    cijena_noci: float

    @property
    def ukupna_cijena(self) -> float:
        return self.noci * self.cijena_noci

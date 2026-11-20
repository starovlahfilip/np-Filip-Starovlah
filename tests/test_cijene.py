import pytest

from src.cijene import prosjecna_cijena


def test_prosjecna_cijena_vise_vrijednosti():
    assert prosjecna_cijena([10, 20, 30]) == 20


def test_prosjecna_cijena_jedna_vrijednost():
    assert prosjecna_cijena([12.5]) == 12.5


def test_prosjecna_cijena_prazna_lista():
    with pytest.raises(ValueError, match="prazna"):
        prosjecna_cijena([])


def test_prosjecna_cijena_negativna_vrijednost():
    with pytest.raises(ValueError, match="negativne"):
        prosjecna_cijena([10, -2])


def test_prosjecna_cijena_neispravan_tip():
    with pytest.raises(TypeError, match="brojevi"):
        prosjecna_cijena([10, "20"])

# Napredno programiranje — Filip Starovlah 

Ovaj GitHub repozitorijum koristi se za sve mini projekte i zadatke iz predmeta
Napredno programiranje.

## Radno okruzenje

- Python 3.12 ili noviji
- Visual Studio Code
- Ruff — provjera kvaliteta i formatiranje Python koda
- pytest — automatsko testiranje

## Instalacija

Kloniraj repozitorijum i udji u njegov direktorijum:

```bash
git clone https://github.com/USERNAME/np-ime-prezime.git
cd np-ime-prezime
```

Kreiraj i aktiviraj virtuelno okruzenje.

Windows:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
```

Instaliraj razvojne alate:

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

## Zadatak: prosjecna cijena

Implementirana je funkcija `prosjecna_cijena(cijene)` u fajlu `src/cijene.py`.
Funkcija racuna aritmeticku sredinu proslijedjenih cijena.

Pravila:
- Ulaz mora sadrzati najmanje jednu cijenu.
- Cijene moraju biti brojevi (`int` ili `float`).
- Negativne cijene nijesu dozvoljene.
- Za prazan skup podize se `ValueError`.
- Za vrijednosti koje nijesu brojevi podize se `TypeError`.

Primjer:

```python
from src.cijene import prosjecna_cijena

print(prosjecna_cijena([10, 20, 30]))  # 20.0
```

## Pokretanje testova

```bash
pytest -v
```

## Ruff — provjera i formatiranje

Provjera:

```bash
ruff check .
```

Automatsko formatiranje:

```bash
ruff format .
```

## AI asistent — upit i uoceni nedostaci

**Upotrijebljeni upit:**

> Napisi Python funkciju `prosjecna_cijena` koja prima kolekciju cijena i vraca
> njihovu aritmeticku sredinu. Obradi slucaj prazne kolekcije i neispravnih
> ulaznih podataka. Napisi pytest testove za normalan slucaj, jednu vrijednost,
> praznu kolekciju, negativnu cijenu i vrijednost pogresnog tipa. Koristi
> citljiv i jednostavan Python kod.

**Uoceni nedostaci i ogranicenja generisanog koda:**

- AI ne zna poslovna pravila zadatka ako nijesu precizno navedena. U ovom
  primjeru pretpostavljeno je da negativne cijene nijesu dozvoljene.
- Nije definisano zaokruzivanje rezultata na odredjeni broj decimala; funkcija
  vraca standardni Python rezultat dijeljenja.
- Za novcane iznose `float` moze dovesti do sitnih gresaka preciznosti. U
  stvarnoj finansijskoj aplikaciji bolje je razmotriti `decimal.Decimal`.
- Generisani kod i testove treba pregledati i pokrenuti prije predaje.

## Struktura projekta

```text
np-ime-prezime/
├── src/
│   ├── __init__.py
│   └── cijene.py
├── tests/
│   └── test_cijene.py
├── .gitignore
├── pyproject.toml
└── README.md
```

# Podaci o hotelskim rezervacijama
rezervacije = [
    {"gost": "Ana", "noci": 3, "cijena_noci": 80},
    {"gost": "Marko", "noci": 5, "cijena_noci": 65},
    {"gost": "Ivana", "noci": 2, "cijena_noci": 120},
    {"gost": "Petar", "noci": 4, "cijena_noci": 90},
]

# Obrada rezervacija
ukupan_prihod = 0
ukupan_broj_nocenja = 0

print("IZVJESTAJ HOTELSKIH REZERVACIJA")
print("-" * 40)

for rezervacija in rezervacije:
    gost = rezervacija["gost"]
    noci = rezervacija["noci"]
    cijena_noci = rezervacija["cijena_noci"]

    ukupna_cijena = noci * cijena_noci

    ukupan_prihod += ukupna_cijena
    ukupan_broj_nocenja += noci

    print(f"Gost: {gost}")
    print(f"Broj nocenja: {noci}")
    print(f"Cijena po noci: {cijena_noci} EUR")
    print(f"Ukupna cijena: {ukupna_cijena} EUR")
    print("-" * 40)

# Prosjecna cijena rezervacije
prosjek = ukupan_prihod / len(rezervacije)

# Izdvajanje skupih rezervacija
skupe_rezervacije = [
    r["gost"] for r in rezervacije if r["noci"] * r["cijena_noci"] > 240
]

# Zavrsni izvjestaj
print("\nUKUPNI IZVJESTAJ")
print(f"Ukupan prihod: {ukupan_prihod} EUR")
print(f"Ukupan broj nocenja: {ukupan_broj_nocenja}")
print(f"Prosjecna vrijednost rezervacije: {prosjek:.2f} EUR")
print(f"Skupe rezervacije: {skupe_rezervacije}")

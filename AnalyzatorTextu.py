'''
author = Petr Šmejkal
'''

uzivatel = input("Napiš své přihlašovací jméno: ")
heslo = input("Napiš své heslo: ")

oddeleni = "-" * 30
print(oddeleni)

uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

if uzivatele.get(uzivatel) == heslo:
    print("Přihlášení proběhlo úspěšně")

else:
    print("Bylo zadáno špatné heslo")
    exit()

print("K analyzování máme 3 texty.")

print(oddeleni)

TEXTS = ["""Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. """,

"""At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.""",

"""The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present."""
]

print(oddeleni)

vyber_textu = (input("Vyber text zadáním čísla od 1 do 3: "))

if vyber_textu.isdigit():
    if int(vyber_textu) in range(1, 4):
        print("Správný výběr")

    else:
        print("Vybral si nesprávné číslo")
        exit()
if vyber_textu.isalpha():
    print("Zadal si text místo čísla")
    exit()

print("Vybral sis text číslo: ", vyber_textu)

print(oddeleni)
vyber_textu = int(vyber_textu)

vyber = TEXTS[vyber_textu - 1]

vynatek = vyber.split(" ")

novy_vynatek = []

for s in vynatek:
    novy_vynatek.append(s.strip(".,\n"))

delka = 0

for s in novy_vynatek:
    if s.isnumeric() or s.isalpha() or s.title():
        delka += 1
print("V textu je ", delka, "slov.")

pocatecni_velke = 0

for s in novy_vynatek:
    if s.istitle():
        pocatecni_velke += 1

print("V textu je ", pocatecni_velke, "slov, která začánají velkým písmenem.")

psany_velky = 0

for s in novy_vynatek:
    if s.isupper():
        if s.isalpha():
            psany_velky += 1
print("V textu je ", psany_velky, "slovo, které je napsané velkými písmeny.")

mala_pismena = 0

for s in novy_vynatek:
    if s.islower():
        mala_pismena += 1
print("V textu je ", mala_pismena, "slov, která jsou napsaná jen malými písmeny.")

cisla = 0

for s in novy_vynatek:
    if s.isnumeric():
        cisla += 1
print("Text obsahuje ", cisla, "čísla.")

celkem = 0

for element in novy_vynatek:
    if isinstance(element, int) or element.isdigit():
        celkem += int(element)
print("Celkový součet čísel je ", celkem, ".")

print("LEN|    OCCURENCES    |NR.")
print(oddeleni)

novy_slovnik = dict()

for i in novy_vynatek:
    novy_slovnik[len(i)] = novy_slovnik.setdefault(len(i), 0) + 1

for delka, pocet in sorted(novy_slovnik.items()):
    print(str(delka) + (2 - len(str(delka))) * " ", pocet * "*" + (20 - pocet) * " ", pocet)
















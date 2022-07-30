"""
Prosta funkcja ktora sprawdza czy dane słowo jest palidromem
"""


def sprawdzimy(slowo):
  print(bool(slowo == slowo[::-1]))
sprawdzimy("100030001")




print("A teraz prosze sam wymysl słowo a ja sprawczy czy jest palidromem")
slowo = input()
sprawdzimy(slowo)

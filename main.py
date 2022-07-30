"""
Prosta funkcja ktora sprawdza czy dane słowo jest palidromem
"""


def sprawdzimy(slowo):
  print(bool(slowo == slowo[::-1]))
sprawdzimy("100030001")

import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko(2,4)
    joukko2 = IntJoukko(1,2)


    joukko.lisaa(33)
    joukko.lisaa(12)
    joukko.lisaa(2)
    joukko2.lisaa(5)
    joukko2.lisaa(2)
    joukko2.lisaa(3)
    joukko2.poista(3)
  
  
    print(joukko.to_int_list())
    print(joukko2.to_int_list())
    print(joukko.yhdiste(joukko, joukko2))
    print(joukko.leikkaus(joukko, joukko2))
    print(joukko.erotus(joukko, joukko2))


if __name__ == "__main__":
    main()

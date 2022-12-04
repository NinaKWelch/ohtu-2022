import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko(2,4)

    joukko.lisaa(2)
    joukko.lisaa(2)
    joukko.lisaa(3)
    joukko.lisaa(2)
    joukko.poista(3)
    joukko.lisaa(4)
    joukko.lisaa(6)
    joukko.lisaa(8)
    joukko.lisaa(9)
    joukko.lisaa(10)
    joukko.lisaa(11)
    joukko.lisaa(12)
    print(joukko.to_int_list())



if __name__ == "__main__":
    main()

# testikoodi tänne jos tarvetta
from ostoskori import Ostoskori
from tuote import Tuote

def main():
    my_basket = Ostoskori()
    my_product = Tuote("maito", 3)

    my_basket.lisaa_tuote(my_product)
    print(my_basket.tavaroita_korissa())
   

if __name__ == "__main__":
    main()
    
# testikoodi tänne jos tarvetta
from ostoskori import Ostoskori
from tuote import Tuote

def main():
    my_basket = Ostoskori()
    my_product_1 = Tuote("Maito", 3)
    my_product_2 = Tuote("Leipä", 5)
    my_basket.lisaa_tuote(my_product_1)
    my_basket.lisaa_tuote(my_product_2)
    print(my_basket.tavaroita_korissa())
    #print(my_basket.hinta())

if __name__ == "__main__":
    main()
    
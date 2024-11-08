def faktorial(cislo):
    vysledek = 1
    x = range(1, cislo+1)
    for i in x:
        vysledek = vysledek * i
        """
        1,2,3,4,5,6,7,8,9,10


        """
    return vysledek
        

        

if __name__=="__main__":
    number = -6
    print(faktorial(number))



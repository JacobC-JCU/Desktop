import sys

def vrat_treti(seznam):
    if len(seznam) < 3:
        return None
    else:
        return seznam[2]
        

def udelej_prumer(cislo):
    x = sum(cislo) / len(cislo)
    return x

def naformatuj_text(student):
    jm = student["jmeno"]
    pr = student["znamky"]
    
    return (f"Jméno: {jm}, Průměr známek: {udelej_prumer(pr)}")


if __name__ == "__main__":
    """polozky = [1,2, 4]
    vysledek = vrat_treti(polozky)
    print(vysledek)
    """
    seznam_cisel = [1,2,3,4,5]
    prumer = udelej_prumer(seznam_cisel)
    print(prumer)

    data = {
        "jmeno" : "Bob",
        "znamky" : [1,2,3,4,5]
    }
    test = naformatuj_text(data)
    print(test)


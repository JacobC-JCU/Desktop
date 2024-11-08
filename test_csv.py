import sys
import csv
import time

def nacti_csv(soubor):
        with open(soubor, "r") as data1:
            try:
                reader = csv.reader(data1) # Načte data
                data1 = [] # Vytvoří prázdný seznam
                for line in reader:
                    data1.append(line) # Zapíše do seznamu všechny hodnoty z tabulek
                
            except FileNotFoundError:
                raise FileNotFoundError(soubor)
            
            return data1

def spoj_data(data1, data2):
    if not data1 or not data2:
        return data1 if data1 else data2

    # Získání hlaviček a dat z obou souborů
    headers1, *rows1 = data1
    headers2, *rows2 = data2

    # Vytvoření slovníků pro snadné vyhledávání
    data_dict1 = {tuple(row[:2]): row[2:] for row in rows1}
    data_dict2 = {tuple(row[:2]): row[2:] for row in rows2}

    # Spojení hlaviček a inicializace výsledného seznamu
    all_headers = list(dict.fromkeys(headers1 + headers2))  # Eliminuje duplicity a udržuje pořadí
    result_data = [all_headers]

    # Spojení dat
    all_keys = set(data_dict1.keys()).union(set(data_dict2.keys()))

    for key in all_keys:
        new_row = list(key) + [data_dict1.get(key, [''])[0]] + [data_dict2.get(key, [''])[0]]
        result_data.append(new_row)

    return result_data


def zapis_csv(soubor, data):
    with open(soubor, "w" , newline="") as file:
        writer = csv.writer(file) # Určí, kam budeme zapisovat
        writer.writerows(data) # Zapíše data


if __name__ == "__main__":
    try:
        soubor1 = sys.argv[1]
        soubor2 = sys.argv[2]
        csv_data1 = nacti_csv(soubor1)
        csv_data2 = nacti_csv(soubor2)
        vysledna_data = spoj_data(csv_data1, csv_data2)
        print(vysledna_data)
        zapis_csv("vysledny_excel.csv", vysledna_data)
    except IndexError:
        print("Nebyly zadany soubory")
    except FileNotFoundError as e:
        print(f"Soubor s názvem {e} neexistuje")
    except Exception: # Zachytí všechny ostatní výjímky
        print("Nastal neočekávaná chyba")
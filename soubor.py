
def zapis_soubor(jmeno_souboru):
    with open(jmeno_souboru, "w", encoding="utf-8") as fp:
        fp.write("Ahoj všichni\n")
        fp.write("Ahoj ostatní\n")


def precti_soubor(jmeno_souboru):
    with open(jmeno_souboru, "r", encoding="utf-8") as fp:
        data = fp.read()
        print(data)
        fp.seek(0)
        for line in fp:
            line = line.strip() # Zajistí, aby print netvyářel nové volné řádky
            print(line)


if __name__ == "__main__":
    soubor = "data.txt"
    zapis_soubor(soubor)
    precti_soubor(soubor)

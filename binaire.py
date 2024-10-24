def int_to_binary(number):
    return bin(number)

def string_to_binary(chaine):
    return ' '.join(format(ord(char), '08b') for char in chaine)

def convert_to_binary():
    choix = input("Tapez '1' pour convertir un entier ou '2' pour convertir une chaîne de caractères : ")

    if choix == '1':
        nombre = int(input("Entrez un entier : "))
        print(f"Le nombre {nombre} en binaire est : {int_to_binary(nombre)}")
    elif choix == '2':
        texte = input("Entrez une chaîne de caractères : ")
        print(f"Le texte '{texte}' en binaire est : {string_to_binary(texte)}")
    else:
        print("Choix invalide")

if __name__ == "__main__":
    convert_to_binary()


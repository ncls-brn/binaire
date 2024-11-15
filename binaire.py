def int_to_binary(number):
    return bin(number)[2:].zfill(8)  # Convertit un entier en binaire sur 8 bits

def string_to_binary(chaine):
    return ' '.join(format(ord(char), '08b') for char in chaine)

def binary_to_int(binaire):
    return int(binaire, 2)  # Convertit un code binaire en entier

def binary_to_string(binaire_texte):
    # Divise la chaîne binaire en morceaux de 8 bits et les convertit en caractères
    chars = binaire_texte.split()
    return ''.join(chr(int(char, 2)) for char in chars)

def convert_to_binary():
    choix = input(
        "Tapez '1' pour convertir un entier en binaire, '2' pour convertir une chaîne de caractères en binaire, "
        "'3' pour convertir un code binaire en entier, ou '4' pour convertir un code binaire en texte : "
    )

    if choix == '1':
        nombre = int(input("Entrez un entier : "))
        print(f"Le nombre {nombre} en binaire est : {int_to_binary(nombre)}")

    elif choix == '2':
        texte = input("Entrez une chaîne de caractères : ")
        binaire_texte = string_to_binary(texte)
        longueur = len(texte)
        print(f"Le texte '{texte}', avec une longueur de {longueur} caractères, se traduit en binaire par : {binaire_texte}")

    elif choix == '3':
        binaire = input("Entrez un code binaire pour convertir en entier : ")
        try:
            nombre = binary_to_int(binaire)
            print(f"Le code binaire '{binaire}' correspond à l'entier : {nombre}")
        except ValueError:
            print("Erreur : Le code binaire n'est pas valide pour une conversion en entier!")

    elif choix == '4':
        binaire_texte = input("Entrez un code binaire pour convertir en texte (8 bits par caractère, séparés par des espaces) : ")
        try:
            texte = binary_to_string(binaire_texte)
            print(f"Le code binaire '{binaire_texte}' correspond au texte : '{texte}'")
        except ValueError:
            print("Erreur : Le code binaire n'est pas valide pour une conversion en texte!")

    else:
        print("Choix invalide!")

if __name__ == "__main__":
    convert_to_binary()

def int_to_binary(number):
    return bin(number)[2:].zfill(8)

def string_to_binary(chaine):
    return ' '.join(format(ord(char), '08b') for char in chaine)

def binary_to_int(binaire):
    return int(binaire, 2)

def binary_to_string(binaire_texte):
    # Divise la chaîne binaire en morceaux de 8 bits et les convertit en caractères
    chars = binaire_texte.split()
    return ''.join(chr(int(char, 2)) for char in chars)

def guess_and_convert_binary(binaire):
    # Vérifier si le binaire contient des espaces (ce qui indiquerait une chaîne de caractères)
    if ' ' in binaire or len(binaire) % 8 == 0:
        # Suppose que c'est une chaîne de caractères en binaire
        try:
            texte = binary_to_string(binaire)
            print(f"Le code binaire '{binaire}' correspond au texte : '{texte}'")
        except ValueError:
            print("Erreur : Le code binaire n'est pas valide pour une conversion en chaîne de caractères.")
    else:
        # Suppose que c'est un entier en binaire
        try:
            nombre = binary_to_int(binaire)
            print(f"Le code binaire '{binaire}' correspond à l'entier : {nombre}")
        except ValueError:
            print("Erreur : Le code binaire n'est pas valide, pour une conversion en entier.")

def convert_to_binary():
    choix = input("Tapez '1' pour convertir un entier en binaire, '2' pour convertir une chaîne de caractères en binaire, ou '3' pour convertir un code binaire sans spécifier le type : ")

    if choix == '1':
        nombre = int(input("Entrez un entier : "))
        print(f"Le nombre {nombre} en binaire est : {int_to_binary(nombre)}")

    elif choix == '2':
        texte = input("Entrez une chaîne de caractères: ")
        binaire_texte = string_to_binary(texte)
        longueur = len(texte)
        print(f"Le texte '{texte}' ,avec une longueur de {longueur} caractères se traduit en binaire par : {binaire_texte}")

    elif choix == '3':
        binaire = input("Entrez un code binaire : ")
        guess_and_convert_binary(binaire)

    else:
        print("Choix invalide!")

if __name__ == "__main__":
    convert_to_binary()

""" Somme des chiffres d'un nombre """
def sum_of_digits(n):
    # Initialiser la somme à 0
    total = 0
    # Convertir le nombre en chaîne pour pouvoir itérer sur chaque chiffre
    chaine_nombre=str(n)
    for chiffre in chaine_nombre: 
        # Ajouter la valeur entière du chiffre à la somme
        total += int(chiffre)
    return total

if __name__ == "__main__":
    # Demander à l'utilisateur d'entrer un nombre
    enter_value = input("Veuillez entrer un nombre entier positif: ")
    
    # Vérifier si l'entrée peut être convertie en entier
    if enter_value.isdigit():  # Vérifie si l'entrée est composée uniquement de chiffres
        number = int(enter_value)
        
        # Vérifier si le nombre est positif
        if number < 0:
            print("Veuillez entrer un nombre entier positif.")
        else:
            # Appeler la fonction et afficher le résultat si l'entrée est valide
            print("La somme des chiffres est:", sum_of_digits(number))
    else:
        # Gérer le cas où l'entrée n'est pas un nombre entier valide
        print("Entrée invalide. Veuillez entrer un nombre entier positif.")
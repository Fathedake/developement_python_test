""" Plus longue sous-chaine unique"""
def longest_unique_substring(s):
    # Dictionnaire pour stocker les derniers indices des caractères
    char_index_map = {}
    start = 0  # Début de la fenêtre
    max_length = 0  # Longueur maximale de la sous-chaîne sans répétition
    
    for end in range(len(s)):
        char = s[end]
        
        # Si le caractère est déjà dans la fenêtre, ajuster le début de la fenêtre
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        
        # Mettre à jour l'indice du caractère actuel
        char_index_map[char] = end
        
        # Calculer la longueur de la fenêtre actuelle et mettre à jour la longueur maximale
        max_length = max(max_length, end - start + 1)
    
    return max_length


if __name__ == "__main__":
    s = input("Entrez une chaîne : ")
    print(f"La longueur de la plus longue sous-chaîne sans caractères répétés est : {longest_unique_substring(s)}")

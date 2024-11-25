""" Anagrammes """
from collections import Counter

def are_anagrams(mot1, mot2):
    # On enlève les espaces et on met tout en minuscules
    mot1 = mot1.replace(" ", "").lower()
    mot2 = mot2.replace(" ", "").lower()
    
    # On utilise Counter pour compter les fréquences des lettres
    return Counter(mot1) == Counter(mot2)

if __name__ == "__main__":
    mot1 = input("Entrez le premier mot : ")
    mot2 = input("Entrez le second mot : ")
    
    if are_anagrams(mot1, mot2):
        print("Les mots sont des anagrammes.")
    else:
        print("Les mots ne sont pas des anagrammes.")


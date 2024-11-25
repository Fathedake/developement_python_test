""" Tri persionnalisé """
def custom_sort(strings):
    # Trier d'abord par la longueur des chaînes, puis par ordre alphabétique en cas d'égalité
    return sorted(strings, key=lambda x: (len(x), x))

# Exemple d'utilisation
if __name__ == "__main__":
    strings = ["banane", "kiwi", "pomme", "orange", "figue"]
    sorted_strings = custom_sort(strings)
    print(sorted_strings)

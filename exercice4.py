""" Nombre manquant dans la liste """
def find_missing_number(nums):
    # Calculer le minimum et le maximum de la liste
    min_num = min(nums)
    max_num = max(nums)
    
    # Calculer la somme attendue de tous les nombres entre min_num et max_num
    total_sum = (max_num * (max_num + 1)) // 2 - (min_num * (min_num - 1)) // 2
    
    # Calculer la somme réelle des éléments dans nums
    actual_sum = sum(nums)
    
    # La différence entre la somme attendue et la somme réelle donne le nombre manquant
    return total_sum - actual_sum

if __name__ == "__main__":
    nums = [15, 16, 18]  # Exemple où 17 manque
    print(f"Le nombre manquant est : {find_missing_number(nums)}")


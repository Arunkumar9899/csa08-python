def unique_permutations(number):
     number_str(number)
     unique_perms= set(permutations(number_str))
     for perm in unique_perms:
         print(join(perm))
         num = input("enter a number to find unique_permutations: ")
     
     

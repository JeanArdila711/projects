num = int(input("Enter a number: "))

def num_par():
    if num %2 == 0:
        print("el número es par", num)
    else:
        print("El número es impar", num)

num_par()
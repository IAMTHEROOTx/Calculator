nombre1 = input("Enter a number: ")
nombre2 = input("Enter a second number: ")

if not nombre1.isnumeric() and not nombre2.isnumeric():
    print("Erreur: les deux nombres doivent être des nombres entiers")
    raise SystemExit("Fin du programme")
    
nombre1 = int(nombre1)
nombre2 = int(nombre2)
    

operation = input("Choose an operation: You can do +, -, *, /")
if operation == "+" or "-" or "*" or "/":
    if operation == "+":
        resultat = nombre1 + nombre2
    elif operation == "-":
        resultat = nombre1 - nombre2
    elif operation == "*":
        resultat = nombre1 * nombre2
    elif operation == "/":
        if nombre2 == 0:
            print(f"The {operation} can have 0 as second number")
            raise SystemExit("Quitter le programme")
        else:
            resultat = nombre1 / nombre2
            resultat = round(resultat)
    else: 
        raise SystemExit("Quitter le programme")
        
print(f"The result of the operation {operation} is {resultat}")
        
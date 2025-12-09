def calcular_stacks_cofres(total_bloques):
    if total_bloques <= 0:
        return "Ingresa una cantidad válida de bloques."

    stacks = total_bloques / 64
    cofres_dobles = stacks / 54

    resultado = (
        f"Total de bloques: {total_bloques}\n"
        f"Stacks: {stacks:.2f}\n"
        f"Cofres dobles: {cofres_dobles:.2f}"
    )
    return resultado

try:
    total = int(input("Ingresa la cantidad total de bloques: "))
    print(calcular_stacks_cofres(total))
except ValueError:
    print("Por favor, ingresa un número entero válido.")

print("Bienvenido, vamos a jugar un juego muy divertido")
print("El cual consiste en adivinar el numero haciendo operaciones matematicas, no importa el numero el resultado sera el mismo")
VecesJuego = int(input("En primer lugar escriba cuanta veces desea jugar el juego: "))

for numero in range(VecesJuego):
    numero = int(input("Por favor ingrese cualquier numero: "))
    
    NunMul = numero * 3
    NumSum = NunMul + 6
    NumDiv = NumSum / 3
    NumFinal = NumDiv - numero

    print(f"El resultado del numero que usted escribio es {NumFinal} ")


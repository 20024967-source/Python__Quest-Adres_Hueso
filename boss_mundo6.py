equipo = ["messi", "pedri", "yamal"]

nuevo = input("¿Cuál es el nombre del nuevo jugador?: ")
equipo.append(nuevo)

lesionado = input("¿Qué jugador sale por lesión?: ")
equipo.remove(lesionado)

print("--- PLANTILLA OFICIAL CONFIRMADA ---")

for jugador in equipo:
    print(f"Jugador confirmado: {jugador}")
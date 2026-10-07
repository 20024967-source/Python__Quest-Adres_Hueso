usuario = int(input("cuantos minutos faltan del partido?"))
minuto = usuario
falta = input(" ¿la falta fue violada?")
   
es_violenta = falta
hombre = input("¿era ultimo hombre?")

ultimo_hombre = hombre

if es_violenta == "si" or ultimo_hombre == "si":
    print(" TARJETA ROJA DIRECTA, EL jugador abandona la cancha.")
elif minuto >=85:
    print("tarjeta amarilla y advertencia poor falta tactica al final del partido.")
else:
    print("solo falta ordinaria. sigue el juego.")

goles_anotados = 0
for tiro in range(1, 6):
    direccion = input("donde quieres patear? (izquierda/centro/derecha:)")
 
    if direccion == "derecha": 
       print ("GOOOOOL eL PORTERO SE TIRO AL LADO CONTRARIO.")
       goles_anotados = goles_anotados + 1
    else:
       print (" ATAJON! EL PORTERO ATAJO EL DISPARON.")

print(f"tanda terminada. Marcador final: {goles_anotados} goles de 5 tiros.")


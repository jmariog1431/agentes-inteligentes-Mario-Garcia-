import time
import random

def cambiar_semaforo(trafico):
    if trafico > 10:
        tiempos = [10, 3, 12]  # Verde, Amarillo, Rojo
    elif 5 <= trafico <= 10:
        tiempos = [7, 3, 9]
    else:
        tiempos = [5, 2, 6]
    
    for color, tiempo in zip(["VERDE", "AMARILLO", "ROJO"], tiempos):
        print(f"Semáforo en {color} - Tiempo: {tiempo} segundos")
        time.sleep(tiempo)

while True:
    trafico = random.randint(0, 20)
    print(f"Vehículos detectados: {trafico}")
    cambiar_semaforo(trafico)

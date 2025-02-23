import random
import time

def imprimir_cuadricula(robot, objetivo):
    for fila in range(5):
        for columna in range(5):
            if (fila, columna) == robot:
                print(" R ", end="")  
            elif (fila, columna) == objetivo:
                print(" O ", end="")  
            else:
                print(" . ", end="")  
        print()
    print("-" * 15)

def mover_robot(robot, objetivo):
    rx, ry = robot
    ox, oy = objetivo
    
    if rx < ox:
        rx += 1  
    elif rx > ox:
        rx -= 1 
    if ry < oy:
        ry += 1  
    elif ry > oy:
        ry -= 1 
    return (rx, ry)

def inicializar_posiciones():
    robot = (random.randint(0, 4), random.randint(0, 4))
    objetivo = robot
    while objetivo == robot:
        objetivo = (random.randint(0, 4), random.randint(0, 4))
    return robot, objetivo

robot, objetivo = inicializar_posiciones()
 
while robot != objetivo:
    imprimir_cuadricula(robot, objetivo)
    time.sleep(0.5)  
    robot = mover_robot(robot, objetivo)

imprimir_cuadricula(robot, objetivo)
print("¡El robot encontró el objetivo!")

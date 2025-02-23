def diagnostico():
    print("Bienvenido al sistema de diagnóstico médico básico.")
    
    preguntas = {
        "tos": "¿Tienes tos? (sí/no): ",
        "fiebre": "¿Tienes fiebre? (sí/no): ",
        "dolor_cabeza": "¿Tienes dolor de cabeza? (sí/no): ",
        "cansancio": "¿Te sientes cansado/a? (sí/no): ",
        "dolor_garganta": "¿Tienes dolor de garganta? (sí/no): "
    }
    
    sintomas = {sintoma: input(pregunta).strip().lower() for sintoma, pregunta in preguntas.items()}
    
    for clave in sintomas:
        if sintomas[clave] in ["si", "sí"]:
            sintomas[clave] = "sí"
        else:
            sintomas[clave] = "no"
   
    print("\n---------------------------")
    if sintomas["tos"] == "sí" and sintomas["fiebre"] == "sí" and sintomas["dolor_cabeza"] == "sí":
        print("Diagnóstico: Podrías tener una gripe o resfriado. Te recomendamos descansar e hidratarte bien.")
    elif sintomas["tos"] == "sí" and sintomas["fiebre"] == "sí" and sintomas["dolor_garganta"] == "sí":
        print("Diagnóstico: Podrías tener una infección viral. Si los síntomas persisten, consulta a un médico.")
    elif sintomas["fiebre"] == "sí" and sintomas["dolor_cabeza"] == "sí" and sintomas["cansancio"] == "sí":
        print("Diagnóstico: Podrías estar experimentando un cuadro de fatiga general o gripe.")
    elif sintomas["tos"] == "sí" and sintomas["dolor_garganta"] == "sí":
        print("Diagnóstico: Puede ser un resfriado o faringitis. Considera visitar un médico si los síntomas empeoran.")
    elif sintomas["cansancio"] == "sí" and sintomas["dolor_cabeza"] == "sí":
        print("Diagnóstico: Puede ser agotamiento o estrés. Descansa y mantén una buena hidratación.")
    else:
        print("Diagnóstico: No se encontraron combinaciones preocupantes de síntomas. Si te sientes mal, consulta a un médico para una mejor evaluación.")
    print("---------------------------")

diagnostico()


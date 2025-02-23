import random

def recomendar_film():
    catalogo = {
        "acción": ["John Wick", "Mad Max: Fury Road", "Gladiador", "Duro de Matar"],
        "comedia": ["Superbad", "La Máscara", "¿Qué pasó ayer?", "Dos tontos en fuga"],
        "ciencia ficción": ["Interstellar", "Blade Runner 2049", "El Origen", "Matrix"],
        "romántica": ["Diario de una Pasión", "Bajo la Misma Estrella", "La La Land", "Titanic"]
    }

    generos_disponibles = ", ".join(catalogo.keys())  # Lista dinámica de géneros disponibles
    
    while True:
        preferencia = input(f"¿Cuál es tu género favorito de película? ({generos_disponibles}): ").strip().lower()
        
        if preferencia in catalogo:
            print(f"Te recomendamos ver: {random.choice(catalogo[preferencia])}")
            
            otra_sugerencia = input("¿Quieres otra recomendación? (sí/no): ").strip().lower()
            if otra_sugerencia in ["no", "n"]:
                print("Gracias por utilizar el asistente de recomendación de películas. ¡Hasta pronto!")
                break
        else:
            print(f"Lo siento, no tenemos recomendaciones para ese género. Prueba con: {generos_disponibles}.")

recomendar_film()

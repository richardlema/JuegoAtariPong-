# estado.py — Estado global del juego
 
from constantes import (
    ANCHO_VENTANA, ALTO_VENTANA,
    ANCHO_JUGADOR, ALTO_JUGADOR,
    VELOCIDAD_BASE
)
 
 
def estado_inicial():
    """Devuelve un diccionario con el estado inicial del juego."""
    return {
        # Jugador 1 (izquierda)
        "j1_x":    60,
        "j1_y":    ALTO_VENTANA // 2 - ALTO_JUGADOR // 2,
        "vel1y":   0,
        "puntos1": 0,
 
        # Jugador 2 (derecha)
        "j2_x":    ANCHO_VENTANA - 60 - ANCHO_JUGADOR,
        "j2_y":    ALTO_VENTANA // 2 - ALTO_JUGADOR // 2,
        "vel2y":   0,
        "puntos2": 0,
 
        # Pelota
        "pelota_x": ANCHO_VENTANA // 2,
        "pelota_y": ALTO_VENTANA  // 2,
        "vel_px":   VELOCIDAD_BASE,
        "vel_py":   VELOCIDAD_BASE,
 
        # Control de juego
        "ganador":  None,   # None | 1 | 2
        "corriendo": True,
    }
 
 
def reiniciar_pelota(estado):
    """Coloca la pelota en el centro e invierte su dirección horizontal."""
    estado["pelota_x"] = ANCHO_VENTANA // 2
    estado["pelota_y"] = ALTO_VENTANA  // 2
    estado["vel_px"]  *= -1
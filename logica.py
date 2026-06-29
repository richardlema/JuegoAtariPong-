
import pygame
from constantes import (
    ALTO_VENTANA, ANCHO_VENTANA,
    ALTO_JUGADOR, RADIO_PELOTA,
    VELOCIDAD_BASE, PUNTOS_GANAR
)
from estado import reiniciar_pelota
 
 
def manejar_eventos(estado):
    """
    Procesa eventos de teclado.
    Retorna False si el usuario cierra la ventana.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            estado["corriendo"] = False
            return
 
        # Reiniciar si hay ganador y se presiona ENTER
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and estado["ganador"] is not None:
                from estado import estado_inicial
                nuevo = estado_inicial()
                estado.update(nuevo)
                return
 
        if estado["ganador"] is not None:
            return  # no procesar movimiento si hay ganador
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                estado["vel1y"] = -VELOCIDAD_BASE
            if event.key == pygame.K_s:
                estado["vel1y"] =  VELOCIDAD_BASE
            if event.key == pygame.K_UP:
                estado["vel2y"] = -VELOCIDAD_BASE
            if event.key == pygame.K_DOWN:
                estado["vel2y"] =  VELOCIDAD_BASE
 
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                estado["vel1y"] = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                estado["vel2y"] = 0
 
 
def mover_jugadores(estado):
    """Actualiza posición de jugadores respetando límites de pantalla."""
    estado["j1_y"] += estado["vel1y"]
    estado["j2_y"] += estado["vel2y"]
 
    estado["j1_y"] = max(0, min(estado["j1_y"], ALTO_VENTANA - ALTO_JUGADOR))
    estado["j2_y"] = max(0, min(estado["j2_y"], ALTO_VENTANA - ALTO_JUGADOR))
 
 
def mover_pelota(estado, audio):
    """
    Mueve la pelota y gestiona rebotes en paredes superior/inferior.
    Recibe el módulo audio para reproducir efectos.
    """
    if estado["ganador"] is not None:
        return
 
    estado["pelota_x"] += estado["vel_px"]
    estado["pelota_y"] += estado["vel_py"]
 
    # Rebote en techo y suelo
    if (estado["pelota_y"] - RADIO_PELOTA <= 0 or
            estado["pelota_y"] + RADIO_PELOTA >= ALTO_VENTANA):
        estado["vel_py"] *= -1
        audio.sonido_rebote()
 
 
def verificar_punto(estado, audio):
    """
    Comprueba si la pelota salió por un lateral.
    Suma punto al jugador correspondiente y verifica si hay ganador.
    """
    if estado["ganador"] is not None:
        return
 
    if estado["pelota_x"] + RADIO_PELOTA > ANCHO_VENTANA:
        estado["puntos1"] += 1
        audio.sonido_punto()
        _verificar_ganador(estado)
        reiniciar_pelota(estado)
 
    elif estado["pelota_x"] - RADIO_PELOTA < 0:
        estado["puntos2"] += 1
        audio.sonido_punto()
        _verificar_ganador(estado)
        reiniciar_pelota(estado)
 
 
def _verificar_ganador(estado):
    """Marca al ganador si algún jugador alcanzó el límite de puntos."""
    if estado["puntos1"] >= PUNTOS_GANAR:
        estado["ganador"] = 1
    elif estado["puntos2"] >= PUNTOS_GANAR:
        estado["ganador"] = 2
 
 
def detectar_colisiones(estado, rect_j1, rect_j2, rect_pelota, audio):
    """Invierte velocidad horizontal de la pelota al colisionar con un jugador."""
    if rect_pelota.colliderect(rect_j1) or rect_pelota.colliderect(rect_j2):
        estado["vel_px"] *= -1
        audio.sonido_golpe()
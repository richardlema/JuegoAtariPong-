
import pygame
from constantes import (
    ANCHO_VENTANA, ALTO_VENTANA,
    ANCHO_JUGADOR, ALTO_JUGADOR,
    RADIO_PELOTA,
    BLACK, WHITE, GRAY, YELLOW, GREEN
)
 
pygame.font.init()
fuente_marcador  = pygame.font.SysFont("Arial", 56, bold=True)
fuente_etiquetas = pygame.font.SysFont("Arial", 26)
fuente_ganador   = pygame.font.SysFont("Arial", 72, bold=True)
fuente_reinicio  = pygame.font.SysFont("Arial", 32)
 
 
def dibujar_campo(surface):
    """Dibuja la línea central punteada."""
    for y in range(0, ALTO_VENTANA, 30):
        pygame.draw.rect(surface, GRAY, (ANCHO_VENTANA // 2 - 2, y, 4, 15))
 
 
def dibujar_jugadores(surface, estado):
    """Dibuja los jugadores y retorna sus rectángulos."""
    rect_j1 = pygame.draw.rect(
        surface, WHITE,
        (estado["j1_x"], estado["j1_y"], ANCHO_JUGADOR, ALTO_JUGADOR)
    )
    rect_j2 = pygame.draw.rect(
        surface, WHITE,
        (estado["j2_x"], estado["j2_y"], ANCHO_JUGADOR, ALTO_JUGADOR)
    )
    return rect_j1, rect_j2
 
 
def dibujar_pelota(surface, estado):
    """Dibuja la pelota y retorna su rectángulo."""
    rect_pelota = pygame.draw.circle(
        surface, WHITE,
        (int(estado["pelota_x"]), int(estado["pelota_y"])),
        RADIO_PELOTA
    )
    return rect_pelota
 
 
def dibujar_marcador(surface, puntos1, puntos2):
    """Muestra el marcador y etiquetas de controles."""
    texto = fuente_marcador.render(f"{puntos1}   {puntos2}", True, WHITE)
    rect  = texto.get_rect(center=(ANCHO_VENTANA // 2, 45))
    surface.blit(texto, rect)
 
    etiq1 = fuente_etiquetas.render("J1  W/S", True, GRAY)
    etiq2 = fuente_etiquetas.render("J2  ↑/↓", True, GRAY)
    surface.blit(etiq1, (60,  12))
    surface.blit(etiq2, (ANCHO_VENTANA - 120, 12))
 
 
def dibujar_pantalla_ganador(surface, ganador):
    """Muestra la pantalla de victoria con el ganador."""
    # Overlay semitransparente
    overlay = pygame.Surface((ANCHO_VENTANA, ALTO_VENTANA), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    surface.blit(overlay, (0, 0))
 
    texto = fuente_ganador.render(f"¡Jugador {ganador} gana!", True, YELLOW)
    rect  = texto.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2 - 40))
    surface.blit(texto, rect)
 
    reinicio = fuente_reinicio.render("Presiona ENTER para jugar de nuevo", True, WHITE)
    rect2    = reinicio.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2 + 50))
    surface.blit(reinicio, rect2)
 
 
def dibujar_todo(surface, estado):
    """
    Función principal de dibujo.
    Limpia la pantalla, dibuja todos los elementos y retorna los rectángulos.
    """
    surface.fill(BLACK)
    dibujar_campo(surface)
    rect_j1, rect_j2 = dibujar_jugadores(surface, estado)
    rect_pelota       = dibujar_pelota(surface, estado)
    dibujar_marcador(surface, estado["puntos1"], estado["puntos2"])
 
    if estado["ganador"] is not None:
        dibujar_pantalla_ganador(surface, estado["ganador"])
 
    return rect_j1, rect_j2, rect_pelota
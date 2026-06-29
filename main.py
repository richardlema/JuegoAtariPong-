
import pygame
from constantes import ANCHO_VENTANA, ALTO_VENTANA, FPS
from estado   import estado_inicial
from logica   import manejar_eventos, mover_jugadores, mover_pelota, verificar_punto, detectar_colisiones
from dibujo   import dibujar_todo
from audio    import Audio


def main():
    pygame.init()

    screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Pong — Primer jugador en llegar a 5 gana")
    clock  = pygame.time.Clock()

    estado = estado_inicial()
    audio  = Audio()           # inicia música de fondo automáticamente

    while estado["corriendo"]:
        # 1. Eventos de teclado
        manejar_eventos(estado)

        # 2. Lógica de juego (solo si no hay ganador)
        if estado["ganador"] is None:
            mover_jugadores(estado)
            mover_pelota(estado, audio)
            verificar_punto(estado, audio)

        # 3. Dibujo y obtención de rectángulos para colisiones
        rect_j1, rect_j2, rect_pelota = dibujar_todo(screen, estado)

        # 4. Colisiones pelota-jugador
        if estado["ganador"] is None:
            detectar_colisiones(estado, rect_j1, rect_j2, rect_pelota, audio)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
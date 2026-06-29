# audio.py — Música y efectos usando solo pygame (sin numpy)

import pygame
import struct
import math

SAMPLE_RATE = 44100


def _generar_tono(frecuencia: float, duracion: float, volumen: float = 0.3) -> pygame.mixer.Sound:
    """Genera un tono sinusoidal usando struct, sin numpy."""
    n_samples = int(SAMPLE_RATE * duracion)
    buf = struct.pack(
        f"{n_samples}h",
        *[int(math.sin(2 * math.pi * frecuencia * i / SAMPLE_RATE) * volumen * 32767)
          for i in range(n_samples)]
    )
    sound = pygame.mixer.Sound(buffer=buf)
    return sound


def _generar_musica_fondo() -> pygame.mixer.Sound:
    """Genera un arpegio simple en loop."""
    notas     = [220.0, 277.0, 330.0, 277.0]
    duracion  = 0.4  # segundos por nota
    n_seg     = int(SAMPLE_RATE * duracion)
    muestras  = []

    for freq in notas:
        for i in range(n_seg):
            val = int(math.sin(2 * math.pi * freq * i / SAMPLE_RATE) * 0.12 * 32767)
            muestras.append(val)

    buf   = struct.pack(f"{len(muestras)}h", *muestras)
    sound = pygame.mixer.Sound(buffer=buf)
    return sound


class Audio:
    """Gestiona todos los sonidos y la música del juego."""

    def __init__(self):
        if not pygame.mixer.get_init():
            pygame.mixer.init(frequency=SAMPLE_RATE, size=-16, channels=1, buffer=512)

        self._sfx_rebote = _generar_tono(440,  0.05, volumen=0.4)
        self._sfx_golpe  = _generar_tono(330,  0.08, volumen=0.5)
        self._sfx_punto  = _generar_tono(660,  0.25, volumen=0.6)
        self._musica     = _generar_musica_fondo()

        self._canal_musica = pygame.mixer.Channel(0)
        self._canal_musica.set_volume(0.25)
        self._canal_musica.play(self._musica, loops=-1)

    def sonido_rebote(self):
        pygame.mixer.Channel(1).play(self._sfx_rebote)

    def sonido_golpe(self):
        pygame.mixer.Channel(2).play(self._sfx_golpe)

    def sonido_punto(self):
        pygame.mixer.Channel(3).play(self._sfx_punto)

    def pausar_musica(self):
        self._canal_musica.pause()

    def reanudar_musica(self):
        self._canal_musica.unpause()
# Importamos la libreria pygame
import pygame
#Inicializamos la libreria pygame
pygame.init() 

#Definicion  de colores Rgb
Black = (0 , 0 , 0)
White = (255,255,255)

#ancho de jugador 
anchoJugador =90
largoJugardor= 15

#tamaño de la ventana
# y VERTICAL  , x HORIZONTAL
size = (1500 ,900)

#creamos la ventana
screen = pygame.display.set_mode(size)

#Tempo
clock = pygame.time.Clock()


#salida de juego
game_over = False

#Cordena de jugador Uno 

player1XCordenada = 60
player1YCordenada = 400

#velocidad del jugador
velocidad1y = 0


#Cordena de jugador dos 

player2XCordenada = 1400
player2YCordenada = 400

velocidad2y = 0

#Coordenadas de la pelota
pelotaX = 750
pelotay = 450

pelotaXVelocidad = 3
pelotayVelocidad =  3

#velocidad del jugador dos 
velocidadpelota = 0



#bucle que permite la apertura de la pantalla con los tamaños y colores establecidos
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
        #Movimiento de jugadores 
        
        if event.type == pygame.KEYDOWN:
            #jugador 1
            if event.key == pygame.K_w:
                velocidad1y = -3
            if event.key == pygame.K_s:
                velocidad1y = 3
            #jugador 2
            if event.key == pygame.K_UP:
                velocidad2y = -3
            if event.key == pygame.K_DOWN:
                velocidad2y = 3
                
        if event.type == pygame.KEYUP:
            #jugador 1
            if event.key == pygame.K_w:
                velocidad1y = 0
            if event.key == pygame.K_s:
                velocidad1y = 0
            #jugador 2
            if event.key == pygame.K_UP:
                velocidad2y = 0
            if event.key == pygame.K_DOWN:
                velocidad2y = 0
                
    #Pelota rebota rebota en cada lado de la pantalla
    
    if pelotay > 900 or pelotay < 35 :
        print(pelotay)
        
        pelotayVelocidad *= -1
        
    
    if pelotaX > 1500:
        pelotaX = 750
        pelotay = 450
        
        
        pelotaXVelocidad *= -1
        pelotayVelocidad *= -1
        
    if pelotaX < 0:
        pelotaX = 750
        pelotay = 450
        
        pelotaXVelocidad *= -1
        pelotayVelocidad *= -1
                
    #Modificacion de coordendas para  los jugadores 1 y 2 
    
    player1YCordenada += velocidad1y
    player2YCordenada += velocidad2y 
    
    #movimieto de la pelota
    pelotaX += pelotaXVelocidad
    pelotay += pelotayVelocidad
    

                
    #logica de programacion 
                
    screen.fill(Black)
    #zona de dibujo *--------------------*
    #creacion de del primer player 
    jugador1 =pygame.draw.rect(screen,White,(player1XCordenada,player1YCordenada,largoJugardor,anchoJugador))
    
    jugador2 =pygame.draw.rect(screen,White,(player2XCordenada,player2YCordenada,largoJugardor,anchoJugador))
    
    pelota= pygame.draw.circle(screen,White,(pelotaX,pelotay),10)
    
    #coliciones
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelotaXVelocidad *= -1
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

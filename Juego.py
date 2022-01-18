import pygame
import random
import sys

#Definiciones
ANCHO = 800
ALTO = 600
color_verde=(0,0,255)
color_negro=(0,0,0)
color_azul = (0,0,255)

#Personaje del Jugador
pos_juga = [400,400] #lista de valores de x,y del jugador. la x se representa por [0] y la "y" por [1]
tam_juga = 50 #es el tamaño de cada jugador.
centrar_juga = [ANCHO/2, ALTO - tam_juga * 2]



#Enemigos que hay que evitar
tam_enemigo = 50
pos_enemigo = [0,300] #para que salgan desde arriba y centrados de la pantalla



# Aqui empieza la Consola donde se proyecta el juego. 
consola = pygame.display.set_mode((WIDTH,HEIGHT))

game_over = False
clock = pygame.time.Clock()

#Eventos del juego (flechas)
#abajo = keydown, izq = k_left, der = k_right, arriba = k_up. todo en mayúsculas






































#Dibujar enemigo: agregarlo abajo del ciclo else de enemigo
pygame.draw.rect(consola, color_azul, (pos_enemigo[0], pos_enemigo[1], tam_enemigo, tam_enemigo))

#Dibujar jugador
pygame.draw.rect(consola, color_verde, (pos_juga[0], pos_juga[1], tam_juga, tam_juga))

#Dar el tiempo del reloj que necesitamos
clock.tick(30)

#Actualizar el juego
pygame.display.update()

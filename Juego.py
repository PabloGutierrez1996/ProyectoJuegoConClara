
from msilib.schema import Font
import pygame #acceder al comando de pygame
import random
import sys


pygame.init() #inicializa los módulos de pygame
#Definiciones
ANCHO = 800
ALTO = 600
color_rojo=(255,0,0)
color_negro=(0,0,0)
color_azul = (0,255,0)
color_texto = (130,130,130)

#Personaje del Jugador
pos_juga = [400,400] #lista de valores de x,y del jugador. la x se representa por [0] y la "y" por [1]
tam_juga = 50 #es el tamaño de cada jugador
centrar_juga = [ANCHO/2, ALTO - tam_juga * 2]


#Enemigos que hay que evitar
tam_enemigo = 50
pos_enemigo = [0,300] #para que salgan desde arriba y centrados de la pantalla



# Aqui empieza la Consola donde se proyecta el juego. 
consola = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Fin del juego")
clock = pygame.time.Clock()
fuente = pygame.font.Font(None, 36)
game_over = False
#Funciones de colicion con el enemigo
def detectar_colision(pos_juga,pos_enemigo):
	jx = pos_juga[0]
	jy = pos_juga[1]
	ex = pos_enemigo[0]
	ey = pos_enemigo[1]
# posicion del enemigo en relacion con el jugador.
	if (ex >= jx and ex <(jx + tam_juga)) or (jx >= ex and jx < (ex + tam_enemigo)):
		if (ey >= jy and ey <(jy + tam_juga)) or (jy >= ey and jy < (ey + tam_enemigo)):
			return True
		return False

#Eventos del juego (flechas)
#abajo = keydown, izq = k_left, der = k_right, arriba = k_up. todo en mayúsculas
while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit

		if event.type == pygame.KEYDOWN:
			x = pos_juga[0]
			if event.key == pygame.K_LEFT:
				x -= tam_enemigo
			if event.key == pygame.K_RIGHT:
				x += tam_enemigo

			pos_juga[0] = x
	consola.fill(color_negro)

	if pos_enemigo[1] >= 0 and pos_enemigo[1] < ALTO:
		pos_enemigo[1] += 20
	else:
		pos_enemigo[0] = random.randint(0,ANCHO - tam_enemigo)
		pos_enemigo[1] = 0
	#Colisiones
	if detectar_colision(pos_juga,pos_enemigo):
		game_over = True

#Dibujamos el rectangulo con texto de game over
		if game_over:
			texto = fuente.render("FIN DEL JUEGO", True, color_texto)
			texto_rect = texto.get_rect()
			texto_x = consola.get_width()/2 - texto_rect.width / 2
			texto_y = consola.get_height()/2 - texto_rect.height / 2
			consola.blit(texto, [texto_x, texto_y])
		else:
			texto = fuente.render("Haz click para terminar el juego", True, color_texto)
			texto_rect = texto.get_rect()
			texto_x = consola.get_width() / 2 - texto_rect.width / 2
			texto_y = consola.get_height() / 2 - texto_rect.height / 2
			consola.blit(texto, [texto_x, texto_y])

#Dibujar enemigo
	pygame.draw.rect(consola, color_azul,
			(pos_enemigo[0],pos_enemigo[1],
			tam_enemigo, tam_enemigo))
	#Dibujar jugador
	pygame.draw.rect(consola, color_rojo,
			(pos_juga[0],pos_juga[1],
			tam_juga,tam_juga))
	clock.tick(50)
	pygame.display.flip()
pygame.quit()
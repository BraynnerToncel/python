import pygame
import sys
import random

#Const
AN = 800
AL = 600
c_rojo = (255,0,0)
c_negro = (0,0,0)
c_azul = (0,0,255)

#jugador
j_size = 50
j_pos = [AN / 2, AL - j_size * 2]

#Obstáculos
e_size = 50
e_pos = [random.randint(0,AN - e_size),0]
#ventana
ventana = pygame.display.set_mode((AN,AL))

game_over = False
clock = pygame.time.Clock()
#Funciones
def detectar_colision(j_pos,e_pos):
	jx = j_pos[0]
	jy = j_pos[1]
	ex = e_pos[0]
	ey = e_pos[1]

	if (ex >= jx and ex <(jx + j_size)) or (jx >= ex and jx < (ex + e_size)):
		if (ey >= jy and ey <(jy + j_size)) or (jy >= ey and jy < (ey + e_size)):
			return True
		return False   
       
def menu():
    ft = pygame.font.Font(None, 36)
    op1 = ft.render("1. Jugar", True, c_rojo)
    op2 = ft.render("2. Salir", True, c_rojo)
    ventana.blit(op1, (AN // 2 - 50, AL // 2 - 50))
    ventana.blit(op2, (AN // 2 - 50, AL // 2 + 50))
    pygame.display.flip()

def fun_juego():
    global game_over
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                x = j_pos[0]
                if event.key == pygame.K_LEFT:
                    x -= j_size
                if event.key == pygame.K_RIGHT:
                    x += j_size
                j_pos[0] = x
        ventana.fill(c_negro)

        if e_pos[1] >= 0 and e_pos[1] < AL:
            e_pos[1] += 20
        else:
            e_pos[0] = random.randint(0, AN - e_size)
            e_pos[1] = 0

        if detectar_colision(j_pos, e_pos):
            game_over = True

        pygame.draw.rect(ventana, c_azul, (e_pos[0], e_pos[1], e_size, e_size))
        pygame.draw.rect(ventana, c_rojo, (j_pos[0], j_pos[1], j_size, j_size))
        clock.tick(30)
        pygame.display.update()

def main():
    while True:
        menu()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    global game_over
                    game_over = False
                    fun_juego()
                elif event.key == pygame.K_2:
                    sys.exit()

if __name__ == "__main__":
    pygame.init()
    main()




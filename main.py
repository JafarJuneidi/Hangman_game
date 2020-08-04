import pygame 
import math
import random

# setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# button variables
RADIUS = 20
GAP = 15
letters = []  # [[x, y, "A", True], [], ....]
startx = round((WIDTH - (RADIUS*2 + GAP) * 12) / 2) 
starty = 400
A = 65
for i in range(26):
	x = startx + ((RADIUS * 2 + GAP) * (i % 13))
	y = starty + ((i // 13) * (GAP + RADIUS * 2))
	letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont("comicsans", 40)
WORD_FONT = pygame.font.SysFont("comicsans", 60)
TITLE_FONT = pygame.font.SysFont("comicsans", 70)

# load images
images = []
for i in range(7):
	image = pygame.image.load("images/hangman" + str(i) + ".png")
	images.append(image)

# game variables
hangman_status = 0
words = ["HELLO", "PYTHON", "PYGAME", "PICKAXE", "DIAMOND", "DEVELOPER", "JAFAR", "GERALT", "MINECRAFT", "STEVE", "PASTA", "PHONE"]
word = random.choice(words)
guessed = []

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)
LIGHT_GREEN = (0, 255, 0)

def draw():
	win.fill(WHITE)

	#draw title
	text = TITLE_FONT.render("DEVELOPER HANGMAN", 1, BLACK)
	win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

	#draw word
	display_word = ""
	for letter in word:
		if letter in guessed:
			display_word += letter + " "
		else:
			display_word += "_ "
	text = WORD_FONT.render(display_word, 1, BLACK)
	win.blit(text, (400, 200))

	#draw buttons
	for letter in letters:
		x, y, ltr, visible = letter
		if visible:
			pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
			text = LETTER_FONT.render(ltr, 1, BLUE)
			win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

	win.blit(images[hangman_status], (150, 100))
	pygame.display.update()

def display_message(message):
	pygame.time.delay(1000)
	win.fill(WHITE)
	text = WORD_FONT.render(message, 1, BLACK)
	win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))		
	pygame.display.update()
	pygame.time.delay(3000)

def menu():
	running = True

	win.fill(WHITE)
	
	title = TITLE_FONT.render("Hangman's Game", 1, BLACK)
	win.blit(title, (WIDTH/2 - title.get_width()/2, 100))

	RECT_HEIGHT = 70
	RECT_WIDTH = 180
	rect_x = WIDTH/2 - RECT_WIDTH/2
	rect_y = HEIGHT/2 - RECT_HEIGHT/2 + 80
	
	text = TITLE_FONT.render("PLAY", 1, BLACK)
	text_x = rect_x + RECT_WIDTH/2 - text.get_width()/2
	text_y = rect_y + RECT_HEIGHT/2 - text.get_height()/2
	

	while running:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			
			if event.type == pygame.MOUSEBUTTONDOWN:
				m_x, m_y = pygame.mouse.get_pos()
				if rect_x + RECT_WIDTH > m_x > rect_x and rect_y + RECT_HEIGHT > m_y > rect_y:
					return True

			mouse = pygame.mouse.get_pos()
			if rect_x + RECT_WIDTH > mouse[0] > rect_x and rect_y + RECT_HEIGHT > mouse[1] > rect_y:
				pygame.draw.rect(win, LIGHT_GREEN, (rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT))
				win.blit(text, (text_x, text_y))
			else:
				pygame.draw.rect(win, GREEN, (rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT))
				win.blit(text, (text_x, text_y))
		
		pygame.display.update()
		

def main():
	global hangman_status
	# setup game loop
	FPS = 60
	clock = pygame.time.Clock()
	run = True 
	
	while run:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				m_x, m_y = pygame.mouse.get_pos()
				for letter in letters:
					x, y, ltr, visible = letter
					if visible:
						dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
						if dis < RADIUS:
							letter[3] = False
							guessed.append(ltr)
							if ltr not in word:
								hangman_status += 1

		draw()

		won = True
		for letter in word:
			if letter not in guessed:
				won = False
				break

		if won:
			display_message("You WON!")
			break

		if hangman_status == 6:
			display_message("You LOST!")
			break

if menu():
	main()

pygame.quit()	
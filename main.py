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
startx = round((WIDTH - (RADIUS*2 + GAP) * 12) / 2) 
starty = 400
A = 65


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
words = ["HELLO", "PYTHON", "PYGAME", "PICKAXE", "DIAMOND", "DEVELOPER", "JAFAR", "GERALT", "MINECRAFT", "STEVE", "PASTA", "PHONE"]
def set_game_variables():
	hangman_status = 0
	word = random.choice(words)
	guessed = []
	letters = []  # [[x, y, "A", True], [], ....]
	for i in range(26):
		x = startx + ((RADIUS * 2 + GAP) * (i % 13))
		y = starty + ((i // 13) * (GAP + RADIUS * 2))
		letters.append([x, y, chr(A + i), True])

	return word, guessed, hangman_status, letters

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)
LIGHT_GREEN = (0, 255, 0)
LIGHT_BLUE = (0, 0, 255)

def draw(word, guessed, hangman_status, letters):
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
	win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT//3 - text.get_height()/2))		
	pygame.display.update()
	pygame.time.delay(500)

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
		

def play_again(message):
	display_message(message)
	global run_again 
	running = True

	RECT_HEIGHT = 60
	RECT_WIDTH = 300
	rect_x = WIDTH/2 - RECT_WIDTH/2
	rect_y = HEIGHT/2 - RECT_HEIGHT/2 + 80
	
	text = TITLE_FONT.render("PLAY AGAIN", 1, BLACK)
	text_x = rect_x + RECT_WIDTH/2 - text.get_width()/2
	text_y = rect_y + RECT_HEIGHT/2 - text.get_height()/2
	

	EXIT_HEIGHT = 60
	EXIT_WIDTH = 150
	exit_x = WIDTH/2 - EXIT_WIDTH/2
	exit_y = HEIGHT/2 - EXIT_HEIGHT/2 + 170
	
	exit = TITLE_FONT.render("EXIT", 1, BLACK)
	exit_text_x = exit_x + EXIT_WIDTH/2 - exit.get_width()/2
	exit_text_y = exit_y + EXIT_HEIGHT/2 - exit.get_height()/2

	while running:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			
			if event.type == pygame.MOUSEBUTTONDOWN:
				m_x, m_y = pygame.mouse.get_pos()
				if rect_x + RECT_WIDTH > m_x > rect_x and rect_y + RECT_HEIGHT > m_y > rect_y:
					run_again = True
					running = False

			mouse = pygame.mouse.get_pos()
			if rect_x + RECT_WIDTH > mouse[0] > rect_x and rect_y + RECT_HEIGHT > mouse[1] > rect_y:
				pygame.draw.rect(win, LIGHT_GREEN, (rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT))
				win.blit(text, (text_x, text_y))
			else:
				pygame.draw.rect(win, GREEN, (rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT))
				win.blit(text, (text_x, text_y))


			if event.type == pygame.MOUSEBUTTONDOWN:
				m_x, m_y = pygame.mouse.get_pos()
				if exit_x + EXIT_WIDTH > m_x > exit_x and exit_y + EXIT_HEIGHT > m_y > exit_y:
					pygame.time.delay(500)
					pygame.quit()

			if exit_x + EXIT_WIDTH > mouse[0] > exit_x and exit_y + EXIT_HEIGHT > mouse[1] > exit_y:
				pygame.draw.rect(win, LIGHT_BLUE, (exit_x, exit_y, EXIT_WIDTH, EXIT_HEIGHT))
				win.blit(exit, (exit_text_x, exit_text_y))
			else:
				pygame.draw.rect(win, BLUE, (exit_x, exit_y, EXIT_WIDTH, EXIT_HEIGHT))
				win.blit(exit, (exit_text_x, exit_text_y))
		
		pygame.display.update()


def main():
	word, guessed, hangman_status, letters = set_game_variables()
	# setup game loop
	FPS = 60
	clock = pygame.time.Clock()
	run = True 
	
	while run:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
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

		draw(word, guessed, hangman_status, letters)

		won = True
		for letter in word:
			if letter not in guessed:
				won = False
				break

		if won:
			play_again("You WON!")
			break

		if hangman_status == 6:
			play_again("You LOST!")
			break

if menu():
	main()

while run_again:
	main()

pygame.quit()	
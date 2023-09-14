import pygame
import random
import math
#setup 
pygame.init()
display = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Hang Cecil!")

#load images
images= []
for i in range(8):
    image= pygame.image.load("cecilhang"+str(i)+".png")
    images.append(image)

#game variablles
hangman_status = 0
words = ["POMONA", "CLAREMONT", "COLLEGE", "CALIFORNIA", "LIBERALARTS", "CONSORTIUM", "5CS", "CLAREMONTCOLLEGES", "ACADEMIC", "CAMPUS", "STUDENT", "DIVERSITY", "COMMUNITY", "RESIDENTIALHALLS", "SAGEHEN", "ATHLETICS", "MCC", "MUDD", "SCRIPPS", "PITZER", "OLDENBORG", "MARSTONQUAD", "VILLAGE", "MUSEUM", "FARM", "OUTDOORS", "MOTLEY", "CLASSROOMS", "ALUMNI", "FIELDSTATION", "ROSEGARDEN", "LIBRARY", "LABS", "CDO", "CENTERS", "SAGEHENS", "ABROAD", "WILDERNESSPARK", "OXYCHEM", "BLAISDELL", "STUDIOART", "THEATER", "HUMANITIES", "MUN", "GOVERNMENT", "SUSTAINABILITY", "EAP", "ACAPELLA", "WALKERBEACH", "HAHN"]
word = random.choice(words)
guessed= []
#buttons
radius= 16
gap = 13
letters=[] 
startx= 380
starty= 350
A=65
#math for spacing of letter button
for i in range(26):
    x = startx + gap*2 + ((radius*2 + gap) * (i%13))
    y = starty + ((i//13)*(gap+radius*2))
    letters.append([x, y, chr(A+i), True])
#drawing background and hanging
def draw():
    display.fill((255,255,255))
    display.blit(images[hangman_status],(30,30))
    button_font = pygame.font.SysFont('comicsans', 22)
    word_font = pygame.font.SysFont('comicsans', 40)
    #draw word
    display_word =""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = word_font.render(display_word, 1, (0,0,0))
    display.blit(text, (550, 200))
    #draw title
    title= pygame.font.SysFont('comicsans', 80).render("Hangbird :)",1, (0,191,255))
    display.blit(title, (400,50))
    #draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(display, (0,191,255), (x,y), radius, 3)
            text = button_font.render(ltr, 1, (0,0,0))
            display.blit(text, (x-radius/2, y-radius))
    pygame.display.update()

#game loop
FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        #if press x, quit
        if event.type == pygame.QUIT:
            run = False
        #mouse click to render its position
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my= pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                distance= math.sqrt((x-mx)**2+(y-my)**2)
                if visible:
                    if distance < radius:
                        letter[3] =False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
        draw()
    won =True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    word_font = pygame.font.SysFont('comicsans', 40)
    if won:
        pygame.time.delay(1000)
        display.fill((255,255,0))
        text = word_font.render("OMG YOU WON, SO SAGEHEN!!!",1, (0,0,0))
        display.blit(text,(250,250))
        pygame.display.update()
        pygame.time.delay(5000)
        break
    if hangman_status == 7:
        pygame.time.delay(3000)
        # display.fill((255,255,0))
        # text = word_font.render("YOU SUCK!!!",1, (0,0,0))
        # display.blit(text,(400,250))
        # pygame.display.update()
        # pygame.time.delay(5000)
        break

pygame.quit()
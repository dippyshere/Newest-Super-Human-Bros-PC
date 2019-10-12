#import items
import pygame, sys, time, os, random, csv
from datetime import timedelta
#init it so it works
pygame.init()
pygame.mixer.init(48000, -16, 2, 1024)

#make window
X = 1280
Y = 720
win = pygame.display.set_mode((X,Y))
#icon jah
icon = pygame.image.load('pictures/icon.png')
pygame.display.set_icon(icon)
#name it
pygame.display.set_caption("Newest Super Human Bros PC")

#loading beacuse it takes a while for those lists down there
loadimg = pygame.image.load('pictures/loading.png')
win.blit(loadimg, (0,0))
pygame.display.update()

#sounds
jumpsnd = pygame.mixer.Sound('audio/jump.wav')
lvlstrt = pygame.mixer.Sound('audio/startlvl.wav')  
sta = pygame.mixer.Sound('audio/step1.wav')
stb = pygame.mixer.Sound('audio/step2.wav')
coin_snd = pygame.mixer.Sound('audio/coin.wav')
tramp = pygame.mixer.Sound('audio/trampoline.wav')
oneup_jingle = pygame.mixer.Sound('audio/oneup.wav')
star = pygame.mixer.Sound('audio/starget.wav')
death = pygame.mixer.Sound('audio/death.wav')
hurryup = pygame.mixer.Sound('audio/hurry up.wav')

#sprites
#walk right list
walkRight = [pygame.image.load('pictures/R1.png'), pygame.image.load('pictures/R2.png'), pygame.image.load('pictures/R3.png'), pygame.image.load('pictures/R4.png'), pygame.image.load('pictures/R5.png'), pygame.image.load('pictures/R6.png'), pygame.image.load('pictures/R7.png'), pygame.image.load('pictures/R8.png'), pygame.image.load('pictures/R9.png')]
#walk left list
walkLeft = [pygame.image.load('pictures/L1.png'), pygame.image.load('pictures/L2.png'), pygame.image.load('pictures/L3.png'), pygame.image.load('pictures/L4.png'), pygame.image.load('pictures/L5.png'), pygame.image.load('pictures/L6.png'), pygame.image.load('pictures/L7.png'), pygame.image.load('pictures/L8.png'), pygame.image.load('pictures/L9.png')]
#background picture
bg = pygame.image.load('pictures/bgnew-min.png')
#ground picture
grnd = pygame.image.load('pictures/ground.png')
#fall
fallimg = pygame.image.load('pictures/fall.png')
#fall left
fallimgl = pygame.image.load('pictures/falll.png')
#idle
char = pygame.image.load('pictures/standing.png')
#idle left
charl = pygame.image.load('pictures/leftidle.png')
#jump
jump = pygame.image.load('pictures/jump.png')
#jump left
jumpl = pygame.image.load('pictures/jumpl.png')
#logo
logo = pygame.image.load('pictures/logo.png')
#back button
back = pygame.image.load('pictures/previous.png')
#coin
coin1 = pygame.image.load('pictures/coin.png')
#tramp
tramp_omg = pygame.image.load('pictures/Toranporin.png')
#star
star1 = pygame.image.load('pictures/star.png')
#1up
mushy = pygame.image.load('pictures/1upmushy.png')
#cutscene test
cutscenetest = pygame.image.load('test/Kattoshintesuto.png')
#clock
tokei = pygame.image.load('pictures/clock.png')
#cutscene
cutscene_img = [pygame.image.load('animation/frame1.png'), pygame.image.load('animation/frame2.png'), pygame.image.load('animation/frame3.png'), pygame.image.load('animation/frame4.png'), pygame.image.load('animation/frame5.png'), pygame.image.load('animation/frame6.png'), pygame.image.load('animation/frame7.png'), pygame.image.load('animation/frame8.png'), pygame.image.load('animation/frame9.png'), pygame.image.load('animation/frame10.png'), pygame.image.load('animation/frame11.png'), pygame.image.load('animation/frame12.png'), pygame.image.load('animation/frame13.png'), pygame.image.load('animation/frame14.png'), pygame.image.load('animation/frame15.png'), pygame.image.load('animation/frame16.png'), pygame.image.load('animation/frame17.png'), pygame.image.load('animation/frame18.png'), pygame.image.load('animation/frame19.png'), pygame.image.load('animation/frame20.png'), pygame.image.load('animation/frame21.png'), pygame.image.load('animation/frame22.png'), pygame.image.load('animation/frame23.png'), pygame.image.load('animation/frame24.png'), pygame.image.load('animation/frame25.png'), pygame.image.load('animation/frame26.png'), pygame.image.load('animation/frame27.png'), pygame.image.load('animation/frame28.png'), pygame.image.load('animation/frame29.png'), pygame.image.load('animation/frame30.png'), pygame.image.load('animation/frame31.png'), pygame.image.load('animation/frame32.png'), pygame.image.load('animation/frame33.png'), pygame.image.load('animation/frame34.png'), pygame.image.load('animation/frame35.png'), pygame.image.load('animation/frame36.png'), pygame.image.load('animation/frame37.png'), pygame.image.load('animation/frame38.png'), pygame.image.load('animation/frame39.png'), pygame.image.load('animation/frame40.png'), pygame.image.load('animation/frame41.png'), pygame.image.load('animation/frame42.png'), pygame.image.load('animation/frame43.png'), pygame.image.load('animation/frame44.png'), pygame.image.load('animation/frame45.png'), pygame.image.load('animation/frame46.png'), pygame.image.load('animation/frame47.png'), pygame.image.load('animation/frame48.png'), pygame.image.load('animation/frame49.png'), pygame.image.load('animation/frame50.png'), pygame.image.load('animation/frame51.png'), pygame.image.load('animation/frame52.png'), pygame.image.load('animation/frame53.png'), pygame.image.load('animation/frame54.png'), pygame.image.load('animation/frame55.png'), pygame.image.load('animation/frame56.png'), pygame.image.load('animation/frame57.png'), pygame.image.load('animation/frame58.png'), pygame.image.load('animation/frame59.png'), pygame.image.load('animation/frame60.png'), pygame.image.load('animation/frame61.png'), pygame.image.load('animation/frame62.png'), pygame.image.load('animation/frame63.png')]
#secret
alphatesta = pygame.image.load('test/alpha.png')
alphatestn = pygame.image.load('test/tile.png')
bg2olv = pygame.image.load('pictures/bglvl2overlay-min.png')
bg3olv = pygame.image.load('pictures/bglvl3overlay-min.png')
bg2 = pygame.image.load('pictures/bglvl2-min.png')
bg1olv = pygame.image.load('pictures/bgoverlay-min.png')
bg4olv = pygame.image.load('pictures/bglvl4overlay-min.png')
secret3 = pygame.image.load('pictures/hidden2.png')
secret3a = pygame.image.load('pictures/hidden2 alpha.png')
secret4 = pygame.image.load('pictures/hidden3.png')
secret4a = pygame.image.load('pictures/hidden3 alpha.png')

#make images scale correctly (resizing lol graphics.py cant do that)
logo_scaled = pygame.transform.scale(logo, (680, 225))
back_scaled = pygame.transform.scale(back, (50,50))
coin_img = pygame.transform.scale(coin1, (30, 32))
coin_hud = pygame.transform.scale(coin1, (32, 32))
tramp_img = pygame.transform.scale(tramp_omg, (32, 30))
star_ig = pygame.transform.scale(star1, (32, 32))
oneup = pygame.transform.scale(mushy, (32,32))
clockimg = pygame.transform.scale(tokei, (32,32))
alphatest = pygame.transform.scale(alphatesta, (107,32))
alphatest43 = pygame.transform.scale(alphatesta, (75,32))
alphatestnon = pygame.transform.scale(alphatestn, (107, 32))
alphatestnon43 = pygame.transform.scale(alphatestn, (75, 32))

#for fonts
font = pygame.font.Font(None, 30)

#for frame capping
clock = pygame.time.Clock()

#testing
fps = clock.get_fps()

#colours
white = (255, 255, 255) 
green = (0, 200, 0) 
blue = (0, 160, 220)
black = (0, 0, 0)
red = (200,0,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0,255,255)
purple = (255,0,255)

#multiplayer
luigi2 = False

#variables
coin1_draw = True
coin2_draw = True
coin3_draw = True
coin_counter = 0
oneup_cntr = 5
oneup_draw1 = True
star_cntr = 0
star1_get = False
star1_get_pause = False
secret = False
secret3_draw = False
secret4_draw = False
oneup_draw2 = True
hudclock = 200
nextlvl = 1
score = 00000000
timetocomplete = 0
pygame.display.set_icon(icon)

#game save testing
with open('scoredata.dataconfig','r') as data:
    csv_reader = csv.reader(data)
    for row in csv_reader:
        lb = row
print(lb)

#checking cache
gcache = globals()
cache = str(sys.getsizeof(gcache))
print(cache)

#player class
class player(object):
    def __init__(self, x, y, width, height):
        #defining character variables
        #where to draw the x of the character
        self.x = x
        #where to draw the y of the character
        self.y = y
        #width of the character
        self.width = width
        #height of the character
        self.height = height
        #how many pixels it moves every frame
        self.vel = 5
        #is jump
        self.isJump = False
        #controls speed during jump
        self.jumpCount = 10
        #is facing left
        self.left = False
        #is facing right
        self.right = False
        #animation timer
        self.walkCount = 0
        #direction facing
        self.idle_type = True
        #fall test
        self.fall = 0
    #for drawing animations
    def draw(self,win):
        #if the timer plus 1 is greater than or equal to 27 then
        if self.walkCount + 1 >= 27:
            #set to 0 to repeat anim
            self.walkCount = 0
        #else if jump state is true
        elif self.isJump == True:
            #jump animation
            #if idle type is true then face right
            if self.idle_type == True and self.jumpCount <= -1:
                win.blit(fallimg, (self.x, self.y))
            elif self.idle_type == True and self.jumpCount >= 0:
                win.blit(jump, (self.x, self.y))
            #else if it is false then face left
            elif self.idle_type == False and self.jumpCount <= -1:
                win.blit(fallimgl, (self.x, self.y))
            elif self.idle_type == False and self.jumpCount >= 0:
                win.blit(jumpl, (self.x, self.y))
            else:
                if self.idle_type == True:
                    win.blit(char, (self.x, self.y))
                elif self.idle_type == False:
                    win.blit(charl, (self.x, self.y))
                else:
                    win.blit(char, (self.x, self.y))
        #else if left variable is true
        elif self.left:
            #make idle animation face left
            self.idle_type = False
            #walk left animation
            #draw the walk left list with [number//3(// means )](for
            #list number), (where to draw x, where to draw y))
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            #add one to walk count
            self.walkCount += 1
            sta.play()
        #else if right variable is true
        elif self.right:
            #make idle face right
            self.idle_type = True
            #dito
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            #dito
            self.walkCount += 1
            stb.play()
        #else if idle type is true (face right)
        elif self.idle_type == True:
            #face right
            #where to draw.draw fuction(sprite to draw, (where x, where y))
            win.blit(char, (self.x, self.y))
        #else if idle is falce (face left)
        elif self.idle_type == False:
            #draw left facing character
            win.blit(charl, (self.x, self.y))
        #else just face right as default
        else:
            #draw facing right
            win.blit(char, (self.x, self.y))
def cutscene():
    global nextlvl
    star1_get = False
    star1_get_pause = False
    nextlvl += 1
    for i in range(1, 63):
        win.blit(cutscene_img[i], (0,0))
        pygame.display.update()
        pygame.time.delay(45)
    pygame.time.delay(1500)
    fade_out(1280,720)
    if nextlvl == 1:
        game_loop_1p()
        #score_tally()
    if nextlvl == 2:
        game_lvl2()
    if nextlvl == 3:
        game_lvl3()
    if nextlvl == 4:
        game_lvl4()
    if nextlvl == 5:
        score_tally()
#draw fuction
def redrawGameWindow():
    timetocomplete2 = timetocomplete/30
    time_yes = str(timedelta(seconds=timetocomplete2))
    global secret
    #global hitbox
    #global coin
    #make this variable global so it exists outside the function
    global luigi2
    #draw the background
    win.blit(bg, (0,0))
    win.blit(grnd, (0, 659))
    win.blit(tramp_img, (150,655))
    win.blit(bg1olv, (0,0))
    if oneup_draw2 == True:
        win.blit(oneup, (528, 655))
    if oneup_draw1 == True:
        win.blit(oneup, (225, 153))
    #uwu for some depth do drawing before this comment for behind mario, and do drawing after for infront of mario
    #draw our character
    #if luigi 2 is true (if 2 player is called)
    if luigi2 == True:
        #draw both characters
        luigi.draw(win)
        mario.draw(win)
    #else it must not be true and therefore not called for two player
    #so just draw one player
    else:
        #draw only one character
        mario.draw(win)
    if (mario.x+mario.width) >= 400 and (mario.x+mario.width) <=688 and mario.y >= 655-16:
        secret = True
    else:
        secret = False
    if coin1_draw == True:
        win.blit(coin_img, (175,153))
    if coin2_draw == True:
        win.blit(coin_img, (275,153))
    if secret == True:
        win.blit(alphatest, (400, 655))
        win.blit(alphatest, (506, 655))
        win.blit(alphatest43, (613, 655))
    if secret == False:
        win.blit(alphatestnon, (400, 655))
        win.blit(alphatestnon, (506, 655))
        win.blit(alphatestnon43, (613, 655))
    win.blit(star_ig, (1150, 525))
    win.blit(oneup, (10, 52))
    win.blit(coin_hud, (10,10))
    win.blit(star_ig, (1167, 10))
    win.blit(clockimg, (1157, 52))
    smallText = pygame.font.Font("fonts/Mario64.ttf",40)
    textSurf, textRect = text_objects(" x  " + str(coin_counter), smallText)
    textRect.center = (81, (10+(24/2)) )
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects(" x  " + str(oneup_cntr), smallText)
    textRect.center = (81, (52+(24/2)) )
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects(" x  " + str(star_cntr), smallText)
    textRect.center = (1238, (10+(24/2)) )
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects(str(hudclock), smallText)
    textRect.center = (1238, (52+(24/2)) )
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects("Score  " + str(score), smallText)
    textRect.center = (860, 43)
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects("Level  " + str(nextlvl), smallText)
    textRect.center = (420, 43)
    win.blit(textSurf, textRect)
    font = pygame.font.Font("fonts/Mario64.ttf",40)
    text = font.render("Time:  " + time_yes,True,black)
    win.blit(text, (975,82))
    #textSurf, textRect = text_objects("Time:  " + time_yes, smallText)
    #textRect.center = (1280//2, 360)
    #win.blit(textSurf, textRect)
    #lol pretty obvious what this is (update display whaaaaa omg so smart)
    pygame.display.update()

def redrawGameWindow2():
    timetocomplete2 = timetocomplete/30
    time_yes = str(timedelta(seconds=timetocomplete2))
    win.blit(bg2, (0,0))
    win.blit(bg2olv, (0,0))
    #uwu for some depth do drawing before this comment for behind mario, and do drawing after for infront of mario
    #draw our character
    #if luigi 2 is true (if 2 player is called)
    if luigi2 == True:
        #draw both characters
        luigi.draw(win)
        mario.draw(win)
    #else it must not be true and therefore not called for two player
    #so just draw one player
    else:
        #draw only one character
        mario.draw(win)
    win.blit(star_ig, (1150, 260))
    win.blit(oneup, (10, 52))
    win.blit(coin_hud, (10,10))
    win.blit(star_ig, (1167, 10))
    win.blit(clockimg, (1157, 52))
    smallText = pygame.font.Font("fonts/Mario64.ttf",40)
    textSurf, textRect = text_objects(" x  " + str(coin_counter), smallText)
    textRect.center = (81, (10+(24/2)) )
    win.blit(textSurf, textRect)
    smallText = pygame.font.Font("fonts/Mario64.ttf",40)
    textSurf, textRect = text_objects(" x  " + str(oneup_cntr), smallText)
    textRect.center = (81, (52+(24/2)) )
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects(" x  " + str(star_cntr), smallText)
    textRect.center = (1238, (10+(24/2)) )
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects(str(hudclock), smallText)
    textRect.center = (1238, (52+(24/2)) )
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects("Score  " + str(score), smallText)
    textRect.center = (860, 43)
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects("Level  " + str(nextlvl), smallText)
    textRect.center = (420, 43)
    font = pygame.font.Font("fonts/Mario64.ttf",40)
    text = font.render("Time:  " + time_yes,True,black)
    win.blit(text, (975,82))
    win.blit(textSurf, textRect)
    pygame.display.update()

def redrawGameWindow3():
    timetocomplete2 = timetocomplete/30
    time_yes = str(timedelta(seconds=timetocomplete2))
    win.blit(bg, (0,0))
    win.blit(grnd, (0, 659))
    win.blit(bg3olv, (0,0))
    win.blit(tramp_img, (150,655))
    win.blit(tramp_img, (384, 320))
    win.blit(tramp_img, (700, 320))
    #uwu for some depth do drawing before this comment for behind mario, and do drawing after for infront of mario
    #draw our character
    #if luigi 2 is true (if 2 player is called)
    if luigi2 == True:
        #draw both characters
        luigi.draw(win)
        mario.draw(win)
    #else it must not be true and therefore not called for two player
    #so just draw one player
    else:
        #draw only one character
        mario.draw(win)
    win.blit(star_ig, (1150, 500))
    win.blit(oneup, (10, 52))
    win.blit(coin_hud, (10,10))
    win.blit(star_ig, (1167, 10))
    win.blit(clockimg, (1157, 52))
    smallText = pygame.font.Font("fonts/Mario64.ttf",40)
    textSurf, textRect = text_objects(" x  " + str(coin_counter), smallText)
    textRect.center = (81, (10+(24/2)) )
    win.blit(textSurf, textRect)
    smallText = pygame.font.Font("fonts/Mario64.ttf",40)
    textSurf, textRect = text_objects(" x  " + str(oneup_cntr), smallText)
    textRect.center = (81, (52+(24/2)) )
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects(" x  " + str(star_cntr), smallText)
    textRect.center = (1238, (10+(24/2)) )
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects(str(hudclock), smallText)
    textRect.center = (1238, (52+(24/2)) )
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects("Score  " + str(score), smallText)
    textRect.center = (860, 43)
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects("Level  " + str(nextlvl), smallText)
    textRect.center = (420, 43)
    win.blit(textSurf, textRect)
    font = pygame.font.Font("fonts/Mario64.ttf",40)
    text = font.render("Time:  " + time_yes,True,black)
    win.blit(text, (975,82))
    pygame.display.update()

def redrawGameWindow4():
    timetocomplete2 = timetocomplete/30
    time_yes = str(timedelta(seconds=timetocomplete2))
    win.blit(bg, (0,0))
    win.blit(bg4olv, (0,0))
    win.blit(grnd, (0, 659))
    #uwu for some depth do drawing before this comment for behind mario, and do drawing after for infront of mario
    #draw our character
    #if luigi 2 is true (if 2 player is called)
    if luigi2 == True:
        #draw both characters
        luigi.draw(win)
        mario.draw(win)
    #else it must not be true and therefore not called for two player
    #so just draw one player
    else:
        #draw only one character
        mario.draw(win)
    if coin3_draw == True:
        win.blit(coin_img, (496,462))
    if secret3_draw == False:
        win.blit(secret3, (469, 442))
    if secret4_draw == False:
        win.blit(secret4, (659, 89))
    if secret3_draw == True:
        win.blit(secret3a, (469, 442))
    if secret4_draw == True:
        win.blit(secret4a, (659, 89))
    win.blit(star_ig, (1150, 500))
    win.blit(oneup, (10, 52))
    win.blit(coin_hud, (10,10))
    win.blit(star_ig, (1117, 10))
    win.blit(clockimg, (1117, 52))
    smallText = pygame.font.Font("fonts/Mario64.ttf",40)
    textSurf, textRect = text_objects(" x  " + str(coin_counter), smallText)
    textRect.center = (81, (10+(24/2)) )
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects(" x  " + str(oneup_cntr), smallText)
    textRect.center = (81, (52+(24/2)) )
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects(" x  " + str(star_cntr), smallText)
    textRect.center = (1188, (10+(24/2)) )
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects(str(hudclock), smallText)
    textRect.center = (1188, (52+(24/2)) )
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects("Score  " + str(score), smallText)
    textRect.center = (860, 43)
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects("Level  " + str(nextlvl), smallText)
    textRect.center = (420, 43)
    win.blit(textSurf, textRect)
    font = pygame.font.Font("fonts/Mario64.ttf",40)
    text = font.render("Time:  " + time_yes,True,black)
    win.blit(text, (975,82))
    pygame.display.update()

#define what mario and luigi is when we call the class
#variable name = class name(x, y, width, height)
mario = player(55, 655, 28, 32)
#for 2nd player
luigi = player(97, 655, 28, 32)

#define text_objects function to make text drawing cleaner
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#epic fade transition
def fade_out(width, height):
    #create a surface
    black1 = pygame.Surface((width, height))
    #make it black
    black1.fill((0,0,0))
    #run over this 100 times
    for alpha in range(0, 100):
        #change the alpha (transperancy) to the itteration in the loop (0 - 100)
        black1.set_alpha(alpha)
        #draw the surface
        win.blit(black1, (0,0))
        #update the display
        pygame.display.update()
        #delay the running of the next itteration until 10 ms passes
        pygame.time.delay(10)
def fade_white(width, height):
    #dito
    white1 = pygame.Surface((width, height))
    white1.fill((255,255,255))
    for alpha in range(0, 50):
        white1.set_alpha(alpha)
        win.blit(white1, (0,0))
        pygame.display.update()
        pygame.time.delay(10)
#nearly less than one second of my name at begining of running program
def name():
    #make cursor invisible
    pygame.mouse.set_visible(False)
    #again cache printing
    pygame.display.set_icon(icon)
    gcache = globals()
    cache = str(sys.getsizeof(gcache))
    print(cache)
    #see if this was called or not
    print('name()')
    #i dont know why this is here it only runs once lol just incase the program is killed just before it passes over this loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gcache = globals()
            cache = str(sys.getsizeof(gcache))
            print('Final Cache: ' + cache)
            pygame.quit()
            sys.exit()
            quit()
    win.fill(black)
    #make name
    largeText = pygame.font.Font('fonts/SuperMario256.ttf',90)
    TextSurf, TextRect = text_objects("Alex Hanson", largeText)
    TextRect.center = ((X/2),(Y/2))
    #draw it
    win.blit(TextSurf, TextRect)
    #update the screen
    pygame.display.update()
    fade_white(1280,720)
    win.fill(white)
    win.blit(TextSurf, TextRect)
    pygame.display.update()
    #print cache again
    print('Global cache: ' + cache)
    #waits one second before moving on
    pygame.time.wait(1000)
    #calls our next function
    game_intro()

#define the fuction that is called for the menu
def game_intro():
    #for when going back into the fuction, avoid unintended button presses
    pygame.time.wait(200)
    pygame.mouse.set_visible(True)
    #just to see if this was called or not
    print('game_intro()')
    #just to see cache
    gcache = globals()
    cache = str(sys.getsizeof(gcache))
    print('Global cache: ' + cache)
    #once again make global so it exists outside this function
    global luigi2
    #print its value for debugging
    print(luigi2)
    #play our music
    music = pygame.mixer.music.load('audio/sm64fs.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.6)
    #only explaining once, make this variable so we can make it false later
    #and it takes up more lines of code
    menu = True
    #and now our main loop
    while menu:
        #for the amount of events that exists in pygame event reciever
        for event in pygame.event.get():
            #if any of those equal quit (only called when application close is
            #announced
            if event.type == pygame.QUIT:
                #print debuging info
                print('Final Cache: ' + cache)
                #uninitialise pygame and close it
                pygame.quit()
                #exit with style via sys exit
                sys.exit()
                #just noob exit that wont be called ever
                #infact just to prove that:
                print('you arent meant to see this message')
                quit()
        #make the background
        win.fill(white)
        #define what lage text means
        largeText = pygame.font.Font('fonts/SuperMario256.ttf',70)
        #make text
        TextSurf, TextRect = text_objects("Newest Super Mario Bros PC", largeText)
        #where to place its centre
        TextRect.center = ((X/2),(Y/8))
        #draw it on the screen
        #win.blit(TextSurf, TextRect)
        win.blit(logo_scaled, (300, 5))
        #make mouse variable and get its position
        mouse = pygame.mouse.get_pos()
        #make click variable and get click location
        click = pygame.mouse.get_pressed()
        #if the left mouse click is between the points that make the rectange
        #make it fancily become brighter color
        if 450+350 > mouse[0] > 450 and 240+80 > mouse[1] > 240:
            #draw bright one
            pygame.draw.rect(win, bright_green,(450,240,350,80))
            #if the mouse left clicks on it
            if click[0]:
                #stop music
                pygame.mixer.music.stop()
                #play start sound
                lvlstrt.play()
                #make cursor invisible
                pygame.mouse.set_visible(False)
                #call fade function
                fade_out(1280,720)
                #wait a bit
                pygame.time.wait(100)
                #call the one player function
                #game_loop_1p()
                game_loop_1p()
        #else if it is over the uit button
        elif 450+350 > mouse[0] > 450 and 480+80 > mouse[1] > 480:
            #dito
            pygame.draw.rect(win, bright_red,(450,480,350,80))
            pygame.draw.rect(win, green,(450,240,350,80))
            if click[0]:
                #call quits
                quit_a()
        #else if over instructions button
        elif 980+250 > mouse[0] > 980 and 610+60 > mouse[1] > 610:
            #dito
            pygame.draw.rect(win, bright_blue,(980,610,250,60))
            pygame.draw.rect(win, green,(450,240,350,80))
            if click[0]:
                #call instructions
                instructions()
        #else if over 2 player button
        elif 980+250 > mouse[0] > 980 and 510+60 > mouse[1] > 510:
            #ditto
            pygame.draw.rect(win, bright_blue,(980,510,250,60))
            pygame.draw.rect(win, green,(450,240,350,80))
            if click[0]:
                #make luigi2 true which means it will draw luigi
                luigi2 = True
                #stop main menu music
                pygame.mixer.music.stop()
                #play start sound effect
                lvlstrt.play()
                #make cursor invisible
                pygame.mouse.set_visible(False)
                #call our fade out function
                fade_out(1280,720)
                #call game 2p function
                game_loop_2p()
        #else if over nut button
        elif 50+250 > mouse[0] > 50 and 610+60 > mouse[1] > 610:
            #dito
            pygame.draw.rect(win, bright_blue,(50,610,250,60))
            pygame.draw.rect(win, green,(450,240,350,80))
            if click[0]:
                pygame.mixer.music.pause()
                #play nut sound
                nut = pygame.mixer.Sound('audio/soundnut.wav')
                print('nut')
                nut.play()
                pygame.time.wait(500)
                pygame.mixer.music.play(-1)
        #else if over settings button
        elif 50+250 > mouse[0] > 50 and 510+60 > mouse[1] > 510:
            pygame.draw.rect(win, green,(450,240,350,80))
            #dito
            if click[0]:
                settings()
        else:
            #start button
            pygame.draw.rect(win, green,(450,240,350,80))
        #exit button
        pygame.draw.rect(win, red,(450,480,350,80))
        #one of the blue buttons
        pygame.draw.rect(win, blue,(980,610,250,60))
        #dito
        pygame.draw.rect(win, blue,(980,510,250,60))
        #dito
        pygame.draw.rect(win, blue,(50,610,250,60))
        #dito
        pygame.draw.rect(win, blue,(50,510,250,60))
        #button texts
        smallText = pygame.font.Font("fonts/Mario64.ttf",40)
        textSurf, textRect = text_objects("**   Start   **", smallText)
        textRect.center = ( (450+(350/2)), (240+(80/2)) )
        win.blit(textSurf, textRect)
        #dito
        textSurf, textRect = text_objects("Quit", smallText)
        textRect.center = ( (450+(350/2)), (480+(80/2)) )
        win.blit(textSurf, textRect)
        #dito
        textSurf, textRect = text_objects("Instructions", smallText)
        textRect.center = ( (980+(250/2)), (610+(60/2)) )
        win.blit(textSurf, textRect)
        #dito
        textSurf, textRect = text_objects("NEW: 2 PLAYER", smallText)
        textRect.center = ( (980+(250/2)), (510+(60/2)) )
        win.blit(textSurf, textRect)
        #dito
        textSurf, textRect = text_objects("NUT", smallText)
        textRect.center = ( (50+(250/2)), (610+(60/2)) )
        win.blit(textSurf, textRect)
        #dito
        textSurf, textRect = text_objects("Settings", smallText)
        textRect.center = ( (50+(250/2)), (510+(60/2)) )
        win.blit(textSurf, textRect)
        #update screen
        pygame.display.update()
        #frame rate
        clock.tick(27)
#quit function
def quit_a():
    pygame.mouse.set_visible(True)
    gcache = globals()
    cache = str(sys.getsizeof(gcache))
    print('Global cache: ' + cache)
    print('quit')
    yes = True
    pygame.time.wait(200)
    while yes:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gcache = globals()
                cache = str(sys.getsizeof(gcache))
                print('Final Cache: ' + cache)
                pygame.quit()
                sys.exit()
                quit()
        win.fill(white)
        largeText = pygame.font.Font('fonts/SuperMario256.ttf',50)
        TextSurf, TextRect = text_objects("are you sure you want to quit?", largeText)
        TextRect.center = ((X/2),(Y/8))
        win.blit(TextSurf, TextRect)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 450+350 > mouse[0] > 450 and 240+80 > mouse[1] > 240:
            pygame.draw.rect(win, bright_green,(450,240,350,80))
            if click[0]:
                game_loop_1p()
        elif 450+350 > mouse[0] > 450 and 480+80 > mouse[1] > 480:
            pygame.draw.rect(win, bright_red,(450,480,350,80))
            pygame.draw.rect(win, green,(450,240,350,80))
            if click[0]:
                pygame.quit()
                sys.exit()
                quit()
        elif 5+50 >mouse[0] > 5 and 10+50 > mouse[1] > 10 and click[0]:
            game_intro()
        else:
            pygame.draw.rect(win, green,(450,240,350,80))
        win.blit(back_scaled, (5,((Y/8)-80)))
        pygame.draw.rect(win, red,(450,480,350,80))
        smallText = pygame.font.Font("fonts/Mario64.ttf",40)
        textSurf, textRect = text_objects("Play", smallText)
        textRect.center = ( (450+(350/2)), (240+(80/2)) )
        win.blit(textSurf, textRect)
        textSurf, textRect = text_objects("Quit", smallText)
        textRect.center = ( (450+(350/2)), (480+(80/2)) )
        win.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(27)
def settings():
    print('settings')
    gusty_garden = True
    pygame.mouse.set_visible(True)
    #this timer is important so as to allow the user to let go of the mouse button before bringing up this screen
    #otherwise it will hit the button under the cursor if the button is still down
    pygame.time.wait(200)
    fade_white(1280,720)
    while gusty_garden:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        win.fill(white)
        #title text
        largeText = pygame.font.Font('fonts/SuperMario256.ttf',50)
        TextSurf, TextRect = text_objects("Settings", largeText)
        TextRect.center = ((X/2),(Y/8))
        win.blit(TextSurf, TextRect)
        for event in pygame.event.get():
            #ive explained it already
            if event.type == pygame.QUIT:
                gcache = globals()
                cache = str(sys.getsizeof(gcache))
                print('Final Cache: ' + cache)
                pygame.quit()
                sys.exit()
                quit()
        if 5+50 >mouse[0] > 5 and 10+50 > mouse[1] > 10 and click[0]:
            game_intro()
        win.blit(back_scaled, (5,((Y/8)-80)))
        pygame.display.update()
        clock.tick(27)
        
def instructions():
    pygame.mouse.set_visible(True)
    gcache = globals()
    cache = str(sys.getsizeof(gcache))
    print('Global cache: ' + cache)
    #debug to see if it called instructions or not
    print('instructions')
    hmmm = True
    #this timer is important so as to allow the user to let go of the mouse button before bringing up this screen
    #otherwise it will hit the button under the cursor if the button is still down
    pygame.time.wait(200)
    fade_white(1280,720)
    while hmmm:
        for event in pygame.event.get():
            #ive explained it already
            if event.type == pygame.QUIT:
                gcache = globals()
                cache = str(sys.getsizeof(gcache))
                print('Final Cache: ' + cache)
                pygame.quit()
                sys.exit()
                quit()
        #white background. may become a nicer picture of something
        win.fill(white)
        #title text
        largeText = pygame.font.Font('fonts/SuperMario256.ttf',50)
        TextSurf, TextRect = text_objects("Heres how to play:", largeText)
        TextRect.center = ((X/2),(Y/8))
        win.blit(TextSurf, TextRect)
        #get position of mouse cursor
        mouse = pygame.mouse.get_pos()
        #get where they have or will click
        click = pygame.mouse.get_pressed()
        #smaller text
        largeText = pygame.font.Font('fonts/Mario64.ttf',40)
        TextSurf, TextRect = text_objects("In this game you control a character on their quest to save a princess", largeText)
        TextRect.center = ((X/2),(Y/5))
        #blit is pygame drawing fuction
        win.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("A - Left  /  D - Right  /  Space/W - Jump  /  Shift - Run", largeText)
        TextRect.center = ((X/2),(Y/3.5))
        win.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("2ND PLAYER: Left - Left  /  Right - Right  /  Up - Jump  /  Shift - Run", largeText)
        TextRect.center = ((X/2),(Y/2.5))
        win.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("Note: 2 player is unfinished and is not part of the main game.", largeText)
        TextRect.center = ((X/2),(Y/2))
        win.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("To jump on a trampoline press the jump button", largeText)
        TextRect.center = ((X/2),(Y/1.5))
        win.blit(TextSurf, TextRect)
        if 980+250 > mouse[0] > 980 and 610+60 > mouse[1] > 610:
            #bottom button (play now)
            pygame.draw.rect(win, bright_blue,(980,610,250,60))
            if click[0]:
                luigi2 = False
                lvlstrt.play()
                fade_out(1280,720)
                game_loop_1p()
        elif 980+250 > mouse[0] > 980 and 510+60 > mouse[1] > 510:
            #higher up button (2 player)
            pygame.draw.rect(win, bright_blue,(980,510,250,60))
            if click[0]:
                luigi2 = True
                lvlstrt.play()
                fade_out(1280,720)
                game_loop_2p()
        else:
            pygame.draw.rect(win, blue,(980,610,250,60))
            pygame.draw.rect(win, blue,(980,510,250,60))
        pygame.draw.rect(win, blue,(980,510,250,60))
        pygame.draw.rect(win, blue,(980,610,250,60))
        #buttons lables
        smallText = pygame.font.Font("fonts/Mario64.ttf",40)
        textSurf, textRect = text_objects("play", smallText)
        textRect.center = ( (980+(250/2)), (610+(60/2)) )
        win.blit(textSurf, textRect)
        textSurf, textRect = text_objects("play (2p)", smallText)
        textRect.center = ( (980+(250/2)), (510+(60/2)) )
        win.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(27)
#main game
def game_loop_1p():
    global oneup_draw2
    global coin_counter
    global coin2_draw
    global coin1_draw
    global oneup_draw1
    global oneup_cntr
    global star1_get
    global star_cntr
    global star1_get_pause
    global hudclock
    global nextlvl
    global score
    global timetocomplete
    global timetocomplete2
    nextlvl = 1
    timer = 0
    hudclock = 200
    if hudclock <= 5:
        hudclock = 101
    pygame.mouse.set_visible(False)
    gcache = globals()
    cache = str(sys.getsizeof(gcache))
    print('Global cache: ' + cache)
    print('1 player')
    global luigi2
    print(luigi2)
    jah = True
    #music
    music = pygame.mixer.music.load('audio/music.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    redrawGameWindow()
    while jah:
        if mario.jumpCount <= -7:
            mario.jumpCount = -7
        #hitboxes
        hitbox = pygame.Rect(mario.x, mario.y, mario.width, mario.height)
        coin1 = pygame.Rect(175, 153, 32, 32)
        coin2 = pygame.Rect(275, 153, 32, 32)
        trampoline = pygame.Rect(150, 635, 32, 64)
        oneuptest = pygame.Rect(225, 153, 32, 32)
        test = pygame.Rect.colliderect(hitbox, coin1)
        oneuptest2 = pygame.Rect(528, 655, 32, 32)
        test1 = pygame.Rect.colliderect(hitbox, coin2)
        wallonright2 = pygame.Rect(225, 247, 16, 440)
        wallonleft2 = pygame.Rect(241, 247, 16, 440)
        trampolinetst = pygame.Rect.colliderect(hitbox, trampoline)
        floor = pygame.Rect(0, 687, 1280, 64)
        grnd_227 = pygame.Rect(225, 207, 32, 128)
        block = pygame.Rect(853, 654, 26, 32)
        wallonright1 = pygame.Rect(850, 682, 16, 5)
        wallonleft1 = pygame.Rect(866, 682, 16, 5)
        step1 = pygame.Rect(400, 655, 32, 32)
        step2 = pygame.Rect(432, 623, 32, 32)
        step3 = pygame.Rect(464, 591, 32, 32)
        step4 = pygame.Rect(496, 559, 16, 32)
        step5 = pygame.Rect(576, 559, 16, 32)
        step6 = pygame.Rect(592, 591, 32, 32)
        step7 = pygame.Rect(624, 623, 32, 32)
        step8 = pygame.Rect(656, 655, 32, 32)
        podium639 = pygame.Rect(1150, 639, 32, 48)
        podium667 = pygame.Rect(1118, 667, 32, 20)
        podium655 = pygame.Rect(1182, 655, 32, 32)
        sticky = pygame.Rect(225, 0, 32, 100)
        startst = pygame.Rect(1150, 525, 32, 32)
        floortest = pygame.Rect.colliderect(hitbox, floor)
        landtest = pygame.Rect.colliderect(hitbox, block)
        hitboxes = [wallonleft1, wallonleft2, wallonright1, wallonright2, grnd_227, sticky, oneuptest, startst, step1, step2, step3, step4, step5, step6, step7, step8, podium655, podium667, podium639, oneuptest2]
        hittest = pygame.Rect.collidelist(hitbox, hitboxes)
        if hittest == -1 and landtest == False and floortest == False and trampolinetst == False and not(mario.isJump):
            mario.y -= (mario.fall * abs(mario.fall)) // 2
            mario.fall -= 0.75
            if mario.fall <= -3:
                mario.fall == 0
                mario.isJump = True
                mario.jumpCount = -3
        else:
            mario.fall = 0
        if hittest == -1:
            wall_left = False
            wall_right = False
        if hittest == 0 or hittest == 1:
            wall_left = True
            wall_right = False
        if hittest == 2 or hittest == 3:
            wall_right = True
            wall_left = False
        if hittest == 4:
            mario.y = (207 - mario.height)
            mario.jumpCount = 10
            mario.isJump = False
        if hittest == 5:
            mario.jumpCount = -2
        if hittest == 6 and oneup_draw1 == True:
            oneup_draw1 = False
            oneup_cntr += 1
            score += 500
            oneup_jingle.play()
        if hittest == 7 and star1_get == False:
            star1_get = True
            star1_get_pause = True
            star_cntr += 1
            star.play()
            score += 10000
            redrawGameWindow()
            pygame.time.delay(500)
            pygame.mixer.music.stop()
            cutscene()
        if hittest == 8 or hittest == 15 or hittest == 16:
            mario.y = (655 - mario.height)
            mario.jumpCount = 10
            mario.isJump = False
        if hittest == 9 or hittest == 14:
            mario.y = (623 - mario.height)
            mario.jumpCount = 10
            mario.isJump = False
        if hittest == 10 or hittest == 13:
            mario.y = (591 - mario.height)
            mario.jumpCount = 10
            mario.isJump = False
        if hittest == 11 or hittest == 12:
            mario.y = (559 - mario.height)
            mario.jumpCount = 10
            mario.isJump = False
        if test == True and coin1_draw == True:
            coin1_draw = False
            coin_counter += 1
            score += 100
            coin_snd.play()
        if test1 == True and coin2_draw == True:
            coin2_draw = False
            coin_counter += 1
            score += 100
            coin_snd.play()
        if trampolinetst == True:
            if keys[pygame.K_w] or keys[pygame.K_SPACE]:
                tramp.play()
                mario.jumpCount = 14
                score += 50
            else:
                mario.y = (660 - mario.height)
                mario.jumpCount = 14
                mario.isJump = False
        if floortest == True:
            mario.y = (687 - mario.height)
            mario.jumpCount = 10
            mario.isJump = False
            mario.fall = 0
        if landtest == True:
            mario.y = (654 - mario.height)
            mario.jumpCount = 10
            mario.isJump = False
        if hittest == 17:
            mario.y = (667 - mario.height)
            mario.jumpCount = 10
            mario.isJump = False
        if hittest == 16:
            mario.y = (655 - mario.height)
            mario.jumpCount = 10
            mario.isJump = False
        if hittest == 18:
            mario.y = (639 - mario.height)
            mario.jumpCount = 10
            mario.isJump = False
        if hittest == 19 and oneup_draw2 == True:
            oneup_draw2 = False
            oneup_cntr += 1
            score += 500
            oneup_jingle.play()
        if timer == 30:
            timer = 0
            hudclock -= 1
        if timer == 0 and hudclock == 100:
            pygame.mixer.music.stop()
            hurryup.play()
            pygame.time.delay(400)
            music = pygame.mixer.music.load('audio/music_faster.mp3')
            pygame.mixer.music.play(-1)
        if timer == 0 and hudclock == 0:
            redrawGameWindow()
            death.play()
            pygame.time.delay(200)
            score -= 100
            oneup_cntr -= 1
            pygame.mixer.music.stop()
            music = pygame.mixer.music.load('audio/outoftime.mp3')
            pygame.mixer.music.play(0)
            pygame.time.delay(1000)
            fade_out(1280,720)
            hudclock = 150
            game_loop_1p()
        timetocomplete += 1
        #p2 of frame limiter
        clock.tick(30)
        #check whether closed to allow for safe quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gcache = globals()
                cache = str(sys.getsizeof(gcache))
                print('Final Cache: ' + cache)
                #un-init pygame modules
                pygame.quit()
                #sys exit
                sys.exit()
                #noob exit
                quit()
        #part of finding what key your pressing
        keys = pygame.key.get_pressed()
        #key to go left
        if star1_get == True and star1_get_pause == False and mario.y == 655:
            pygame.time.delay(2000)
            star1_get_pause = True
        if keys[pygame.K_a] and mario.x > mario.vel and not(wall_left):
            mario.idle_type = False
            #if holding sprint button
            if keys[pygame.K_LSHIFT]:
                if not(mario.isJump):
                    pass
                #double velocity (speed)
                mario.vel = 10
                #move -x by the velocity
                mario.x -= mario.vel
                #change these statments for facing direction
                mario.left = True
                mario.right = False
            #must not be wanting to sprint
            else:
                if not(mario.isJump):
                    pass
                #normal velocity
                mario.vel = 5
                #move -x by velocity
                mario.x -= mario.vel
                #facing directions
                mario.left = True
                mario.right = False
        #key to go right
        elif keys[pygame.K_d] and mario.x < 1280 - mario.vel - mario.width and not(wall_right):
            mario.idle_type = True
            #if wanting to sprint
            if keys[pygame.K_LSHIFT]:
                if not(mario.isJump):
                    pass
                #double velocity
                mario.vel = 10
                #move +x by velocity
                mario.x += mario.vel
                #facing directions
                mario.left = False
                mario.right = True
            else:
                if not(mario.isJump):
                    pass
                #normal velocity
                mario.vel = 5
                #move +x by velocity
                mario.x += mario.vel
                #facing direction
                mario.left = False
                mario.right = True

        #part of direction facing
        else:
            #standing still
            mario.left = False
            mario.right = False
            mario.walkCount = 0
        #if is jump is false (to prevent jumping in air lol maybe i will allow double jump
        if not(mario.isJump):
            #if spacebar is held (jump button)
            if keys[pygame.K_w] or keys[pygame.K_SPACE]:
                score += 5
                jumpsnd.play()
                #is jump is now true (cannot jump anymore. begins jump procedure)
                mario.isJump = True
                #dont walk in air and change direction
                mario.left = False
                mario.right = False
                #no walk animation in air
                mario.walkCount = 0
        #arc of falling
        else:
            if mario.jumpCount >= -50:
                #quadratics reeeee
                #the abs makes the negative positive and the positive positive
                #w/o abs, charcater jumps to peak, and then goes up again, instead of down
                mario.y -= (mario.jumpCount * abs(mario.jumpCount)) // 2
                mario.jumpCount -= 0.8
                mario.vel = 3
            else:
                #jump has finished - cleanup
                mario.vel = 5
                mario.jumpCount = 10
                mario.isJump = False
        timer += 1
        #redraw game window function to draw other entities that we want to draw
        redrawGameWindow()
#level 2 game logic
def game_lvl2():
    global oneup_draw2
    global coin_counter
    global coin2_draw
    global coin1_draw
    global oneup_draw1
    global oneup_cntr
    global star1_get
    global star_cntr
    global star1_get_pause
    global hudclock
    global nextlvl
    global timer
    global score
    global timetocomplete
    #reset variables
    timer = 0
    star1_get = False
    mario.x = 55
    mario.y = 328
    wall_left = False
    wall_right = False
    pygame.mouse.set_visible(False)
    jah = True
    #hudclock = 500
    if hudclock <= 5:
        hudclock = 101
    #music
    music = pygame.mixer.music.load('audio/music.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    redrawGameWindow2()
    while jah:
        if mario.jumpCount <= -7:
            mario.jumpCount = -7
        hitbox = pygame.Rect(mario.x, mario.y, mario.width, mario.height)
        startst = pygame.Rect(1150, 260, 32, 32)
        floor1 = pygame.Rect(0, 360, 640, 32)
        floor2 = pygame.Rect(736, 360, 544, 32)
        wallonleft = pygame.Rect(627, 370, 16, 350)
        wallonright = pygame.Rect(733, 370, 16, 350)
        hitboxes = [startst, floor1, floor2, wallonleft, wallonright]
        hittest = pygame.Rect.collidelist(hitbox, hitboxes)
        if hittest == -1 and not(mario.isJump):
            mario.y -= (mario.fall * abs(mario.fall)) // 2
            mario.fall -= 0.75
            if mario.fall <= -3:
                mario.fall == 0
                mario.isJump = True
                mario.jumpCount = -3
        else:
            mario.fall = 0
        if hittest == -1:
            wall_left = False
            wall_right = False
        if hittest == 0 and star1_get == False:
            star1_get = True
            star1_get_pause = True
            star_cntr += 1
            star.play()
            score += 10000
            redrawGameWindow2()
            pygame.time.delay(500)
            pygame.mixer.music.stop()
            cutscene()
            game_lvl3()
        if hittest == 3:
            wall_left = True
            wall_right = False
        if hittest == 4:
            wall_left = False
            wall_right = True
        if hittest == 1 or hittest == 2:
            mario.y = 360-mario.height
            mario.jumpCount = 10
            mario.isJump = False
        if timer == 30:
            timer = 0
            hudclock -= 1
        if timer == 0 and hudclock == 100:
            pygame.mixer.music.stop()
            hurryup.play()
            pygame.time.delay(400)
            music = pygame.mixer.music.load('audio/music_faster.mp3')
            pygame.mixer.music.play(-1)
        if timer == 0 and hudclock == 0:
            redrawGameWindow2()
            death.play()
            pygame.time.delay(200)
            score -= 100
            oneup_cntr -= 1
            pygame.mixer.music.stop()
            music = pygame.mixer.music.load('audio/outoftime.mp3')
            pygame.mixer.music.play(0)
            pygame.time.delay(1000)
            fade_out(1280,720)
            hudclock = 150
            game_lvl2()
        if mario.y >= (720-mario.height):
            death.play()
            score -= 100
            oneup_cntr -= 1
            mario.y = 360-mario.height
            mario.x = 55
            wall_left = False
            wall_right = False
        #p2 of frame limiter
        clock.tick(30)
        timetocomplete += 1
        if star1_get == True and star1_get_pause == False and mario.y == 655:
            pygame.time.delay(2000)
            star1_get_pause = True
        #check whether closed to allow for safe quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gcache = globals()
                cache = str(sys.getsizeof(gcache))
                print('Final Cache: ' + cache)
                #un-init pygame modules
                pygame.quit()
                #sys exit
                sys.exit()
                #noob exit
                quit()
        #part of finding what key your pressing
        keys = pygame.key.get_pressed()
        #key to go left
        if keys[pygame.K_a] and mario.x > mario.vel and not(wall_left):
            mario.idle_type = False
            #if holding sprint button
            if keys[pygame.K_LSHIFT]:
                if not(mario.isJump):
                    pass
                #double velocity (speed)
                mario.vel = 10
                #move -x by the velocity
                mario.x -= mario.vel
                #change these statments for facing direction
                mario.left = True
                mario.right = False
            #must not be wanting to sprint
            else:
                if not(mario.isJump):
                    pass
                #normal velocity
                mario.vel = 5
                #move -x by velocity
                mario.x -= mario.vel
                #facing directions
                mario.left = True
                mario.right = False
        #key to go right
        elif keys[pygame.K_d] and mario.x < 1280 - mario.vel - mario.width and not(wall_right):
            mario.idle_type = True
            #if wanting to sprint
            if keys[pygame.K_LSHIFT]:
                if not(mario.isJump):
                    pass
                #double velocity
                mario.vel = 10
                #move +x by velocity
                mario.x += mario.vel
                #facing directions
                mario.left = False
                mario.right = True
            else:
                if not(mario.isJump):
                    pass
                #normal velocity
                mario.vel = 5
                #move +x by velocity
                mario.x += mario.vel
                #facing direction
                mario.left = False
                mario.right = True

        #part of direction facing
        else:
            #standing still
            mario.left = False
            mario.right = False
            mario.walkCount = 0
        #if is jump is false (to prevent jumping in air lol maybe i will allow double jump
        if not(mario.isJump):
            #if spacebar is held (jump button)
            if keys[pygame.K_w] or keys[pygame.K_SPACE]:
                score += 5
                jumpsnd.play()
                #is jump is now true (cannot jump anymore. begins jump procedure)
                mario.isJump = True
                #dont walk in air and change direction
                mario.left = False
                mario.right = False
                #no walk animation in air
                mario.walkCount = 0
        #arc of falling
        else:
            if mario.jumpCount >= -50:
                #quadratics reeeee
                #the abs makes the negative positive and the positive positive
                #w/o abs, charcater jumps to peak, and then goes up again, instead of down
                mario.y -= (mario.jumpCount * abs(mario.jumpCount)) // 2
                mario.jumpCount -= 0.8
                mario.vel = 3
            else:
                #jump has finished - cleanup
                mario.vel = 5
                mario.jumpCount = 10
                mario.isJump = False
        timer += 1
        #redraw game window function to draw other entities that we want to draw
        redrawGameWindow2()
def game_lvl3():
    global oneup_draw2
    global coin_counter
    global coin2_draw
    global coin1_draw
    global oneup_draw1
    global oneup_cntr
    global star1_get
    global star_cntr
    global star1_get_pause
    global hudclock
    global nextlvl
    global score
    global timer
    global timetocomplete
    #reset variables
    timer = 0
    star1_get = False
    mario.x = 55
    mario.y = 682
    pygame.mouse.set_visible(False)
    jah = True
    #hudclock = 500
    if hudclock <= 5:
        hudclock = 101
    wall_left = False
    wall_right = False
    #music
    music = pygame.mixer.music.load('audio/music.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    redrawGameWindow3()
    while jah:
        if mario.jumpCount <= -7:
            mario.jumpCount = -7
        hitbox = pygame.Rect(mario.x, mario.y, mario.width, mario.height)
        startst = pygame.Rect(1150, 500, 32, 32)
        floor1 = pygame.Rect(0, 687, 1280, 64)
        floor2 = pygame.Rect(300, 350,200, 64)
        floor3 = pygame.Rect(900, 350,200, 64)
        floor4 = pygame.Rect(600, 350,200, 64)
        slime1 = pygame.Rect(700, 0, 260, 64)
        slime2 = pygame.Rect(350, 0, 260, 64)
        muncher1 = pygame.Rect(500, 655, 100, 32)
        muncher2 = pygame.Rect(800, 655, 100, 32)
        wallonleft = pygame.Rect(298, 450, 16, 237)
        wallonleft2 = pygame.Rect(898, 150, 16, 577)
        wallonleft3 = pygame.Rect(598, 150, 16, 577)
        wallonright = pygame.Rect(486, 450, 16, 237)
        wallonright2 = pygame.Rect(1086, 450, 16, 237)
        wallonright3 = pygame.Rect(786, 450, 16, 237)
        trampo = pygame.Rect(150, 655, 32, 32)
        trampo2 = pygame.Rect(384, 310, 32, 42)
        trampo3 = pygame.Rect(700, 310, 32, 42)
        trampcheck = pygame.Rect.colliderect(hitbox, trampo)
        trampcheck2 = pygame.Rect.colliderect(hitbox, trampo2)
        trampcheck3 = pygame.Rect.colliderect(hitbox, trampo3)
        grndtst = pygame.Rect.colliderect(hitbox,floor1)
        hitboxes = [startst, slime1, floor2, floor3, floor4, muncher1, muncher2, wallonleft, wallonright, slime2, wallonleft2, wallonleft3, wallonright2, wallonright3]
        hittest = pygame.Rect.collidelist(hitbox, hitboxes)
        if hittest == -1 and grndtst == False and trampcheck == False and trampcheck2 == False and trampcheck3 == False and not(mario.isJump):
            mario.y -= (mario.fall * abs(mario.fall)) // 2
            mario.fall -= 0.75
            if mario.fall <= -3:
                mario.fall == 0
                mario.isJump = True
                mario.jumpCount = -3
        else:
            mario.fall = 0
        if hittest == -1:
            wall_left = False
            wall_right = False
        if hittest == 0 and star1_get == False:
            star1_get = True
            star1_get_pause = True
            star_cntr += 1
            score += 10000
            star.play()
            redrawGameWindow3()
            pygame.time.delay(500)
            pygame.mixer.music.stop()
            cutscene()
        if hittest == 8 or hittest == 12 or hittest == 13:
            wall_left = True
            wall_right = False
        if hittest == 7 or hittest == 10 or hittest == 11:
            wall_left = False
            wall_right = True
        if timer == 30:
            timer = 0
            hudclock -= 1
        if timer == 0 and hudclock == 100:
            pygame.mixer.music.stop()
            hurryup.play()
            pygame.time.delay(400)
            music = pygame.mixer.music.load('audio/music_faster.mp3')
            pygame.mixer.music.play(-1)
        if timer == 0 and hudclock == 0:
            redrawGameWindow3()
            death.play()
            pygame.time.delay(200)
            score -= 100
            oneup_cntr -= 1
            pygame.mixer.music.stop()
            music = pygame.mixer.music.load('audio/outoftime.mp3')
            pygame.mixer.music.play(0)
            pygame.time.delay(1000)
            fade_out(1280,720)
            game_lvl3()
        if timer == 0 and hudclock == 100:
            hurryup.play()
        if timer == 30 and hudclock == 0:
          death.play()
          pygame.time.delay(200)
          score -= 100
          oneup_cntr -= 1
          pygame.mixer.music.stop()
          music = pygame.mixer.music.load('audio/outoftime.mp3')
          pygame.mixer.music.play(0)
          hudclock = 101
          fade_out(1280,720)
        if hittest == 5 or hittest == 6:
            death.play()
            score -= 100
            oneup_cntr -= 1
            mario.y = 682-mario.height
            mario.x = 55
            wall_left = False
            wall_right = False
        if hittest == 2 or hittest == 3 or hittest == 4:
            mario.y = 350-mario.height
            mario.jumpCount = 10
            mario.isJump = False
        if hittest == 1 or hittest == 9:
            mario.jumpCount = -1
        if trampcheck2 == True or trampcheck3 == True:
            if keys[pygame.K_w] or keys[pygame.K_SPACE]:
                tramp.play()
                score += 50
                mario.jumpCount = 14
            else:
                mario.y = (325 - mario.height)
                mario.jumpCount = 14
                mario.isJump = False
        if trampcheck == True:
            if keys[pygame.K_w] or keys[pygame.K_SPACE]:
                tramp.play()
                score += 50
                mario.jumpCount = 14
            else:
                mario.y = (660 - mario.height)
                mario.jumpCount = 14
                mario.isJump = False
        if grndtst == True:
            mario.y = 687-mario.height
            mario.jumpCount = 10
            mario.isJump = False
        #p2 of frame limiter
        clock.tick(30)
        timetocomplete += 1
        if star1_get == True and star1_get_pause == False and mario.y == 655:
            pygame.time.delay(2000)
            star1_get_pause = True
        #check whether closed to allow for safe quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gcache = globals()
                cache = str(sys.getsizeof(gcache))
                print('Final Cache: ' + cache)
                #un-init pygame modules
                pygame.quit()
                #sys exit
                sys.exit()
                #noob exit
                quit()
        #part of finding what key your pressing
        keys = pygame.key.get_pressed()
        #key to go left
        if keys[pygame.K_a] and mario.x > mario.vel and not(wall_left):
            mario.idle_type = False
            #if holding sprint button
            if keys[pygame.K_LSHIFT]:
                if not(mario.isJump):
                    pass
                #double velocity (speed)
                mario.vel = 10
                #move -x by the velocity
                mario.x -= mario.vel
                #change these statments for facing direction
                mario.left = True
                mario.right = False
            #must not be wanting to sprint
            else:
                if not(mario.isJump):
                    pass
                #normal velocity
                mario.vel = 5
                #move -x by velocity
                mario.x -= mario.vel
                #facing directions
                mario.left = True
                mario.right = False
        #key to go right
        elif keys[pygame.K_d] and mario.x < 1280 - mario.vel - mario.width and not(wall_right):
            mario.idle_type = True
            #if wanting to sprint
            if keys[pygame.K_LSHIFT]:
                if not(mario.isJump):
                    pass
                #double velocity
                mario.vel = 10
                #move +x by velocity
                mario.x += mario.vel
                #facing directions
                mario.left = False
                mario.right = True
            else:
                if not(mario.isJump):
                    pass
                #normal velocity
                mario.vel = 5
                #move +x by velocity
                mario.x += mario.vel
                #facing direction
                mario.left = False
                mario.right = True

        #part of direction facing
        else:
            #standing still
            mario.left = False
            mario.right = False
            mario.walkCount = 0
        #if is jump is false (to prevent jumping in air lol maybe i will allow double jump
        if not(mario.isJump):
            #if spacebar is held (jump button)
            if keys[pygame.K_w] or keys[pygame.K_SPACE]:
                score += 5
                jumpsnd.play()
                #is jump is now true (cannot jump anymore. begins jump procedure)
                mario.isJump = True
                #dont walk in air and change direction
                mario.left = False
                mario.right = False
                #no walk animation in air
                mario.walkCount = 0
        #arc of falling
        else:
            if mario.jumpCount >= -50:
                #quadratics reeeee
                #the abs makes the negative positive and the positive positive
                #w/o abs, charcater jumps to peak, and then goes up again, instead of down
                mario.y -= (mario.jumpCount * abs(mario.jumpCount)) // 2
                mario.jumpCount -= 0.8
                mario.vel = 3
            else:
                #jump has finished - cleanup
                mario.vel = 5
                mario.jumpCount = 10
                mario.isJump = False
        timer += 1
        #redraw game window function to draw other entities that we want to draw
        redrawGameWindow3()
def game_lvl4():
    global oneup_draw2
    global coin_counter
    global coin3_draw
    global coin2_draw
    global coin1_draw
    global oneup_draw1
    global oneup_cntr
    global star1_get
    global star_cntr
    global star1_get_pause
    global hudclock
    global nextlvl
    global score
    global timer
    global timetocomplete
    global secret3_draw
    global secret4_draw
    #reset variables
    timer = 0
    star1_get = False
    mario.x = 55
    mario.y = 682
    pygame.mouse.set_visible(False)
    jah = True
    #hudclock = 101
    if hudclock <= 5:
        hudclock = 101
    wall_left = False
    wall_right = False
    #music
    music = pygame.mixer.music.load('audio/music.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    redrawGameWindow4()
    while jah:
        if mario.jumpCount <= -7:
            mario.jumpCount = -7
        hitbox = pygame.Rect(mario.x, mario.y, mario.width, mario.height)
        startst = pygame.Rect(1150, 500, 32, 32)
        floor1 = pygame.Rect(0, 687, 1280, 64)
        floor2 = pygame.Rect(445,55,111,32)
        floor3 = pygame.Rect(465,515,88,16)
        floor4 = pygame.Rect(610,510,64,32)
        floor5 = pygame.Rect(655,160,27,11)
        floor6 = pygame.Rect(1108,570,139,32)
        floor7 = pygame.Rect(767,216,123,32)
        slime1 = pygame.Rect(135, 220, 279, 32)
        slime2 = pygame.Rect(740,120,32,96)
        muncher1 = pygame.Rect(555,653,210,32)
        muncher2 = pygame.Rect(682,0,85,32)
        muncher3 = pygame.Rect(889,655,388,32)
        muncher4 = pygame.Rect(1248,0,32,665)
        wallonleft = pygame.Rect(444,87,16,600)
        wallonleft2 = pygame.Rect(660,0,11,82)
        wallonleft3 = pygame.Rect(659,175,11,263)
        wallonleft4 = pygame.Rect(766,0,32,90)
        wallonleft5 = pygame.Rect(765,253,32,435)
        wallonright = pygame.Rect(455,440,16,80)
        wallonright2 = pygame.Rect(671,0,11,82)
        wallonright3 = pygame.Rect(672,175,11,263)
        wallonright4 = pygame.Rect(860,253,32,435)
        wallonright5 = pygame.Rect(858,0,32,90)
        wallonright6 = pygame.Rect(539,86,16,355)
        wallonright7 = pygame.Rect(539,525,16,172)
        ceiling1 = pygame.Rect(660,82,22,16)
        ceiling2 = pygame.Rect(660,407,22,56)
        ceiling3 = pygame.Rect(766,87,123,32)
        ceiling4 =  pygame.Rect(465,424,88,16)
        trampo = pygame.Rect(300, 655, 32, 32)
        trampo2 = pygame.Rect(80, 350, 32, 42)
        trampo3 = pygame.Rect(676,510,64,32)
        coin123 = pygame.Rect(496,462,32,32)
        trampcheck = pygame.Rect.colliderect(hitbox, trampo)
        trampcheck2 = pygame.Rect.colliderect(hitbox, trampo2)
        trampcheck3 = pygame.Rect.colliderect(hitbox, trampo3)
        ceilingtest1 = pygame.Rect.colliderect(hitbox, ceiling1)
        ceilingtest2 = pygame.Rect.colliderect(hitbox, ceiling2)
        ceilingtest3 = pygame.Rect.colliderect(hitbox, ceiling3)
        ceilingtest4 = pygame.Rect.colliderect(hitbox, ceiling4)
        cointest69 = pygame.Rect.colliderect(hitbox, coin123)
        grndtst = pygame.Rect.colliderect(hitbox,floor1)
        hitboxes = [startst, slime1, floor2, floor3, floor4, muncher1, muncher2, wallonleft, wallonright, slime2, wallonleft2, wallonleft3, wallonright2, wallonright3, floor5, floor6, floor7, muncher3, muncher4, wallonleft4, wallonleft5, wallonright4, wallonright5, wallonright6, wallonright7]
        hittest = pygame.Rect.collidelist(hitbox, hitboxes)
        if hittest == -1 and grndtst == False and trampcheck == False and trampcheck2 == False and trampcheck3 == False and not(mario.isJump):
            mario.y -= (mario.fall * abs(mario.fall)) // 2
            mario.fall -= 0.75
            if mario.fall <= -3:
                mario.fall == 0
                mario.isJump = True
                mario.jumpCount = -3
        else:
            mario.fall = 0
        if hittest == -1:
            wall_left = False
            wall_right = False
        if cointest69 == True and coin3_draw == True:
            coin3_draw = False
            coin_counter += 1
            score += 100
            coin_snd.play()
        if hittest == 0 and star1_get == False:
            star1_get = True
            star1_get_pause = True
            star_cntr += 1
            score += 10000
            star.play()
            redrawGameWindow4()
            pygame.time.delay(500)
            pygame.mixer.music.stop()
            cutscene()
        if hittest == 8 or hittest == 12 or hittest == 13 or hittest == 21 or hittest == 22 or hittest == 23 or hittest == 24:
            wall_left = True
            wall_right = False
        if hittest == 7 or hittest == 10 or hittest == 11 or hittest == 19 or hittest == 20:
            wall_left = False
            wall_right = True
        if timer == 30:
            timer = 0
            hudclock -= 1
        if timer == 0 and hudclock == 100:
            pygame.mixer.music.stop()
            hurryup.play()
            pygame.time.delay(400)
            music = pygame.mixer.music.load('audio/music_faster.mp3')
            pygame.mixer.music.play(-1)
        if timer == 0 and hudclock == 0:
            redrawGameWindow4()
            death.play()
            pygame.time.delay(200)
            score -= 100
            oneup_cntr -= 1
            pygame.mixer.music.stop()
            music = pygame.mixer.music.load('audio/outoftime.mp3')
            pygame.mixer.music.play(0)
            pygame.time.delay(1000)
            hudclock = 101
            fade_out(1280,720)
            game_lvl4()
        if hittest == 5 or hittest == 6 or hittest == 17 or hittest == 18:
            death.play()
            score -= 100
            oneup_cntr -= 1
            mario.y = 682-mario.height
            mario.x = 55
            wall_left = False
            wall_right = False
        if hittest == 2:
            mario.y = 55-mario.height
            mario.jumpCount = 10
            mario.isJump = False
        if hittest == 3:
            mario.y = 515-mario.height
            mario.jumpCount = 10
            mario.isJump = False
        if hittest == 4:
            mario.y = 510-mario.height
            mario.jumpCount = 10
            mario.isJump = False
        if hittest == 1 or hittest == 9:
            mario.jumpCount = -1
        if hittest == 14:
            mario.y = 160-mario.height
            mario.jumpCount = 10
            mario.isJump = False
        if hittest == 15:
            mario.y = 570-mario.height
            mario.jumpCount = 10
            mario.isJump = False
        if hittest == 16:
            mario.y = 216-mario.height
            mario.jumpCount = 10
            mario.isJump = False
        if ceilingtest1 == True:
            mario.y = 82+22
            mario.jumpCount = -5
        if ceilingtest2 == True:
            mario.y = 439+16
            mario.jumpCount = -5
        if ceilingtest3 == True:
            mario.y = 87+32
            mario.jumpCount = -3
        if ceilingtest4 == True:
            mario.y = 424+16
            mario.jumpCount = -5
        if trampcheck3 == True:
            if keys[pygame.K_w] or keys[pygame.K_SPACE]:
                tramp.play()
                score += 50
                mario.jumpCount = 14
            else:
                mario.y = (510 - mario.height)
                mario.jumpCount = 14
                mario.isJump = False
        if trampcheck2 == True:
            if keys[pygame.K_w] or keys[pygame.K_SPACE]:
                tramp.play()
                score += 50
                mario.jumpCount = 14
            else:
                mario.y = (350 - mario.height)
                mario.jumpCount = 14
                mario.isJump = False
        if trampcheck == True:
            if keys[pygame.K_w] or keys[pygame.K_SPACE]:
                tramp.play()
                score += 50
                mario.jumpCount = 13
            else:
                mario.y = (660 - mario.height)
                mario.jumpCount = 13
                mario.isJump = False
        if grndtst == True:
            mario.y = 687-mario.height
            mario.jumpCount = 10
            mario.isJump = False
        if mario.x > 469-mario.width and mario.x < 469+88+mario.width and mario.y > 442-mario.height and mario.y < 442+75+mario.height:
            secret3_draw = True
        else:
            secret3_draw = False
        if mario.x > 659-mario.width and mario.x < 659+24+mario.width and mario.y > 89-mario.height and mario.y < 89+73+mario.height:
            secret4_draw = True
        else:
            secret4_draw = False
        #p2 of frame limiter
        clock.tick(30)
        timetocomplete += 1
        if star1_get == True and star1_get_pause == False and mario.y == 655:
            pygame.time.delay(2000)
            star1_get_pause = True
        #check whether closed to allow for safe quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gcache = globals()
                cache = str(sys.getsizeof(gcache))
                print('Final Cache: ' + cache)
                #un-init pygame modules
                pygame.quit()
                #sys exit
                sys.exit()
                #noob exit
                quit()
        #part of finding what key your pressing
        keys = pygame.key.get_pressed()
        #key to go left
        if keys[pygame.K_a] and mario.x > mario.vel and not(wall_left):
            mario.idle_type = False
            #if holding sprint button
            if keys[pygame.K_LSHIFT]:
                if not(mario.isJump):
                    pass
                #double velocity (speed)
                mario.vel = 10
                #move -x by the velocity
                mario.x -= mario.vel
                #change these statments for facing direction
                mario.left = True
                mario.right = False
            #must not be wanting to sprint
            else:
                if not(mario.isJump):
                    pass
                #normal velocity
                mario.vel = 5
                #move -x by velocity
                mario.x -= mario.vel
                #facing directions
                mario.left = True
                mario.right = False
        #key to go right
        elif keys[pygame.K_d] and mario.x < 1280 - mario.vel - mario.width and not(wall_right):
            mario.idle_type = True
            #if wanting to sprint
            if keys[pygame.K_LSHIFT]:
                if not(mario.isJump):
                    pass
                #double velocity
                mario.vel = 10
                #move +x by velocity
                mario.x += mario.vel
                #facing directions
                mario.left = False
                mario.right = True
            else:
                if not(mario.isJump):
                    pass
                #normal velocity
                mario.vel = 5
                #move +x by velocity
                mario.x += mario.vel
                #facing direction
                mario.left = False
                mario.right = True

        #part of direction facing
        else:
            #standing still
            mario.left = False
            mario.right = False
            mario.walkCount = 0
        #if is jump is false (to prevent jumping in air lol maybe i will allow double jump
        if not(mario.isJump):
            #if spacebar is held (jump button)
            if keys[pygame.K_w] or keys[pygame.K_SPACE]:
                score += 5
                jumpsnd.play()
                #is jump is now true (cannot jump anymore. begins jump procedure)
                mario.isJump = True
                #dont walk in air and change direction
                mario.left = False
                mario.right = False
                #no walk animation in air
                mario.walkCount = 0
        #arc of falling
        else:
            if mario.jumpCount >= -50:
                #quadratics reeeee
                #the abs makes the negative positive and the positive positive
                #w/o abs, charcater jumps to peak, and then goes up again, instead of down
                mario.y -= (mario.jumpCount * abs(mario.jumpCount)) // 2
                mario.jumpCount -= 0.8
                mario.vel = 3
            else:
                #jump has finished - cleanup
                mario.vel = 5
                mario.jumpCount = 10
                mario.isJump = False
        timer += 1
        #redraw game window function to draw other entities that we want to draw
        redrawGameWindow4()
def score_tally():
    global timetocomplete
    global score
    global highscore
    global besttime
    highscore = 69
    fade_white(1280, 720)
    win.fill(white)
    timetocomplete2 = timetocomplete/30
    time_yes = str(timedelta(seconds=timetocomplete2))
    time_yes2 = time_yes[:-3]
    if int(score) >= int(lb[0]):
        highscore = score
    else:
        score = lb[0]
    hum = lb[3].replace(":","")
    hummm = hum.replace(".","")
    testin = time_yes.replace(":", "")
    testingg = testin.replace(".", "")
    if testingg <= hum:
        besttime = time_yes
    else:
        besttime = lb[3]
    smallText = pygame.font.Font("fonts/Mario64.ttf",40)
    textSurf, textRect = text_objects("High score:  " + str(highscore), smallText)
    textRect.center = (1280//2, ((720//2)-150))
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects("Your Score:  " + str(score), smallText)
    textRect.center = (1280//2, ((720//2)-100) )
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects("Developer High Score:  " + lb[2], smallText)
    textRect.center = (1280//2, (-50+(720//2)) )
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects("Time to complete:  " + time_yes, smallText)
    textRect.center = (1280//2, (50+(720//2)) )
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects("Fastest time:  " + "00:00:16.600000", smallText)
    textRect.center = (1280//2, (100+(720//2)) )
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects("Hours : Minutes : Seconds.Milliseconds", smallText)
    textRect.center = (1280//2, (150+(720//2)) )
    win.blit(textSurf, textRect)
    pygame.display.update()
    qwerty = True
    print(str(timedelta(seconds=timetocomplete2)))
    while qwerty:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #un-init pygame modules
                pygame.quit()
                #sys exit
                sys.exit()
                #noob exit
                quit()
        #part of finding what key your pressing
        keys = pygame.key.get_pressed()
        #key to go left
        if keys[pygame.K_RETURN]:
            fade_out(1280, 720)
            name()
#2p test
def game_loop_2p():
    pygame.mouse.set_visible(False)
    gcache = globals()
    cache = str(sys.getsizeof(gcache))
    print('Global cache: ' + cache)
    print('2 player. WARNING: UNFINISHED. BASICALLY A SNAPSHOT FROM WHEN IT WAS IMPLEMENTED')
    global luigi2
    luigi2 = True
    print(luigi2)
    jah = True
    #music jah
    music = pygame.mixer.music.load('audio/music.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    while jah:
        #p2 of frame limiter
        clock.tick(27)
        #check whether closed to allow for safe quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gcache = globals()
                cache = str(sys.getsizeof(gcache))
                print('Final Cache: ' + cache)
                #un-init pygame modules
                pygame.quit()
                #sys exit
                sys.exit()
                #python exit
                quit()
        #part of finding what key your pressing
        keys = pygame.key.get_pressed()
        #key to go left
        if keys[pygame.K_a] and mario.x > mario.vel:
            if keys[pygame.K_LSHIFT]:
                mario.vel = 10
                mario.x -= mario.vel
                mario.left = True
                mario.right = False
            else:
                mario.vel = 5
                mario.x -= mario.vel
                mario.left = True
                mario.right = False
        #key to go right
        elif keys[pygame.K_d] and mario.x < 1280 - mario.vel - mario.width:
            if keys[pygame.K_LSHIFT]:
                mario.vel = 10
                mario.x += mario.vel
                mario.left = False
                mario.right = True
            else:
                mario.vel = 5
                mario.x += mario.vel
                mario.left = False
                mario.right = True

        #part of direction facing
        else: 
            mario.left = False
            mario.right = False
            mario.walkCount = 0
        #jumping
        if not(mario.isJump):
            if keys[pygame.K_SPACE]:
                jumpsnd.play()
                mario.isJump = True
                mario.left = False
                mario.right = False
                mario.walkCount = 0
        #arc of falling
        else:
            if mario.jumpCount >= -10:
                #quadratics reeeee
                #the abs makes the negative positive and the positive positive
                #w/o abs, charcater jumps to peak, and then goes up again, instead of down
                mario.y -= (mario.jumpCount * abs(mario.jumpCount)) * 0.4
                mario.jumpCount -= 1
            else: 
                mario.jumpCount = 10
                mario.isJump = False
        # --------------------------------------------------------------------
        if keys[pygame.K_LEFT] and luigi.x > luigi.vel:
            if keys[pygame.K_LSHIFT]:
                luigi.vel = 10
                luigi.x -= luigi.vel
                luigi.left = True
                luigi.right = False
            else:
                luigi.vel = 5
                luigi.x -= luigi.vel
                luigi.left = True
                luigi.right = False
        #key to go right
        elif keys[pygame.K_RIGHT] and luigi.x < 1280 - luigi.vel - luigi.width:
            if keys[pygame.K_LSHIFT]:
                luigi.vel = 10
                luigi.x += luigi.vel
                luigi.left = False
                luigi.right = True
            else:
                luigi.vel = 5
                luigi.x += luigi.vel
                luigi.left = False
                luigi.right = True
        #part of direction facing
        else: 
            luigi.left = False
            luigi.right = False
            luigi.walkCount = 0
        #jumping
        if not(luigi.isJump):
            if keys[pygame.K_UP]:
                jumpsnd.play()
                luigi.isJump = True
                luigi.left = False
                luigi.right = False
                luigi.walkCount = 0
        #arc of falling
        else:
            if luigi.jumpCount >= -10:
                #quadratics reeeee
                #the abs makes the negative positive and the positive positive
                #w/o abs, charcater jumps to peak, and then goes up again, instead of down
                luigi.y -= (luigi.jumpCount * abs(luigi.jumpCount)) * 0.4
                luigi.jumpCount -= 1
            else: 
                luigi.jumpCount = 10
                luigi.isJump = False
        #redraw game window
        redrawGameWindow()
if __name__ == '__main__':
    fade_out(1280,720)
    #score_tally()
    name()
    #game_loop_1p()
    #game_lvl2()
    #game_lvl3()
    #game_lvl4()
    #cutscene()
#cya mate
pygame.quit()
sys.exit

#Type Master
#Program to help memorize the type chart for Pokemon
#Created by Pierce Renio and Manuel Morales

import pygame, random, TypeMatchups, TypeEffectiveness
from Type import Type
from pygame.locals import (
    K_ESCAPE,
    QUIT,
    KEYDOWN,
    MOUSEBUTTONUP
)

pygame.init()
pygame.font.init()

#Setting colors
color_white = (255,255,255)
color_black = (0,0,0)
color_light = (170,170,170)
def make_darker(color):
    color_1 = color[0]*(2/3)
    color_2 = color[1]*(2/3)
    color_3 = color[2]*(2/3)
    return (color_1,color_2,color_3)


#Setting basis for screen
screen = pygame.display.set_mode([700,700])

pygame.display.set_caption('Type Master')

width = screen.get_width()
height = screen.get_height()

qb_start =width/(4/3)
hb_start = width-(qb_start)-160
nb_start = hb_start+160+(width/(4/3)-(width-(width/(4/3)))-160)/2
b1_start, b2_start = width*.1, width*.6
b3_start,b4_start = width*.1, width*.6


smallfont = pygame.font.SysFont('Corbel',50)
text = smallfont.render('Quit' , True , color_white)
fontXL = pygame.font.SysFont('timesnewroman', 75)
fontL = pygame.font.SysFont('timesnewroman', 30)
fontS = pygame.font.SysFont('timesnewroman', 17)


#Creating all the types
labels = {0:"Typeless", 1:"Normal", 2:"Fighting", 3:"Flying", 4:"Poison", 5:"Ground", 6:"Rock", 7:"Bug", 8:"Ghost", 9:"Steel", 10:"Fire", 11:"Water", 12:"Grass", 13:"Electric", 14:"Psychic", 15:"Ice", 16:"Dragon", 17:"Dark", 18:"Fairy"}
typeList = []
i = 0
while i <= 18:
    advantageList = TypeMatchups.Type_Matchups(i)
    typeList.append(Type(advantageList, i))

    i += 1

#Setting up the lists for the types (b=battling,d=defending)
b = []
e = []
b1=0
b2=0
b3=0
b4=0
d1=0
d2=0

#Randomizes all the types, both attacking and defending
def randomizeTypes():
    same_b = True
    same_d = True
    while same_b == True:
        b1 = random.randint(1,18)
        b2 = random.randint(1,18)
        b3 = random.randint(1,18)
        b4 = random.randint(1,18)
        #This if statement is here because there is no Pokemon that have 2 of the same type.
        #Types must be different.
        if b1==b2 or b1==b3 or b1==b4 or b2==b3 or b2==b4 or b3==b4:
            same_b = True
        else:
            same_b = False

    while same_d == True:
        d1 = random.randint(0,18)
        d2 = random.randint(0,18)
        if d1 == d2:
            same_d = True
        #This else is here because if the first type is "Typeless", switch the type spots.
        #Pokemon never have "Typeless" as their first type.
        else:
            same_d = False
            if d1 == 0:
                d1 = d2
                d2 = 0
    
    print([d1,d2])
    print(typeList[d1].name + " and " + typeList[d2].name)

    print("")

    return b1,b2,b3,b4,d1,d2

#Checks to see how effective each attacking move is against the defending type
def overall_checker(b,d):
    i, j, k = 0,0,0
    lst1 = []
    lst2 = []
    lst3 = []
    while i <= 3:
        lst1.append(d[0][labels[b[i]]])
        i += 1
    while j <= 3:
        lst2.append(d[1][labels[b[j]]])
        j += 1
    while k <= 3:
        lst3.append(lst1[k]*lst2[k])
        k += 1
    return lst3

#Checks to see if the guess being made was correct, wrong, or if there was another correct option.
def guess_checker(guess,effectiveness_result):
    global streak
    if effectiveness_result[guess] == max(effectiveness_result):
        if effectiveness_result.count(effectiveness_result[guess]) > 1:
            return "You picked one of the right types!"
        else:
            return "You picked the right type!"
    else:
        streak = 0
        return "There was a better option..."

#Creates the variables for the result texts
def textCreation():
    return (typeText(bNames[0],dNames,de),typeText(bNames[1],dNames,de),typeText(bNames[2],dNames,de),typeText(bNames[3],dNames,de))

#Returns text for the results screen
def typeText(name,dNames,d):
    effect1 = ""
    effect2 = "" 

    if de[0][name] == 0.5:
        effect1 = " is not very effective against "
    elif de[0][name] == 1:
        effect1 =" is neutral against "
    elif de[0][name] == 2:
        effect1 =" is super effective against "
    elif de[0][name] == 0:
        effect1 = " has no effect against "

    if de[1][name] == 0.5:
        effect2 = " is not very effective against "
    elif de[1][name] == 1:
        effect2 =" is neutral against "
    elif de[1][name] == 2:
        effect2 =" is super effective against "
    elif de[1][name] == 0:
        effect2 = " has no effect against "

    if d2 == 0:
        return (name +  effect1  + dNames[0])
    else:
        return (name +  effect1  + dNames[0] + " and" + effect2  + dNames[1])



#--------------------------------------------------------------------------------------------------------
#Setting up game loops
running = True
next_present = False
type_present = False
start_present = True
streak_present = False
buttons_present = False
streak = None
results_screen = False
home_screen = True
guess = None
while True:

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:



#Event for quit button
            if qb_start <= mouse[0] <= qb_start+160 and height/1.2 <= mouse[1] <= height/1.2+60:
                pygame.quit()

#Event for next button
            if next_present == True:
                if nb_start <= mouse[0] <= nb_start+160 and height/1.2 <= mouse[1] <= height/1.2+60:
                    print("Next round!\n")
                    type_present = True
                    next_present = False
                    results_screen= False
                    buttons_present = True
                    b1,b2,b3,b4,d1,d2 = randomizeTypes()
                    b = [b1,b2,b3,b4]
                    d = [d1,d2]
                    de = [typeList[d1].effectiveness,typeList[d2].effectiveness]

                    print(b)

                    bNames = [typeList[b1].name,typeList[b2].name,typeList[b3].name,typeList[b4].name]
                    dNames = [typeList[d1].name,typeList[d2].name]

                    print(bNames)
                    print("\n")

                    print(de)
                    effectiveness_result = overall_checker(b,de)
                    print(effectiveness_result)
                    print("")


#Event for start button
            if start_present == True:
                if nb_start <= mouse[0] <= nb_start+160 and height/1.2 <= mouse[1] <= height/1.2+60:
                    print("Start!\n")
                    home_screen = False
                    start_present = False
                    type_present = True
                    buttons_present = True
                    streak = 0
                    streak_present = True
                    b1,b2,b3,b4,d1,d2 = randomizeTypes()
                    b = [b1,b2,b3,b4]
                    d = [d1,d2]
                    de = [typeList[d1].effectiveness,typeList[d2].effectiveness]

                    print(b)

                    bNames = [typeList[b1].name,typeList[b2].name,typeList[b3].name,typeList[b4].name]
                    dNames = [typeList[d1].name,typeList[d2].name]

                    print(bNames)
                    print("\n")

                    print(de)
                    effectiveness_result = overall_checker(b,de)
                    print(effectiveness_result)
                    print("")

#Event for home button
            if hb_start <= mouse[0] <= hb_start+160 and height/1.2 <= mouse[1] <= (height/1.2+60):
                print("Home\n")
                next_present = False
                type_present = False
                start_present = True
                streak_present = False
                results_screen = False
                buttons_present = False
                home_screen = True

#Event for type buttons
            if buttons_present == True:
                if b1_start <= mouse[0] <= b1_start+200 and height*.35 <= mouse[1] <= (height*.35)+125:
                    guess = 0
                    print(guess_checker(guess,effectiveness_result))
                    next_present = True
                    type_present = False
                    start_present = False
                    results_screen = True
                    buttons_present = False
                    txt1, txt2, txt3, txt4 = textCreation()
                    streak += 1


                if b2_start <= mouse[0] <= b2_start+200 and height*.35 <= mouse[1] <= (height*.35)+125:
                    guess = 1
                    print(guess_checker(guess,effectiveness_result))
                    next_present = True
                    type_present = False
                    start_present = False
                    results_screen = True
                    buttons_present = False
                    txt1, txt2, txt3, txt4 = textCreation()
                    streak += 1

                if b3_start <= mouse[0] <= b3_start+200 and height*.55 <= mouse[1] <= (height*.55)+125:
                    guess = 2
                    print(guess_checker(guess,effectiveness_result))
                    next_present = True
                    type_present = False
                    start_present = False
                    results_screen = True
                    buttons_present = False
                    txt1, txt2, txt3, txt4 = textCreation()
                    streak += 1

                if b4_start <= mouse[0] <= b4_start+200 and height*.55 <= mouse[1] <= (height*.55)+125:
                    guess = 3
                    print(guess_checker(guess,effectiveness_result))
                    next_present = True
                    type_present = False
                    start_present = False
                    results_screen = True
                    buttons_present = False
                    txt1, txt2, txt3, txt4 = textCreation()
                    streak += 1


#Setting the border for the game
    screen.fill(color_white)
    pygame.draw.lines(screen, color_black, False, [(0,height/1.3),(width,height/1.3)],5)

#Displaying the results screen
    if results_screen:
        resultText = fontL.render(guess_checker(guess,effectiveness_result), True, color_black, color_white)
        resultRect = text.get_rect()
        resultRect.center = (width*.35,height*.3)
       
        b1Text = fontS.render(txt1, True, color_black, color_white)
        b1TextRect = text.get_rect()
        b1TextRect.center = (width*.22,height*.4)

        b2Text = fontS.render(txt2, True, color_black, color_white)
        b2TextRect = text.get_rect()
        b2TextRect.center = (width*.22,height*.5)

        b3Text = fontS.render(txt3, True, color_black, color_white)
        b3TextRect = text.get_rect()
        b3TextRect.center = (width*.22,height*.6)

        b4Text = fontS.render(txt4, True, color_black, color_white)
        b4TextRect = text.get_rect()
        b4TextRect.center = (width*.22,height*.7)


        b1Number = fontL.render(str(de[0][bNames[0]]) + "       x       " + str(de[1][bNames[0]]) + "     =     " + str(de[0][bNames[0]]*de[1][bNames[0]]), True, color_black, color_white)
        b1NumberRect = text.get_rect()
        b1NumberRect.center = (width*.4, height*.44)

        b2Number = fontL.render(str(de[0][bNames[1]]) + "       x       " + str(de[1][bNames[1]]) + "     =     " + str(de[0][bNames[1]]*de[1][bNames[1]]), True, color_black, color_white)
        b2NumberRect = text.get_rect()
        b2NumberRect.center = (width*.4, height*.54)

        b3Number = fontL.render(str(de[0][bNames[2]]) + "       x       " + str(de[1][bNames[2]]) + "     =     " + str(de[0][bNames[2]]*de[1][bNames[2]]), True, color_black, color_white)
        b3NumberRect = text.get_rect()
        b3NumberRect.center = (width*.4, height*.64)

        b4Number = fontL.render(str(de[0][bNames[3]]) + "       x       " + str(de[1][bNames[3]]) + "     =     " + str(de[0][bNames[3]]*de[1][bNames[3]]), True, color_black, color_white)
        b4NumberRect = text.get_rect()
        b4NumberRect.center = (width*.4, height*.74)


        b1Result = pygame.image.load(TypeEffectiveness.returnImage(typeList[b1].name))
        b1Result = pygame.transform.scale(b1Image, (100,50))

        b2Result = pygame.image.load(TypeEffectiveness.returnImage(typeList[b2].name))
        b2Result = pygame.transform.scale(b2Image, (100,50))

        b3Result = pygame.image.load(TypeEffectiveness.returnImage(typeList[b3].name))
        b3Result = pygame.transform.scale(b3Image, (100,50))

        b4Result = pygame.image.load(TypeEffectiveness.returnImage(typeList[b4].name))
        b4Result = pygame.transform.scale(b4Image, (100,50))

        screen.blit(resultText,resultRect)

        screen.blit(b1Text, b1TextRect)
        screen.blit(b2Text, b2TextRect)
        screen.blit(b3Text, b3TextRect)
        screen.blit(b4Text, b4TextRect)
        screen.blit(b1Number,b1NumberRect)
        screen.blit(b2Number,b2NumberRect)
        screen.blit(b3Number,b3NumberRect)
        screen.blit(b4Number,b4NumberRect)

        screen.blit(b1Result,(5,height*.35))
        screen.blit(b2Result,(5,height*.45))
        screen.blit(b3Result,(5,height*.55))
        screen.blit(b4Result,(5,height*.65))
        screen.blit(d1Image,(width*.1875,height*.05))
        screen.blit(d2Image,(width*.5125,height*.05))




   
###################################################################################################################
##################################     BUTTONS FOR MAIN MENU ON BOTTOM     ########################################
###################################################################################################################

 
    mouse = pygame.mouse.get_pos()

#Button for quit
    if qb_start <= mouse[0] <= qb_start+160 and height/1.2 <= mouse[1] <= height/1.2+60:
        pygame.draw.rect(screen,color_light,[qb_start,height/1.2,160,60])
    else:
        pygame.draw.rect(screen,make_darker(color_light),[qb_start,height/1.2,160,60])


#Button for next
    if next_present == True:
        if nb_start <= mouse[0] <= nb_start+160 and height/1.2 <= mouse[1] <= height/1.2+60:
            pygame.draw.rect(screen,color_light,[nb_start,height/1.2,160,60]) 
        else:
            pygame.draw.rect(screen,make_darker(color_light),[nb_start,height/1.2,160,60])


#Button for start
    if start_present == True:
        if nb_start <= mouse[0] <= nb_start+160 and height/1.2 <= mouse[1] <= height/1.2+60:
            pygame.draw.rect(screen,color_light,[nb_start,height/1.2,160,60]) 
        else:
            pygame.draw.rect(screen,make_darker(color_light),[nb_start,height/1.2,160,60])

#Button for type buttons
    if type_present == True:
        b1Image = pygame.image.load(TypeEffectiveness.returnImage(typeList[b1].name))
        b1Image = pygame.transform.scale(b1Image, (200,125))

        if b1_start <= mouse[0] <= b1_start+200 and height*.35 <= mouse[1] <= (height*.35)+125:
            moveb1 = True
        else:
            moveb1 = False

        b2Image = pygame.image.load(TypeEffectiveness.returnImage(typeList[b2].name))
        b2Image = pygame.transform.scale(b2Image, (200,125))

        if b2_start <= mouse[0] <= b2_start+200 and height*.35 <= mouse[1] <= (height*.35)+125:
            moveb2 = True
        else:
            moveb2 = False

        b3Image = pygame.image.load(TypeEffectiveness.returnImage(typeList[b3].name))
        b3Image = pygame.transform.scale(b3Image, (200,125))

        if b3_start <= mouse[0] <= b3_start+200 and height*.55 <= mouse[1] <= (height*.55)+125:
            moveb3 = True
        else:
            moveb3 = False

        b4Image = pygame.image.load(TypeEffectiveness.returnImage(typeList[b4].name))
        b4Image = pygame.transform.scale(b4Image, (200,125))

        if b4_start <= mouse[0] <= b4_start+200 and height*.55 <= mouse[1] <= (height*.55)+125:
            moveb4 = True
        else:
            moveb4 = False


    #Button for home
    if hb_start <= mouse[0] <= hb_start+160 and height/1.2 <= mouse[1] <= (height/1.2+60):
        pygame.draw.rect(screen,color_light,[hb_start,height/1.2,160,60]) 
    else:
        pygame.draw.rect(screen,make_darker(color_light),[hb_start,height/1.2,160,60])


###################################################################################################################
###################################     BUTTONS FOR GAME WHEN STARTED     #########################################
###################################################################################################################

#Buttons for home,next,and quit
    screen.blit(text,(width/(1.244),height/1.18))
    screen.blit(smallfont.render('Home' , True , color_white),((width-(width/1.244)-105),height/1.18))
    if next_present == True:
        screen.blit(smallfont.render('Next' , True , color_white),(nb_start+35,height/1.18))

    if start_present == True:
            screen.blit(smallfont.render('Start' , True , color_white),(nb_start+33,height/1.18))
  


#Buttons and jpgs for the types
    if type_present == True:
        if moveb1:
            screen.blit(b1Image,(width*.1+7,height*.35-7))
        else:
            screen.blit(b1Image,(width*.1,height*.35))
        if moveb2:
            screen.blit(b2Image,(width*.6+7,height*.35-7))
        else:
            screen.blit(b2Image,(width*.6,height*.35))
        if moveb3:
            screen.blit(b3Image,(width*.1+7,height*.55-7))
        else:
            screen.blit(b3Image,(width*.1,height*.55))
        if moveb4:
            screen.blit(b4Image,(width*.6+7,height*.55-7))
        else:
            screen.blit(b4Image,(width*.6,height*.55))

        d1Image = pygame.image.load(TypeEffectiveness.returnImage(typeList[d1].name))
        d1Image = pygame.transform.scale(d1Image, (200,125))
        screen.blit(d1Image,(width*.1875,height*.05))
        d2Image = pygame.image.load(TypeEffectiveness.returnImage(typeList[d2].name))
        d2Image = pygame.transform.scale(d2Image, (200,125))
        screen.blit(d2Image,(width*.5125,height*.05))


#Text for the home screen
    if home_screen == True:
        homeText = fontXL.render("Type Master", True, color_black, color_white)
        homeTextRect = text.get_rect()
        homeTextRect.center = (width*.3,height*.1)

        descriptionText1 = fontL.render("Pick the best move based on type advantage!", True, color_black, color_white)
        descriptionTextRect1 = text.get_rect()
        descriptionTextRect1.center = (width*.19,height*.3)

        descriptionText2 = fontL.render("There might be more than one correct answer!", True, color_black, color_white)
        descriptionTextRect2 = text.get_rect()
        descriptionTextRect2.center = (width*.175,height*.4)

        descriptionText3 = fontL.render("means Typeless!", True, color_black, color_white)
        descriptionTextRect3 = text.get_rect()
        descriptionTextRect3.center = (width*.55 ,height*.6)

        typelessImage = pygame.image.load('Type Labels\\typeless.jpg')
        typelessImage = pygame.transform.scale(typelessImage, (200,125))


        screen.blit(homeText,homeTextRect)
        screen.blit(descriptionText1,descriptionTextRect1)
        screen.blit(descriptionText2,descriptionTextRect2)
        screen.blit(descriptionText3,descriptionTextRect3)
        screen.blit(typelessImage, (130,350))


#Text for streak
    if streak_present:
        streakText = fontL.render("Streak: " + str(0), True, color_black, color_white)
        streakText = fontL.render("Streak: " + str(streak), True, color_black, color_white)
        streakRect = text.get_rect()
        streakRect.center = (width*.075,height*.05)

        screen.blit(streakText,streakRect)

    pygame.display.update()








































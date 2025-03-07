from tkinter import*    #imports tkinter to be used in GUI
import time             #imports time to slow down code, more user friendly
import random           #imports random, allowing for true shuffle of deck
import os               #imports os incase needed to interact with Operating System

global tk
tk = Tk()
global canvas
    
class Cards():
    def __init__(self, inv1, inv2, inv3, inv4, inv5):
        self.inv1 = inv1            #sets inventory for class to player inventory
        self.inv2 = inv2            #sets inventory for class to ai1 inventory
        self.inv3 = inv3            #sets inventory for class to ai2 inventory
        self.inv4 = inv4            #sets inventory for class to dealer inventory
        self.inv5 = inv5            #sets inventory for class for the player split inventory
        
        
    def deckingCards(self):
        self.deckOfCards = []                                                       #clears the deck of cards to nothing
        for i in range (0,4):                                                       #sets the amount of decks to be used to 4
            for each in ["h","d","s","c"]:                                          #assigns a house to each card
                for value in ['a','2','3','4','5','6','7','8','9','0','j','q','k']: #assigns a value to each card
                    self.card = [each,value]                                        #combines house and value to create card
                    self.deckOfCards.append(self.card)                              #adds card to the deck
        random.shuffle(self.deckOfCards)                                            #shuffles the deck so is random order
        return self.deckOfCards                                                     #returns deck to main code
    
    def showCardsai1(self, inv2):
        print("This is showCards method")
        x2 = 1250                                                                           #sets the x coordinate for the first card in A1 inv
        x3 = 45                                                                             #sets the x coordinate for the first card in AI2 inv
        time.sleep(0.5)                                                                     #adds a timed break into the code to improve visuals
        self.inv2Card1_img = PhotoImage(file="playingCards/"+str(self.inv2[0])+".png")      #sets the image to be inserted from playingCards subfolder to be the first card in A1 inv
        backG.create_image(x2, 575, image=self.inv2Card1_img, anchor=NW)                    #places image on the canvas
        time.sleep(0.5)                                                                     #adds a timed break into the code to improve visuals
        tk.update()
        x2= x2+95                                                                           #moves the x coordinates so next image wont be overlapping
        self.inv2Card2_img = PhotoImage(file="playingCards/"+str(self.inv2[1])+".png")      #sets the image to be inserted to be the next card in A1 inv
        backG.create_image(x2, 575, image=self.inv2Card2_img, anchor=NW)                    #places image on the canvas
        tk.update()
        if len(self.inv2)>=3:                                                               #if the length of inv is over 3 then adds the 3rd card to be shown
            time.sleep(0.5)                                                                 #adds a timed break into the code to improve visuals
            x2= x2+95                                                                       #moves the x coordinates so next image wont be overlapping
            self.inv2Card3_img = PhotoImage(file="playingCards/"+str(self.inv2[2])+".png")  #sets the image to be inserted from playingCards subfolder to be the next card in A1 inv
            backG.create_image(x2, 575, image=self.inv2Card3_img, anchor=NW)                #places image on the canvas
            tk.update()
        if len(self.inv2)>=4:                                                               #if the length of inv is over 4 then adds the 4th card to be shown
            time.sleep(0.5)                                                                 #adds a timed break into the code to improve visuals
            x2= x2+95                                                                       #moves the x coordinates so next image wont be overlapping
            self.inv2Card4_img = PhotoImage(file="playingCards/"+str(self.inv2[3])+".png")  #sets the image to be inserted from playingCards subfolder to be the next card in A1 inv
            backG.create_image(x2, 575, image=self.inv2Card4_img, anchor=NW)                #places image on the canvas
            tk.update()
        if len(self.inv2)>=5:                                                               #if the length of inv is over 5 then adds the 5th card to be shown
            time.sleep(0.5)                                                                 #adds a timed break into the code to improve visuals
            x2= x2+95                                                                       #moves the x coordinates so next image wont be overlapping
            self.inv2Card5_img = PhotoImage(file="playingCards/"+str(self.inv2[4])+".png")  #sets the image to be inserted from playingCards subfolder to be the next card in A1 inv
            backG.create_image(x2, 575, image=self.inv2Card5_img, anchor=NW)                #places image on the canvas
            tk.update()

        backG.pack()
        tk.update()
        
    def showCardsai2(self, inv3):
        x3 = 45
        self.inv3Card1_img = PhotoImage(file="playingCards/"+str(self.inv3[0])+".png")      #sets the image from playingCards subfolder to be inserted to the first card in AI2 inv
        backG.create_image(x3, 575, image=self.inv3Card1_img, anchor=NW)                    #places image on canvas
        tk.update()
        x3=x3+95                                                                            #moves the x coordinates so next image wont be overlapping
        time.sleep(0.5)                                                                     #adds a timed break into the code to improve visuals
        self.inv3Card2_img = PhotoImage(file="playingCards/"+str(self.inv3[1])+".png")      #sets the image from playingCards subfolder to be inserted to the next card in AI2 inv
        backG.create_image(x3, 575, image=self.inv3Card2_img, anchor=NW)                    #places image on canvas
        tk.update()
        time.sleep(0.5)                                                                     #adds a timed break into the code to improve visuals
        if len(self.inv3)>=3:                                                               #if the length of inv is over 3 then adds the 3th card to be shown
            time.sleep(0.5)                                                                 #adds a timed break into the code to improve visuals
            x3= x3+95                                                                       #moves the x coordinates so next image wont be overlapping
            self.inv3Card3_img = PhotoImage(file="playingCards/"+str(self.inv3[2])+".png")  #sets the image from playingCards subfolder to be inserted to the next card in AI2 inv
            backG.create_image(x3, 575, image=self.inv3Card3_img, anchor=NW)                #places image on canvas
            tk.update()
        if len(self.inv3)>=4:                                                               #if the length of inv is over 4 then adds the 4th card to be shown
            time.sleep(0.5)                                                                 #adds a timed break into the code to improve visuals
            x3= x3+95                                                                       #moves the x coordinates so next image wont be overlapping
            self.inv3Card4_img = PhotoImage(file="playingCards/"+str(self.inv3[3])+".png")  #sets the image from playingCards subfolder to be inserted to the next card in AI2 inv
            backG.create_image(x3, 575, image=self.inv3Card4_img, anchor=NW)                #places image on canvas
            tk.update()
        if len(self.inv3)>=5:                                                               #if the length of inv is over 5 then adds the 5th card to be shown
            time.sleep(0.5)                                                                 #adds a timed break into the code to improve visuals
            x3= x3+95                                                                       #moves the x coordinates so next image wont be overlapping
            self.inv3Card5_img = PhotoImage(file="playingCards/"+str(self.inv3[4])+".png")  #sets the image from playingCards subfolder to be inserted to the next card in AI2 inv
            backG.create_image(x3, 575, image=self.inv3Card5_img, anchor=NW)                #places image on canvas
            tk.update()
    
    def showPCards(self,inv1):
        x1 = 645
        tk.update()
        self.inv1Card1_img = PhotoImage(file="playingCards/"+str(self.inv1[0])+".png")      #sets the image from playingCards subfolder to be inserted to the first card in player inv
        backG.create_image(x1, 575, image = self.inv1Card1_img, anchor=NW)                  #places image on canvas
        tk.update()
        time.sleep(0.5)                                                                     #adds a timed break into the code to improve visuals
        x1=x1+95                                                                            #moves the x coordinates so next image wont be overlapping
        self.inv1Card2_img = PhotoImage(file="playingCards/"+str(self.inv1[1])+".png")      #sets the image from playingCards subfolder  to be inserted to be the next card in player inv
        backG.create_image(x1, 575, image = self.inv1Card2_img, anchor=NW)                  #places image on the canvas
        tk.update()
        if len(self.inv1)>=3:
            time.sleep(0.5)                                                                 #adds a timed break into the code to improve visuals
            x1= x1+95                                                                       #moves the x coordinates so next image wont be overlapping
            self.inv1Card3_img = PhotoImage(file="playingCards/"+str(self.inv1[2])+".png")  #sets the image from playingCards subfolder  to be inserted to be the next card in player inv
            backG.create_image(x1, 575, image=self.inv1Card3_img, anchor=NW)                #places image on the canvas
            tk.update()
        if len(self.inv1)>=4:
            time.sleep(0.5)                                                                 #adds a timed break into the code to improve visuals
            x1= x1+95                                                                       #moves the x coordinates so next image wont be overlapping
            self.inv1Card4_img = PhotoImage(file="playingCards/"+str(self.inv1[3])+".png")  #sets the image from playingCards subfolder  to be inserted to be the next card in player inv
            backG.create_image(x1, 575, image=self.inv1Card4_img, anchor=NW)                #places image on the canvas
            tk.update()
        if len(self.inv1)>=5:
            time.sleep(0.5)                                                                 #adds a timed break into the code to improve visuals
            x1= x1+95                                                                       #moves the x coordinates so next image wont be overlapping
            self.inv1Card5_img = PhotoImage(file="playingCards/"+str(self.inv1[4])+".png")  #sets the image from playingCards subfolder  to be inserted to be the next card in player inv
            backG.create_image(x1, 575, image=self.inv1Card5_img, anchor=NW)                #places image on the canvas
            tk.update()
        
        
    def dealerCards(self, inv4, hidden):
        x4 = 1030
        self.inv4 = inv4
        if hidden == True:#if the card needs to be hidden
            self.inv4Card1_img = PhotoImage(file="playingCards/BackOfCard90p.png")          #opens subfolder playingCards and opens back of card imahe
            backG.create_image(x4, 65, image=self.inv4Card1_img, anchor=NW)                 #places image on the canvas
        elif hidden == False:#if the card doesnt need to be hidden
            self.inv4Card1_img = PhotoImage(file="playingCards/"+str(self.inv4[0])+".png")  #opens subfolder playing card and opens the image of card needed
            backG.create_image(x4, 65, image=self.inv4Card1_img, anchor=NW)                 #places image on the canvas
            tk.update()
        x4=x4-95                                                                            #moves x coordinate so images wont overlap
        time.sleep(0.5)                                                                     #added a timed break to improve on visuals
        self.inv4Card2_img = PhotoImage(file="playingCards/"+str(self.inv4[1])+".png")      #sets the image from sub folder playingCards to be inserted to be the next card in dealer inv
        backG.create_image(x4, 65, image=self.inv4Card2_img, anchor=NW)                     #places image on the canvas
        tk.update()
        if len(self.inv4)>=3:#if inv4 length greater then 3
            time.sleep(0.5)                                                                 #adds a timed break into the code to improve visuals
            x4= x4-95                                                                       #moves the x coordinates so next image wont be overlapping
            self.inv4Card3_img = PhotoImage(file="playingCards/"+str(self.inv4[2])+".png")  #sets the image from sub folder playingCards to be inserted to be the next card in dealer inv
            backG.create_image(x4, 65, image=self.inv4Card3_img, anchor=NW)                 #places image on the canvas
            tk.update()
        if len(self.inv4)>=4:#if inv4 length greater then 4
            time.sleep(0.5)                                                                 #adds a timed break into the code to improve visuals
            x4= x4-95                                                                       #moves the x coordinates so next image wont be overlapping
            self.inv4Card4_img = PhotoImage(file="playingCards/"+str(self.inv4[3])+".png")  #sets the image from sub folder playingCards to be inserted to be the next card in dealer inv
            backG.create_image(x4, 65, image=self.inv4Card4_img, anchor=NW)                 #places image on the canvas
            tk.update()
        if len(self.inv4)>=5:#if inv4 length greater then 5
            time.sleep(0.5)                                                                 #adds a timed break into the code to improve visuals
            x4= x4-95                                                                       #moves the x coordinates so next image wont be overlapping
            self.inv4Card5_img = PhotoImage(file="playingCards/"+str(self.inv4[4])+".png")  #sets the image from sub folder playingCards to be inserted to be the next card in dealer inv
            backG.create_image(x4, 65, image=self.inv4Card5_img, anchor=NW)                 #places image on the canvas
            tk.update()
            
    def showSplitP(self, inv1, inv5):
        y1 = 575#sets y coordinate
        tk.update()
        self.inv1 = inv1
        self.inv1Card1_img = PhotoImage(file="playingCards/"+str(self.inv1[0])+".png")      #sets the image from sub folder playingCards to be inserted to be the first card in player inv
        backG.create_image(645, y1, image = self.inv1Card1_img, anchor=NW)                  #places image
        tk.update()
        if len(self.inv1)>=2:#if length of inv1 is greater then 2
            y1=y1-55                                                                        #moves the y coordinates so next image wont be overlapping
            self.inv1Card2_img = PhotoImage(file="playingCards/"+str(self.inv1[1])+".png")  #sets the image from sub folder playingCards to be inserted to be the next card in player inv
            backG.create_image(645, y1, image = self.inv1Card2_img, anchor=NW)              #places image on the canvas
            tk.update()
        if len(self.inv1)>=3:#if length of inv1 is greater then 3
            y1= y1-55                                                                       #moves the y coordinates so next image wont be overlapping
            self.inv1Card3_img = PhotoImage(file="playingCards/"+str(self.inv1[2])+".png")  #sets the image from sub folder playingCards to be inserted to be the next card in player inv
            backG.create_image(645, y1, image=self.inv1Card3_img, anchor=NW)                #places image on the canvas
            tk.update()
        if len(self.inv1)>=4:#if length of inv1 is greater then 4
            y1= y1-55                                                                       #moves the y coordinates so next image wont be overlapping
            self.inv1Card4_img = PhotoImage(file="playingCards/"+str(self.inv1[3])+".png")  #sets the image from sub folder playingCards to be inserted to be the next card in player inv
            backG.create_image(645, y1, image=self.inv1Card4_img, anchor=NW)                #places image on the canvas
            tk.update()
        if len(self.inv1)>=5:#if length of inv1 is greater then 5
            y1= y1-55                                                                       #moves the y coordinates so next image wont be overlapping
            self.inv1Card5_img = PhotoImage(file="playingCards/"+str(self.inv1[4])+".png")  #sets the image from sub folder playingCards to be inserted to be the next card in player inv
            backG.create_image(645, y1, image=self.inv1Card5_img, anchor=NW)                #places image on the canvas
            tk.update()


        y1 = 575#sets y coordinate
        tk.update()
        self.inv5Card1_img = PhotoImage(file="playingCards/"+str(self.inv5[0])+".png")      #opens sub folder playingCards and gets first card from inv image
        backG.create_image(1025, y1, image = self.inv5Card1_img, anchor=NW)                 #places image on canvas
        tk.update()
        if len(self.inv5)>=2:#if length of inv5 is greater then 2
            y1=y1-55                                                                        #moves the y coordinates so next image wont be overlapping
            self.inv5Card2_img = PhotoImage(file="playingCards/"+str(self.inv5[1])+".png")  #sets the image to be inserted to be the next card in inv5
            backG.create_image(1025, y1, image = self.inv5Card2_img, anchor=NW)             #places image on the canva
            tk.update()
        if len(self.inv5)>=3:#if length of inv5 is greater then 3
            y1= y1-55                                                                       #moves the y coordinates so next image wont be overlapping
            self.inv5Card3_img = PhotoImage(file="playingCards/"+str(self.inv5[2])+".png")  #sets the image from sub folder playingCards to be inserted to be the next card in inv5
            backG.create_image(1025, y1, image=self.inv5Card3_img, anchor=NW)               #places image on the canvas
            tk.update()
        if len(self.inv5)>=4:#if length of inv5 is greater then 4
            y1= y1-55                                                                       #moves the y coordinates so next image wont be overlapping
            self.inv5Card4_img = PhotoImage(file="playingCards/"+str(self.inv5[3])+".png")  #sets the image from sub folder playingCards to be inserted to be the next card in inv5
            backG.create_image(1025, y1, image=self.inv5Card4_img, anchor=NW)               #places image on the canvas
            tk.update()
        if len(self.inv5)>=5:#if length of inv5 is greater then 5                                                             
            y1= y1-55                                                                       #moves the y coordinates so next image wont be overlapping
            self.inv5Card5_img = PhotoImage(file="playingCards/"+str(self.inv5[4])+".png")  #sets the image from sub folder playingCards to be inserted to be the next card in inv5
            backG.create_image(1025, y1, image=self.inv5Card5_img, anchor=NW)               #places image on the canvas
            tk.update()
        

        
        
class aiCounting():#class used by first ai if undergoing counting procedure
    def __init__(self, inv1, inv2, inv3, inv4, runTotal_1, runTotal_2, deck, trueCount1, trueCount2, playedCardsAI1, playedCardsAI2):
        self.score = 0              #sets score used for counting to 0 
        self.inv1 = inv1            #sets inventory for class to player inventory
        self.inv2 = inv2            #sets inventory for class to ai1 inventory
        self.inv3 = inv3            #sets inventory for class to ai2 inventory
        self.inv4 = inv4            #sets inventory for class to dealer inventory
        self.runTotal_1 = runTotal_1#sets the runTotal 1 for ai1 counting         
        self.runTotal_2 = runTotal_2#sets the runTotal 2 for ai2 counting
        self.deck = deck            #sets deck for class to be current deck
        self.trueCount1 = trueCount1#sets the true count for ai1 to the current true count
        self.trueCount2 = trueCount2#sets the true count for ai2 to the current true count
        self.playedCardsAI1 = playedCardsAI1
        self.playedCardsAI2 = playedCardsAI2



        
    def counting1(self, c, inv1, inv2, inv3, inv4, deck, trueCount1, playedCards):  #counting strategy Hi-Lo
        print("hi-lo")
        for i in range(0,len(inv1)):                                                                                #for however many cards are in the players inv
            self.temp = self.inv1[i]                                                                                #puts one card from inv into a temporary attribute
            self.value = self.temp[1]                                                                               #finds the value of card from temporay attribute
            print(self.value)
            if self.value == 'q' or self.value =='k' or self.value =='j' or self.value =='0' or self.value == 'a':  #decreases the runTotal_1 value by 1 for each high value card
                self.runTotal_1 = self.runTotal_1 -1
                print("-1")
            elif int(self.value) <=6:                                                                               #increases the runTotal_1 value by 1 for each lower value card
                self.runTotal_1 = self.runTotal_1+1
                print("+1")
            print("run total 1:", self.runTotal_1)
                
        for i in range(0,len(inv2)):                                                                                #for however many cards are in the AI1 inv
            self.temp = self.inv2[i]                                                                                #puts one card from ai1 inv into a temporary attribute
            self.value = self.temp[1]                                                                               #finds the value of the card from the temporary attribute
            print(self.value)
            if self.value == 'q' or self.value =='k' or self.value =='j' or self.value =='0' or self.value == 'a':  #decreases the runTotal_1 value by 1 for each high value card
                self.runTotal_1 = self.runTotal_1 -1
                print("-1")
            elif int(self.value) <=6:                                                                               #increases the runTotal_1 value by 1 for each lower value card
                self.runTotal_1 = self.runTotal_1+1
                print("+1")
            print("run total 1:", self.runTotal_1)
        for i in range(0,len(inv3)):                                                                                #for however many cards are in the AI2 inv
            self.temp = self.inv3[i]                                                                                #puts one card from ai1 inv into a temporary attribute
            self.value = self.temp[1]                                                                               #finds the value of the card from the temporary attribute
            print(self.value)
            print(self.value)
            if self.value == 'q' or self.value =='k' or self.value =='j' or self.value =='0' or self.value == 'a':  #decreases the runTotal_1 value by 1 for each high value card
                print("-1")
                self.runTotal_1 = self.runTotal_1 -1
            elif int(self.value) <=6:                                                                               #increases the runTotal_1 value by 1 for each lower value card
                self.runTotal_1 = self.runTotal_1+1
                print("+1")
            print("run total 1:", self.runTotal_1)

        self.temp = self.inv4[1]                                                                                    #puts shown card from dealer into a temporary attribute
        self.value = self.temp[1]                                                                                   #finds the value of the card from the temporary attribute
        print(self.value)
        if self.value == 'q' or self.value =='k' or self.value =='j' or self.value =='0' or self.value == 'a':      #decreases the runTotal_1 value by 1 for each high value card
            print("-1")
            self.runTotal_1 = self.runTotal_1 -1
        elif int(self.value) <=6:                                                                                   #increases the runTotal_1 value by 1 for each lower value card
            self.runTotal_1 = self.runTotal_1+1
            print("+1")
        print("run total 1:", self.runTotal_1)

        self.trueCount1 = (self.runTotal_1/(len(self.deck)/52))                                                     #finds out the trueCount1 which can be used across all rounds to come
        print("number of decks remaining: ",len(self.deck)/52)
        print("running total: ", self.runTotal_1)
        print("true count: ", self.trueCount1)
        return self.trueCount1
        




    def counting2(self, c, inv1, inv2, inv3, inv4, deck, trueCount2):  #counting strategy halves
        print("halves")
        for i in range(0,len(inv1)):                                                                                #for however many cards are in the players inv
            self.temp = self.inv1[i]                                                                                #puts one card from player inv into a temporary attribute
            self.value = self.temp[1]                                                                               #finds the value of card from temproray attribute
            print(self.value)
            if self.value == 'q' or self.value =='k' or self.value =='j' or self.value =='0' or self.value == 'a':  #decreases the runTotal_2 value by 1 for each high value card
                self.runTotal_2 = self.runTotal_2-1
                print("-1")
            elif int(self.value) ==9:                                                                               #decreases the runTotal_2 value by 0.5 for each 9 card
                self.runTotal_2 = self.runTotal_2-0.5
                print("-0.5")
            elif int(self.value) ==7 or int(self.value) ==2:                                                        #increases the runTotal_2 value by 0.5 for each 2 or 7 card
                self.runTotal_2 = self.runTotal_2+0.5
                print("+0.5")
            elif int(self.value) == 3 or int(self.value) == 4 or int(self.value) == 6:                              #increases the runTotal_2 value by 1 for each 3, 4 or 6 card
                self.runTotal_2 = self.runTotal_2+1
                print("+1")
            elif int(self.value) ==5:                                                                               #increases the runTotal_2 valye by 1.5 for each 5 card
                self.runTotal_2 = self.runTotal_2+1.5
                print("+1.5")
            print("run total 2:",self.runTotal_2)
                
        for i in range(0,len(inv2)):                                                                                #for however many cards are in the AI1 inv
            self.temp = self.inv2[i]                                                                                #puts one card from ai1 inv into a temporary attribute
            self.value = self.temp[1]                                                                               #finds the value of card from temproray attribute
            print(self.value)
            if self.value == 'q' or self.value =='k' or self.value =='j' or self.value =='0' or self.value == 'a':  #decreases the runTotal_2 value by 1 for each high value card
                self.runTotal_2 = self.runTotal_2-1
                print("-1")
            elif int(self.value) ==9:                                                                               #decreases the runTotal_2 value by 0.5 for each 9 card
                self.runTotal_2 = self.runTotal_2-0.5
                print("-0.5")
            elif int(self.value) ==7 or int(self.value) ==2:                                                        #increases the runTotal_2 value by 0.5 for each 2 or 7 card
                self.runTotal_2 = self.runTotal_2+0.5
                print("+0.5")
            elif int(self.value) == 3 or int(self.value) == 4 or int(self.value) == 6:                              #increases the runTotal_2 value by 1 for each 3, 4 or 6 card
                self.runTotal_2 = self.runTotal_2+1
                print("+1")
            elif int(self.value) ==5:                                                                               #increases the runTotal_2 valye by 1.5 for each 5 card
                self.runTotal_2 = self.runTotal_2+1.5
                print("+1.5")

            print("run total 2:",self.runTotal_2)                
        for i in range(0,len(inv3)):                                                                                #for however many cards are in the AI2 inv
            print(self.inv3)
            self.temp = self.inv3[i]                                                                                #puts one card from ai2 inv into a temporary attribute
            self.value = self.temp[1]                                                                               #finds the value of card from temporary attribute
            print(self.value)
            if self.value == 'q' or self.value =='k' or self.value =='j' or self.value =='0' or self.value == 'a':  #decreases the runTotal_2 value by 1 for each high value card
                self.runTotal_2 = self.runTotal_2-1
                print("-1")
            elif int(self.value) ==9:                                                                               #decreases the runTotal_2 value by 0.5 for each 9 card
                self.runTotal_2 = self.runTotal_2-0.5
                print("-0.5")
            elif int(self.value) ==7 or int(self.value) ==2:                                                        #increases the runTotal_2 value by 0.5 for each 2 or 7 card
                self.runTotal_2 = self.runTotal_2+0.5
                print("+0.5")
            elif int(self.value) == 3 or int(self.value) == 4 or int(self.value) == 6:                              #increases the runTotal_2 value by 1 for each 3, 4 or 6 card
                self.runTotal_2 = self.runTotal_2+1
                print("+1")
            elif int(self.value) ==5:                                                                               #increases the runTotal_2 value by 1.5 for each 5 card
                self.runTotal_2 = self.runTotal_2+1.5
                print("+1.5")
                
        self.temp = self.inv4[1]                                                                                    #puts shown card from dealer into a temporary attribute
        self.value = self.temp[1]                                                                                   #finds the value of card from temporary attribute
        print(self.value)
        if self.value == 'q' or self.value =='k' or self.value =='j' or self.value =='0' or self.value == 'a':      #decreases the runTotal_2 value by 1 for each high value card
            self.runTotal_2 = self.runTotal_2-1
            print("-1")
        elif int(self.value) ==9:                                                                                   #decreases the runTotal_2 value by 0.5 for each 9 card
            self.runTotal_2 = self.runTotal_2-0.5
            print("-0.5")
        elif int(self.value) ==7 or int(self.value) ==2:                                                            #increases the runTotal_2 value by 0.5 for each 2 or 7 card
            self.runTotal_2 = self.runTotal_2+0.5
            print("+0.5")
        elif int(self.value) == 3 or int(self.value) == 4 or int(self.value) == 6:                                  #increases the runTotal_2 value by 1 for each 3, 4 or 6 card
            self.runTotal_2 = self.runTotal_2+1
            print("+1")
        elif int(self.value) ==5:                                                                                   #increases the runTotal_2 valye by 1.5 for each 5 card
            self.runTotal_2 = self.runTotal_2+1.5
            print("+1.5")
        self.trueCount2= (self.runTotal_2/(len(self.deck)/52))                                                      #finds trueCount2 which can be used across all rounds to come
        print("run total 2:",self.runTotal_2)
        print(self.trueCount2)
        return self.trueCount2
    
    def ai1EndgameCount(self, playedCardsAI1, trueCount1, deck):
        print("hilo")
        print(self.playedCardsAI1)
        for i in range(0, len(playedCardsAI1)):                                                                     #for length in array
            self.temp = self.playedCardsAI1[i]                                                                      #gets card from array
            self.value = self.temp[1]                                                                               #finds value from card
            print(self.value)
            if self.value == 'q' or self.value =='k' or self.value =='j' or self.value =='0' or self.value == 'a':  #decreases the runTotal_1 value by 1 for each high value card
                self.runTotal_1 = self.runTotal_1 -1
                print("-1")
            elif int(self.value) <=6:                                                                               #increases the runTotal_1 value by 1 for each lower value card
                self.runTotal_1 = self.runTotal_1+1
                print("+1")
        print(len(self.deck))
        print(self.runTotal_1)
        self.trueCount1 =(self.runTotal_1/(len(self.deck)/52))                                                      #finds out truecount by dividing total+run count by length of deck remaining
        return self.trueCount1


    
    def ai2EndgameCount(self, playedCardsAi2, trueCount2, deck):
        self.playedCardsAi2 = playedCardsAi2
        print("in ai2 endgame count")
        print(self.playedCardsAi2)
        for i in range(0, len(self.playedCardsAi2)):                                                                #for however many cards are in the AI2 inv
            self.temp = self.playedCardsAi2[i]                                                                      #puts one card from ai2 inv into a temporary attribute
            self.value = self.temp[1]                                                                               #finds the value of card from temporary attribute
            print(self.value)
            if self.value == 'q' or self.value =='k' or self.value =='j' or self.value =='0' or self.value == 'a':  #decreases the runTotal_2 value by 1 for each high value card
                self.runTotal_2 = self.runTotal_2-1
                print("-1")
            elif int(self.value) ==9:                                                                               #decreases the runTotal_2 value by 0.5 for each 9 card
                self.runTotal_2 = self.runTotal_2-0.5
                print("-0.5")
            elif int(self.value) ==7 or int(self.value) ==2:                                                        #increases the runTotal_2 value by 0.5 for each 2 or 7 card
                self.runTotal_2 = self.runTotal_2+0.5
                print("+0.5")
            elif int(self.value) == 3 or int(self.value) == 4 or int(self.value) == 6:                              #increases the runTotal_2 value by 1 for each 3, 4 or 6 card
                self.runTotal_2 = self.runTotal_2+1
                print("+1")
            elif int(self.value) ==5:                                                                               #increases the runTotal_2 value by 1.5 for each 5 card
                self.runTotal_2 = self.runTotal_2+1.5
                print("+1.5")
            print(len(self.deck))
            print(self.runTotal_2)
            self.trueCount2 =(self.runTotal_2/(len(self.deck)/52))                                                  #finds out truecount by dividing total+run count by length of deck remaining
            print(self.value, " ", self.runTotal_2, "", len(self.deck))
            
        return self.trueCount2

    def actions(self, value, aceCount, trueCount):#ai actions if counting enabled
        self.Hand = False#sets hand to false
        self.value = value#initialises value to class
        self.aceCount = aceCount# initialises aceCount to class
        self.trueCount = trueCount#initialises trueCount to class
        if self.value == 20:#if the ai has a value of 20
            self.state = "Stand"#ai will stand
        elif self.value == 19:#if ai has value of 19
            self.state = "Stand"#ai will stand
        elif self.value == 18:#if ai has value of 18
            self.state = "Stand"#ai will stand
        elif self.value == 17 and self.aceCount>0:#if ai has 17 and an ace
            self.state = "Hit"#ai will hit
        elif self.value == 17:#if ai has 17 and no ace
            self.state = "Stand"#ai will stand
        elif self.value == 16 and (self.trueCount<-1 or self.aceCount>0):#if ai has 16 and high chance of low card or owns an ace card
            self.state = "Hit"#ai will hit
        elif self.value == 16:#if ai has 16 and no ace or no high chance of low card
            self.state = "Stand"#ai will stand
        elif self.value == 15 and (self.trueCount<-0.5 or self.aceCount>0):#if ai has 15 and high chance of low card or owns an ace card
            self.state = "Hit"#ai will hit
        elif self.value == 11:#if ai is at 11
            self.state = "Double Down"#ai will double down
        elif self.value == 10 and self.trueCount>2:#if ai is at 10 and high chance of getting a high value card
            self.state = "Double Down"#ai will double down
        else:#if ai has any other value
            self.state = "Hit"#ai will hit
        return self.state#will return state back to gameCycle method

    def getRunTotal_1(self):
        return self.runTotal_1
    def getRunTotal_2(self):
        return self.runTotal_2
            
class Rounds():
    def __init__(self, inv1, inv2, inv3, inv4, deck): #initialises rounds class
        self.score = 0              #sets score used for counting to 0
        self.inv1 = inv1            #sets inventory for class to player inventory
        self.inv2 = inv2            #sets inventory for class to ai1 inventory
        self.inv3 = inv3            #sets inventory for class to ai2 inventory
        self.inv4 = inv4            #sets inventory for class to dealer inventory
        self.deck = deck            #sets deck for class to be current deck
        self.countingChance1 = 0    #sets the chance for counting for ai1 to occur to be 0
        self.countingChance2 = 0    #sets the chance for counting for ai2 to occur to be 0
        self.trueCount1 = 0         #sets the trueCount1 to 0 for start of game
        self.trueCount2 = 0         #sets the trueCount2 to 0 for start of game
        self.ai1Value = 0           #sets the value of a1 inv to 0
        self.pValue = 0             #sets the value of player inv to 0
        self.ai2Value = 0           #sets the value of ai2 inv to 0
        self.dealerValueH = 0       #sets the value of the dealers hidden value to 0 
        self.dealerValueS = 0       #sets the value of the dealers shown value to 0
        self.dealerValue = 0        #sets the value of the dealer total value to 0
        self.aceAi1Count = 0        #sets the count of aces AI1 has to 0
        self.acePCount = 0          #sets the count of aces player has to 0
        self.aceAi2Count = 0        #sets the count of aces AI2 has to 0
        self.aceDealerCount = 0     #sets the count of aces dealer has to 0
        self.ai1Bet = 5000          #sets the bet of the ai1 to 5000
        self.ai2Bet = 5000          #sets the bet of the ai2 to 5000
        self.playerBet = 5000       #sets the bet of the player to 5000
        self.dealerHit = False      #sets the dealerHit to false
        self.splitValue = 0         #sets the value of split inv to 0





    def playerHit(self):#if the player has chosen to hit
        self.pHit = True#prevents player from getting blackjack
        self.pHand = False#keeps player in hand
        self.pCurrentHit = True#allows player to hit

    def playerStand(self):#player chosen to stant
        print("player trying to stand")
        self.pHand = True#ends players hand
        self.pSplit = False#prevents split from occuring
        self.inv1Split = True
        self.inv5Split = True
        self.pSplit = False
            

    def playerDouble(self):#player doubles down
        self.pHit = True#prevents player from getting blackjack
        self.pHand = False#keeps player hand going
        self.pDDHit = True#allows player to double down

    def playerSplit(self):#player chooses to split
        self.pSplit = True
    
    def values(self,inv1, inv2, inv3, inv4):
        #resets all variables used in values
        self.ai1Value = 0
        self.ai2Value = 0
        self.pValue = 0
        self.aceAi1Count = 0
        self.aceAi2Count = 0
        self.acePCount = 0
        self.aceDealerCount = 0
        for i in self.inv2:
            #determins ai1 card values
            #gets the first card in ai1 inventory
            elementposition = self.inv2.index(i)
            self.ai1Card = self.inv2[elementposition]
            self.ai1CardValue = self.ai1Card[1]#finds the value of the first card
            if self.ai1CardValue == "k" or self.ai1CardValue == "q" or self.ai1CardValue == "j" or self.ai1CardValue =="0":
                self.ai1CardValue = 10 #changes the value of a face or 10 card to a 10
                self.ai1Face = True
            elif self.ai1CardValue == "a":
                self.ai1CardValue = 11 #changes the value of an ace to 11 and changes boolean
                self.ai1AceHand = True
                self.aceAi1Count = self.aceAi1Count + 1
            print(self.ai1Value)
            print(self.ai1CardValue)
            self.ai1Value = int(self.ai1Value)+int(self.ai1CardValue)#finds the combined total value of cards of the ai1
            for i in range(0,self.aceAi1Count):
                if self.ai1Value>21: #if the value exceeds 21 and contains an ace, one ace card will revert to the value of 1
                    print("ace moved to 1 ai1")
                    self.ai1Value = self.ai1Value-10
                    self.aceAi1Count = self.aceAi1Count-1

        for j in self.inv1:
            #determins ai1 card values
            #gets the card in player inventory
            elementposition = self.inv1.index(j)
            self.pCard = self.inv1[elementposition]
            self.pCardValue = self.pCard[1]#finds the value of the card
            print(self.pCard)
            print(self.pCardValue)
            if self.pCardValue == "k" or self.pCardValue == "q" or self.pCardValue == "j" or self.pCardValue =="0":
                self.pCardValue = 10 #changes the value of a face or 10 card to 10
            elif self.pCardValue == "a":
                self.pCardValue = 11 #changes the value of an ace to 11 and changes boolean
                self.pAceHand = True
                self.acePCount = self.acePCount + 1
            self.pValue = int(self.pValue)+int(self.pCardValue)#finds the combined total value of cards of the player
            for i in range(0,self.acePCount):
                if self.pValue>21: #if the value exceeds 21 and contains an ace, one ace card will revert to the value of 1
                    print("ace moved to 1 player")
                    self.pValue = self.pValue-10
                    self.acePCount = self.acePCount-1

        for k in self.inv3:#for length of inv3
            #determins ai1 card values
            #gets the card in ai2 inventory
            elementposition = self.inv3.index(k)
            self.ai2Card = self.inv3[elementposition]
            self.ai2CardValue = self.ai2Card[1]#finds the value of the card
            if self.ai2CardValue == "k" or self.ai2CardValue == "q" or self.ai2CardValue == "j" or self.ai2CardValue =="0":
                self.ai2CardValue = 10 #changes the value of a face or 10 card to 10
            elif self.ai2CardValue == "a":
                self.ai2CardValue = 11 #changes the value of an ace to 11 and changes boolean
                self.ai2AceHand = True
                self.aceAi2Count = self.aceAi2Count + 1
            self.ai2Value = int(self.ai2Value)+int(self.ai2CardValue)#finds the combined total value of cards of the ai2
            for i in range(0,self.aceAi2Count):
                if self.ai2Value>21: #if the value exceeds 21 and contains an ace, one ace card will revert to the value of 1
                    self.ai2Value = self.ai2Value-10
                    self.aceAi2Count = self.aceAi2Count-1

        global ai1Value
        global pValue
        global ai2Value
        global dealerValue
        global splitValue

    def splitValues(self, inv5):
        self.splitValue = 0
        self.aceSplitCount = 0
        for i in self.inv5:#for length of inv5
        #gets card from split inventory
            elementposition = self.inv5.index(i)
            self.splitCard = self.inv5[elementposition]
            self.splitCardValue = self.splitCard[1]#finds the value of the card
            if self.splitCardValue == "k" or self.splitCardValue == "q" or self.splitCardValue == "j" or self.splitCardValue =="0":
                self.splitCardValue = 10 #changes the value of a face or 10 card to 10
                self.splitFace = True
            elif self.splitCardValue == "a":
                self.splitCardValue = 11 #changes the value of an ace to 11 and changes boolean
                self.splitAceHand = True
                self.aceSplitCount = self.aceSplitCount + 1
            self.splitValue = int(self.splitValue)+int(self.splitCardValue)#finds the combined total value of cards of the split inv
            for i in range(0,self.aceSplitCount):
                if self.splitValue>21: #if the value exceeds 21 and contains an ace, one ace card will revert to the value of 1
                    print("ace moved to 1 ai1")
                    self.splitValue = self.splitValue-10
                    self.aceSplitCount = self.aceSplitCount-1
        return self.splitValue



    def dealerValueCounter(self, inv4):
        self.dealerValue = 0
        for l in self.inv4:#for how long inv 4 is
            #finds value of card
            elementposition = self.inv4.index(l)
            self.dealerCard = self.inv4[elementposition]
            self.dealerCardValue = self.dealerCard[1]
            if self.dealerCardValue == "k" or self.dealerCardValue == "q" or self.dealerCardValue == "j" or self.dealerCardValue =="0":
                self.dealerCardValue = 10 #changes the value of a face or 10 card to 10
            elif self.dealerCardValue == "a":
                self.dealerCardValue = 11 #changes the value of an ace to 11 and changes boolean
                self.dealerAceHand = True
                self.aceDealerCount = self.aceDealerCount + 1#increases ace count for dealer
            self.dealerValue = int(self.dealerValue)+int(self.dealerCardValue)#finds the combined total value of cards of the dealer
            for i in range(0,self.aceDealerCount):
                if self.dealerValue>21:
                    self.dealerValue = self.dealerValue-10
                    self.aceDealerCount = self.aceDealerCount-1
                #if the value exceeds 21 and contains an ace, one ace card will revert to the value of 1
                
        global dealerValue
        

    def betUp10(self):#if player chooses up 10
        if self.playerBet>=10:#will check if player has enough cash
            global pCashCounter, pBetCounter
            self.playerBet = self.playerBet-10#will remove 10 from total cash
            self.playerPlayBet = self.playerPlayBet + 10#will add 10 to current bet
            #destroys current labels
            pCashCounter.destroy()
            pBetCounter.destroy()
            self.betChange = True#changes boolean to true
        else:
            #states that u are broke in console
            print("ur broke lol")
            
    def betUp100(self):#if player chooses up 100
        if self.playerBet>=100:#check if player has enough cash
            global pCashCounter, pBetCounter
            self.playerBet = self.playerBet-100#will remove 100 from total cash
            self.playerPlayBet = self.playerPlayBet+100#will add 100 to current bet
            #will destroy old labels
            pCashCounter.destroy()
            pBetCounter.destroy()
            self.betChange = True#changes boolean to true
    def betDown10(self):#if player wants to remove 10 from current bet
        global pCashCounter, pBetCounter
        if self.playerPlayBet-10>=0:#checks if enough cash is in current bet
            self.playerBet = self.playerBet+10#adds 10 to total cash
            self.playerPlayBet = self.playerPlayBet-10#remove 10 from current bet
            #destroys old labels
            pBetCounter.destroy()
            pCashCounter.destroy()
            self.betChange = True#changes boolean to true
    def betDown100(self):#if player chooses down 100
        global pCashCounter, pBetCounter
        if self.playerPlayBet-100>=0:#checks if player has enough cash in current bet
            self.playerBet=self.playerBet+100#adds 100 to total cash
            self.playerPlayBet = self.playerPlayBet-100#removes 100 from current bet
            pCashCounter.destroy()#destroys old labels
            pBetCounter.destroy()
            self.betChange = True#changes boolean to true
    def confirmBet(self):#if player has confirmed their bet
        if self.playerPlayBet >0:#checks to see if player has acutally bet
            self.playerBetChosen = True#ends the betting process
        elif self.playerBet<0:#if player hasnt actually bet
            actuallyBetUPoor = Label(tk, text="You do not have enough cash for this bet\nIf you have run out of cash\npress the play button again to restart")#label made to say they dont have enough to bet that
#(cont from prev line) and if the user has ran out of money they will be told to restart their game
            actuallyBetUPoor.place(x=850, y=400)#places label
            tk.update()
            time.sleep(3)#time delay added for visual improvement
            actuallyBetUPoor.destroy()#destroys label

        else:
            actuallyBetUPoor = Label(tk, text="You need to actually bet some money")#label made to say they cant bet nothing
            actuallyBetUPoor.place(x=850, y=400)#places label
            tk.update()
            time.sleep(3)#adds delay for visual improvement
            actuallyBetUPoor.destroy()#destroys label

    def playerSplitAction(self, inv1):#this function splits inv1 into two different invs
        clearPlayerCards = PhotoImage(file="Background folder/clearPlayerCards.png")
        backG.create_image(897, 630, image=clearPlayerCards)
        tk.update()
        time.sleep(1)
        self.temp = self.inv1[1]#takes 2nd card from inv1
        self.inv5.append(self.temp)#adds card to inv5
        self.inv1.pop(1)#removes card from player inv
        cards = Cards(self.inv1, self.inv2, self.inv3, self.inv4, self.inv5)#initializes card class due to new inv
        cards.showSplitP(self.inv1, self.inv5)#show new inv
        self.pSplit = True

    def saveGame(self):
        f = open("Save Folder/saveFile.txt", "w")#opens subfolder Save folder and opens a txt file in write mode
        f.write(str(self.playerBet)+"\n"+str(self.trueCount1)+"\n"+str(self.trueCount2)+"\n")#writes integer values as strings on each line in txt file
        for i in range(0, len(self.inv1)):#for the length of inv1
            f.write(str(self.inv1[i])+"\n")#adds card to next line in txt file
        for i in range(0, len(self.inv2)):#for length of inv2
            f.write(str(self.inv2[i])+"\n")#adds card to next line in txt file
        for i in range(0, len(self.inv3)):#for length of inv3
            f.write(str(self.inv3[i])+"\n")#adds card to next line in txt file
        for i in range(0, len(self.inv4)):#for length of inv4
            f.write(str(self.inv4[i])+"\n")#adds card to next line in txt file
        f.close()#closes saveFile.txt
        f = open("Save Folder/saveDeck.txt", "w")#opens subfolder Save folder and opens saveDeck txt file in write mode
        for i in range(0, len(self.deck)):#for length of deck
            f.write(str(self.deck[i])+"\n")#adds card to the next line in txt file
        f.close()#closes saveDeck file

    def loadGame(self):
        #resets arrays to allow for loading of variables
        self.inv1 = []
        self.inv2 = []
        self.inv3 = []
        self.inv4 = []
        self.deck = []
        f = open("Save Folder/saveFile.txt", "r")#accesses sub folder Save Folder to open txt saveFile in read mode
        #reads each line from file and assigns line to a variable
        lineFromFile = f.readline().rstrip()#reads line
        self.playerBet = int(lineFromFile)#variable set to contents of line
        lineFromFile = f.readline().rstrip()#reads line
        self.trueCount1 = float(lineFromFile)#variable set to contents of line
        lineFromFile = f.readline().rstrip()#reads line
        self.trueCount2 = float(lineFromFile)#variable set to contents of line
        lineFromFile = f.readline().rstrip()#reads line
        invAdder = [lineFromFile[2], lineFromFile[7]]#only takes two characters from line (house, value)
        self.inv1.append(invAdder)#adds card to inv
        lineFromFile = f.readline().rstrip()#reads line
        invAdder = [lineFromFile[2], lineFromFile[7]]#only takes two characters from line (house, value)
        self.inv1.append(invAdder)#adds card to inv
        lineFromFile = f.readline().rstrip()#reads line
        invAdder = [lineFromFile[2], lineFromFile[7]]#only takes two characters from line (house, value)
        self.inv2.append(invAdder)#adds card to inv
        lineFromFile = f.readline().rstrip()#reads line
        invAdder = [lineFromFile[2], lineFromFile[7]]#only takes two characters from line (house, value)
        self.inv2.append(invAdder)#adds card to inv
        lineFromFile = f.readline().rstrip()#reads line
        invAdder = [lineFromFile[2], lineFromFile[7]]#only takes two characters from line (house, value)
        self.inv3.append(invAdder)#adds card to inv
        lineFromFile = f.readline().rstrip()#reads line
        invAdder = [lineFromFile[2], lineFromFile[7]]#only takes two characters from line (house, value)
        self.inv3.append(invAdder)#adds card to inv
        lineFromFile = f.readline().rstrip()#reads line
        invAdder = [lineFromFile[2], lineFromFile[7]]#only takes two characters from line (house, value)
        self.inv4.append(invAdder)#adds card to inv
        lineFromFile = f.readline().rstrip()#reads line
        invAdder = [lineFromFile[2], lineFromFile[7]]#only takes two characters from line (house, value)
        self.inv4.append(invAdder)#adds card to inv
        f.close()#closes file
        f = open("Save Folder/saveDeck.txt", "r")#accesses sub folder Save folder to open txt saveDeck in read mode
        for line in f:#for every line in file will read
            try:#will try to execute code
                deckAdder = [line[2], line[7]]#only takes two characters from line (house, value)
                self.deck.append(deckAdder)#adds card to deck
            except:#if code couldnt be executed
                pass#does nothing so doesnt affect code
        f.close
        
        f.close
    def gameCycle(self, countingChance1, countingChance2, inv1, inv2, inv3, inv4, deck):
        global loadBoolean
        global pHitButton
        global pStandButton
        
        self.roundStart(countingChance1, countingChance2, inv1, inv2, inv3, inv4, deck)#intializes the start of the round
        if loadBoolean == True: #if the loadBoolean = True then the game will load data from seperate files
            self.loadGame()
            loadBoolean = False #returns boolean to default value to stop false positives
        self.values(self.inv1, self.inv2, self.inv3, self.inv4) #finds te values of image
        self.runTotal_1 = 0
        self.runTotal_2 = 0
        while self.playerBet<50000: # creates a while loop to help end game at 50000 score
            self.saveGame() #saves game variables to two different files
            print(self.deck)
            print(len(self.deck))
            #used to test split
            self.inv1 = []
            self.inv1.append(['c', 'k'])
            #self.inv1.append(['c', 'a'])
            self.inv1.append(['c', 'k'])
            #resets all variables and arrays
            self.splitBet = 0
            self.inv5 = []
            self.playedCardsAI1 = []
            self.playedCardsAI2 = []
            self.values(self.inv1, self.inv2, self.inv3, self.inv4)
            self.ai1Hit = False
            self.ai2Hit = False
            self.ai1Blackjack = False
            self.ai2Blackjack = False
            cards = Cards(self.inv1, self.inv2, self.inv3, self.inv4, self.inv5)#initializes Card class incase of change from load
            self.handClear = PhotoImage(file="Background folder/clearAllCards.png")#accesses Background folder sub folder to assign an image
            backG.create_image(0,444,image=self.handClear,anchor=NW)#places image over to hide player and AI previous cards
            self.dealerClear = PhotoImage(file = "Background folder/clearDealerCards.PNG")#accesses Background folder sub folder to assign an image
            backG.create_image(601, 60, image=self.dealerClear,anchor=NW)#places image over dealer previous carsd
            counting = aiCounting(self.inv1, self.inv2, self.inv3, self.inv4,self.runTotal_1,self.runTotal_2, self.deck, self.trueCount1, self.trueCount2, self.playedCardsAI1, self.playedCardsAI2) # initializes aiCounting class
            #resets variables
            self.Hidden = True
            self.playerBetChosen = False
            self.playerPlayBet = 0
            #player bet
            global pCashCounter, pBetCounter
            pBetButtonUp10 = Button(tk, text="Increase bet by 10", command = self.betUp10)#creates button to increase bet by total of 10
            pBetButtonUp10.place(x=710, y=480)#places button on canvas
            pBetButtonUp100 = Button(tk, text="Increase bet by 100", command = self.betUp100)#creates button to increase bet by total of 100
            pBetButtonUp100.place(x=830, y=480)#places button on canvas
            pBetButtonDown10 = Button(tk, text="Decrease bet by 10", command = self.betDown10)#creates button to decrease bet by total of 10
            pBetButtonDown10.place(x=950, y=480)#places button on canvas
            pBetButtonDown100 = Button(tk, text="Decrease bet by 100", command = self.betDown100)#creates button to decrease bet by total of 100
            pBetButtonDown100.place(x=1080, y=480)#places button on canvas
            pBetFinish = Button(tk, text="Confirm Bet", command = self.confirmBet)#creates button to confirm bet
            pBetFinish.place(x=845, y=400)#places button on canvas
            tk.update()
            
            self.betChange = True #allows bet Change labels to appear
            while self.playerBetChosen == False:
                if self.betChange == True:
                    pCashCounter = Label(tk, text="Total Cash Available:"+str(self.playerBet))#sets a label for players total cash
                    pCashCounter.place(x=730, y=450)#places label
                    pBetCounter = Label(tk, text="Total Bet for this round:"+str(self.playerPlayBet))#sets a label for players current bet
                    pBetCounter.place(x=890, y=450)#places label
                    tk.update()
                    self.betChange = False #exits if statement
                tk.update()

            #destroys buttons so game can continue
            pBetButtonUp10.destroy()
            pBetButtonUp100.destroy()
            pBetButtonDown10.destroy()
            pBetButtonDown100.destroy()
            pBetFinish.destroy()
            pBetCounter.destroy()
            pCashCounter.destroy()
            
                              
            #finds AIs bet dependant of the AIs true count
            if self.trueCount1>=0:
                self.modifier = (100+(10*self.trueCount1))/100
                self.ai1PlayBet = abs(round((self.ai1Bet*0.2) * self.modifier))#finds bet and rounds to nearest whole positive number
            elif self.trueCount1<0:
                self.modifier = (100-(10*self.trueCount1))/100
                self.ai1PlayBet = abs(round((self.ai1Bet*0.2) / (-1*self.modifier)))#finds bet and rounds to nearest whole positive number
            self.ai1Bet = self.ai1Bet - self.ai1PlayBet
            if self.trueCount2>=0:
                self.modifier = (100+(10*self.trueCount2))/100
                self.ai2PlayBet = abs(round((self.ai2Bet*0.2) * self.modifier))#finds bet and rounds to nearest whole positive number
            elif self.trueCount2<0:
                self.modifier = (100+(10*self.trueCount2))/100
                self.ai2PlayBet = abs(round((self.ai2Bet*0.2) * self.modifier))#finds bet and rounds to nearest whole positive number
            self.ai2Bet = self.ai2Bet - self.ai2PlayBet
            #creates labels to show current Bets
            pBetLabel = Label(tk, text="Player Current Bet: " + str(self.playerPlayBet))
            ai1BetLabel = Label(tk, text="AI 1 Current Bet: " + str(self.ai1PlayBet))
            ai2BetLabel = Label(tk, text="AI 2 Current Bet: " + str(self.ai2PlayBet))
            #places labels
            pBetLabel.place(x=450, y=10)
            ai1BetLabel.place(x=450, y=30)
            ai2BetLabel.place(x=450, y=50)
            tk.update()
            time.sleep(0.5)#time gap to improve visuals
            cards.showCardsai1(self.inv2)#displays inventory of inv2
            time.sleep(0.75)#time gap to improve visuals
            cards.showPCards(self.inv1)#displays inventory of player
            time.sleep(0.75)#time gap to improve visuals
            cards.showCardsai2(self.inv3)#displays inventory of inv3
            time.sleep(0.75)#time gap to improve visuals
            #shows dealers Cards with first one being hidden
            self.Hidden = True
            cards.dealerCards(self.inv4, self.Hidden)
            self.dealerHit == False

            if self.dealerValue == 21 and self.dealerHit == False:#finds out if dealer has blackjack off start
                    print("dealer Blackjack")
                    self.dealerState = "Blackjack" #sets the state of the dealer to Blackjack
                    #prevents other members from having their go
                    self.pHand = True
                    self.ai2Hand  = True
                    self.ai1Hand  = True

            
            #ai1 decision
            self.ai1Hand = False
            self.ai1State = ""
            if self.countingChance1 != 1: #if the ai is not undergoing counting
                self.DD = False #sets double down to false
                while self.ai1Value<17 and self.DD == False and len(self.inv2)<5 and self.ai1Hand == False:
                    if self.ai1Value == 11 and self.ai1Hit == False: #if the ai1  is 11 and hasnt hit before then will double down
                        self.HitCard=self.deck[0] #card set from top deck
                        self.deck.pop(0)#card from top of deck removed
                        self.inv2.append(self.HitCard)#added card to inv2
                        self.ai1PlayBet = self.ai1PlayBet*2#doubles the current ai1 bet
                        ai1BetLabel.destroy()#destroys old ai1 bet label
                        #updates ai1 bet label
                        ai1BetLabel = Label(tk, text="AI 1 Current Bet: " + str(self.ai1PlayBet))
                        ai1BetLabel.place(x=450, y=50)
                        self.values(self.inv1, self.inv2, self.inv3, self.inv4)#finds value of inventories
                    if int(self.ai1Value) <17:#ai will hit if under17 
                        #hit card
                        self.HitCard=self.deck[0]#card set from top deck
                        self.deck.pop(0)#card removed from top of deck
                        self.inv2.append(self.HitCard)#card added to inv2
                        self.values(self.inv1, self.inv2, self.inv3, self.inv4)#finds value of inventories
                        self.ai1Hit = True #means the AI cant double down
                if self.ai1Value == 21 and self.ai1Hit == False: #checks for blackjack
                    self.ai1State = "Blackjack" #sets ai1 state to Blackjack
                if len(self.inv2) == 5 and self.ai1Value<=21: #checks for 5 card charlie
                    self.ai1State = "5 Card Charlie" #sets ai1 state to 5 card charlier
                elif int(self.ai1Value)>21: #checks to see if ai1 is bust
                    self.ai1State = "Bust" #sets ai1 state to bust
            

            
            if self.ai1Value == 21 and self.ai1Hit == False: #checks to see if ai1 has a blackjack
                print("ai1 Blackjack")
                self.ai1State = "Blackjack"#sets the state to Blackjack
                self.ai1Hand = True#ends ai1 hand
                
            if self.countingChance1 ==1:#ichecks to see if ai is going to be counting
                print("ai1 counting choices")
                self.trueCount1 = counting.counting1(self.countingChance1, self.inv1, self.inv2, self.inv3, self.inv4, self.deck, self.trueCount1, self.playedCards)#finds the true count before ai1 actions
                print()
                print(self.trueCount1)
                self.values(self.inv1, self.inv2, self.inv3, self.inv4)#finds value of inventory
                print("before ai1 while loop")
                #resets variables
                self.ai1Counter = 0 
                self.ai1Hit = False
                while self.ai1Hand == False:
                    self.values(self.inv1, self.inv2, self.inv3, self.inv4)#finds values of inventories
                    print(self.ai1Value)
                    print(self.ai1State)
                    self.ai1State = counting.actions(self.ai1Value, self.aceAi1Count, self.trueCount1)#ai decides what action it will do
                    if self.ai1State == "Hit":
                        self.HitCard=self.deck[0]#takes card from top of deck
                        self.deck.pop(0)#remove card from deck
                        self.inv2.append(self.HitCard)#adds card to inventory
                        self.playedCardsAI1.append(self.HitCard)
                    if self.ai1State == "Double Down":
                        self.HitCard=self.deck[0]#takes card from deck
                        self.deck.pop(0)#removes it from array
                        self.inv2.append(self.HitCard)#adds card to inv2
                        self.playedCardsAI1.append(self.HitCard)
                        self.ai1PlayBet = self.ai1PlayBet*2#dubles ai1 bet
                        ai1BetLabel.destroy()#destroys old bet label
                        ai1BetLabel = Label(tk, text="AI 1 Current Bet: " + str(self.ai1PlayBet))#creates label for new bet
                        ai1BetLabel.place(x=450, y=30)#places label
                        self.ai1State = "Stand"#ends ai1 hand
                    if len(self.inv2) == 5 and self.ai1Value<=21:
                        self.ai1State = "5 Card Charlie"#if length of inv is 5 and value less then or equal to 21 then 5 card charlie awarded
                        self.ai1Hand = True#ends ai1 hand
                    if self.ai1State == "Stand" or self.ai1Value<=21:#if ai1 stands or busts ends hand
                        self.ai1Hand = True#ends ai1 hand
                    cards.showCardsai1(self.inv2)#updates gui to show new ai1 cards
                    tk.update()
            self.ai1Hand = True
            
            #resets all player variables
            self.pSplit = False
            self.pHand = False
            self.HitCard = False
            self.pState = ""
            self.splitState = ""
            #runs functions to make sure they still exist and work
            self.playerHit()
            self.playerDouble()
            pHitButton = Button(tk, text="Hit", command = self.playerHit)#creates button allowing for player to hit
            pHitButton.place(x = 810, y=480)#places button
            pStandButton = Button(tk, text="Stand", command = self.playerStand)#creates button allowing for player to stand
            pStandButton.place(x=840, y=480)#places button
            pDoubleButton = Button(tk, text="Double Down", command = self.playerDouble)#creates a button allowing for player to double down
            pDoubleButton.place(x=884, y=480)#places button
            pSplitButton = Button(tk, text="Split", command = self.playerSplit)#creates a button allowing for player to split if two cards have same value
            #finds the values of both cards
            self.card1 = self.inv1[0]
            self.card2 = self.inv1[1]
            self.value1 = self.card1[1]
            self.value2 = self.card2[1]
            print(self.value1, self.value2)
            if self.value1 == self.value2: #compares values of both cards to see if they are the same
                pSplitButton.place(x=974, y=480)#places split button if two cards are the same
            cards.showPCards(self.inv1)#updates player cards
            backG.pack()
            tk.update()
            self.pCurrentHit = False#reset variable
            
            if self.pValue == 21 and self.HitCard == False:#checks to see if player has a blackjack
                self.pState = "Blackjack"#sets pState to Blackjack
                self.pHand = True#ends players hand
                time.sleep(1)#delays code by 1 second to improve visuals
            while self.pHand == False:#creates a loop for player to choose action
                if len(self.inv1) == 5 and self.pValue<=21:#if the length of inv1 is 5 and value less than or equal to 21 5 card charlie awarded
                    self.pState = "5 Card Charlie"#sets state to 5 card charlie
                    self.pHand = True#ends player hand
                #resets variables
                self.pHand = False
                self.pCurrentHit = False
                self.pDDHit = False
                tk.update()
                if self.pCurrentHit == True:#player chooses hit
                        print("player is trying to hit")
                        pDoubleButton.destroy()#destroys double down button
                        self.HitCard = self.deck[0]#takes one card from top of deck
                        self.deck.pop(0)#deletes card from top of deck
                        self.inv1.append(self.HitCard)#adds card to inv1
                        self.playedCardsAI1.append(self.HitCard)#adds card to playedCardsAI1 for counting
                        cards.showPCards(self.inv1)#updates gui to show new player card
                        self.values(self.inv1, self.inv2, self.inv3, self.inv4)#finds value of new hand
                        if self.pValue>21:#checks to see if player has gone bust
                            self.pState = "Bust"#sets state to bust
                            self.pHand = True#ends players hand
                            print("Bust")
                        self.pCurrentHit = False#resets variable
                        if self.value1 == self.value2:#if hit is chosen when could split it will destroy split button
                            pSplitButton.destroy()
                        tk.update()
                if self.pDDHit == True:#if player chooses double down
                        self.HitCard = self.deck[0]#takes card from top of deck
                        self.deck.pop(0)#removes card from deck
                        self.inv1.append(self.HitCard)#adds card to inv1
                        self.playedCardsAI1.append(self.HitCard)#adds card to array for ai1 to count
                        cards.showPCards(self.inv1)#updates gui to show new player card
                        self.values(self.inv1, self.inv2, self.inv3, self.inv4)#finds the new value
                        #updates the bet to be double
                        self.playerBet = self.playerBet - self.playerPlayBet
                        self.playerPlayBet = self.playerPlayBet*2
                        pBetLabel.destroy()#destroys old player bet labe;
                        pBetLabel = Label(tk, text="Player Current Bet: " + str(self.playerPlayBet))#updates bet label
                        pBetLabel.place(x=450, y=10)#places new label
                        if self.pValue>21:#checks to see if player goes bust
                            self.pState = "Bust"#sets state to bust
                            self.pHand = True#ends players go
                            print("Bust")
                        self.pHand = True#ends players go
                        if self.value1 == self.value2:#if double down when could of split destroys split button
                            pSplitButton.destroy()
                if self.pSplit == True:#if split has been chosen
                    print(self.inv1)
                    #destroys split and double down button
                    pSplitButton.destroy()
                    pDoubleButton.destroy()
                    self.playerSplitAction(self.inv1)#sets up split actions
                    print("after playerSplitAction")
                    #creates a new bet for the new inv and removes from total player cash
                    self.splitBet = self.playerPlayBet
                    self.playerBet = self.playerBet - self.splitBet
                    splitBetLabel = Label(tk, text="Split Hand Current Bet: " + str(self.splitBet))#creates new bet label
                    splitBetLabel.place(x = 450, y=70)#places new label
                    self.pHand = True
                    self.pSplit = True
                    clearPlayerCards = PhotoImage(file="Background folder/clearPlayerCards.png")#opens sub folder Background folder to access image
                    backG.create_image(897, 630, image=clearPlayerCards)#places image over old player hand due to inv changes
                    tk.update()
            #reste
            self.inv1Split = False
            self.inv5Split = False      
            while self.pSplit == True:
                tk.update()
                cards.showSplitP(self.inv1, self.inv5)#shows new cards
                while self.inv1Split == False:#hand 1
                    tk.update()
                    if len(self.inv1) == 5 and self.pValue<=21:#checks for 5 card charlie
                        self.pState = "5 Card Charlie"#sets state to 5 card charlie
                    if self.pCurrentHit ==True:#when player chooses to hit on first inv
                        print("player is trying to hit from split")
                        self.HitCard = self.deck[0]#takes card from top of deck
                        self.deck.pop(0)#removes card from deck
                        self.inv1.append(self.HitCard)#adds card to inv1
                        self.playedCardsAI1.append(self.HitCard)#adds card to array for ai1 counting
                        self.values(self.inv1, self.inv2, self.inv3, self.inv4)#finds new value
                        if self.pValue>21:#checks to see if player is bust
                            self.pState = "Bust"#sets state to bust
                            self.pHand = True
                            print("Bust")
                            self.inv1Split = True#ends inv1 hand
                        self.pCurrentHit = False
                        cards.showSplitP(self.inv1, self.inv5)#shows new cards
                self.inv5Split = False
                while self.inv5Split == False:#hand 2
                    tk.update()
                    if len(self.inv5) == 5 and self.splitValue<=21:#checks for 5 card charlie
                        self.splitState = "5 Card Charlie"#sets state to 5 card charlie
                    if self.pCurrentHit ==True:#player chooses to hit on second inv
                        print("player is trying to hit from split")
                        self.HitCard = self.deck[0]#takes card from top of deck
                        self.deck.pop(0)#removes card from top of deck
                        self.inv5.append(self.HitCard)#adds card to inv5
                        self.playedCardsAI1.append(self.HitCard)#adds card to array for ai1 counting
                        self.splitValue = self.splitValues(self.inv5)#finds the value of the new inv
                        print(self.splitValue)
                        if self.splitValue>21:#checks to see if inv is bust
                            self.splitState = "Bust"#sets state to bust
                            self.inv5Split = True
                            self.pSplit = False
                            print("Bust")
                            self.inv5Split = True#ends inv5 hand
                        self.pCurrentHit = False
                        cards.showSplitP(self.inv1, self.inv5)#shows new cards
            if self.splitValue>0:
                self.pSplit = True
            print("out of loops") 
                    
                        
            if self.value1 == self.value2:#if split button has been placed
                try:
                    pSplitButton.destroy()#destroy split button
                except:
                    pass
            #destroys player action buttons
            pHitButton.destroy()
            pDoubleButton.destroy()
            pStandButton.destroy()
            tk.update()
            #resests ai2 state
            self.ai2State = ""
            if self.countingChance2 != 2:#checks if ai2 isnt counting
                self.DD = False#reset variable
                while self.ai2Value<17 and len(self.inv3)<5 and self.DD == False:#checks to see if ai2 hand is over
                    if self.ai2Value == 11:#double down
                        #doubles ai2 bet
                        self.ai2PlayBet = self.ai2PlayBet*2
                        ai2BetLabel.destroy()#destroys old bet
                        ai2BetLabel = Label(tk, text="AI 2 Current Bet: " + str(self.ai2PlayBet))#updates new bet label
                        ai2BetLabel.place(x=450, y=50)#places new bet label
                        self.DD = True
                    if int(self.ai2Value) <=17:#ai will hit
                        print("ai2 Hitting at:", self.ai2Value)
                        #hit card
                        self.HitCard=self.deck[0]#card taken from top of deck
                        print(self.deck[0])
                        self.deck.pop(0)#card removed from top of deck
                        self.inv3.append(self.HitCard)#card added to inv
                        self.playedCardsAI1.append(self.HitCard)#adds card to playedCardsAI1 for counting
                        print(self.inv3)
                        self.values(self.inv1, self.inv2, self.inv3, self.inv4)#finds new values
                        print()
                        print()
                        print(self.inv3, " ", self.ai2Value)
                        self.ai2Hit = True#prevents ai2 from getting blackjack state after hitting
                if self.ai2Value == 21 and self.ai2Hit == False:#checks for blackjack
                    self.ai2State = "Blackjack"#sets state to blackjack
                if len(self.inv3) == 5 and self.ai2Value<=21:#checks for 5 card charlie
                    self.ai2State = "5 Card Charlie"#sets state to 5 card charlie
                elif int(self.ai2Value)>21:#checks to see if ai has bust
                    self.ai2State = "Bust"#sets state to bust



            self.ai2Hand = False
            self.ai2Counter = 0
            self.ai2State = ""

            if self.ai2Value == 21 and self.ai2Hit == False:#checks for blackjack
                print("ai2 Blackjack")
                self.ai2State = "Blackjack"
                self.ai2Hand = True
            
            if self.countingChance2 ==2:#checks if ai2 will be counting
                self.trueCount2 = counting.counting2(self.countingChance2, self.inv1, self.inv2, self.inv3, self.inv4, self.deck, self.trueCount2)#counts current cards using halves method
                while self.ai2Hand == False:#while ai2 hand is going
                    self.values(self.inv1, self.inv2, self.inv3, self.inv4)#finds values of cards
                    self.ai2State = counting.actions(self.ai2Value, self.aceAi2Count, self.trueCount2)#ai2 chooses action
                    if self.ai2State == "Hit":#if ai2 hits
                        self.HitCard=self.deck[0]#card taken from top of deck
                        self.deck.pop(0)#card removed from top of deck
                        self.inv3.append(self.HitCard)#card added to inv3
                        self.playedCardsAI1.append(self.HitCard)#adds card to array for ai1 counting
                    if self.ai2State == "Double Down":#double down
                        self.HitCard=self.deck[0]#card taken from top of deck
                        self.deck.pop(0)#card removed from top of deck
                        self.inv3.append(self.HitCard)#adds card to ai2 inv
                        self.playedCardsAI1.append(self.HitCard)#adds card to array for ai1 counting
                        #doubles ai2 bet
                        self.ai2PlayBet = self.ai2PlayBet*2
                        ai2BetLabel.destroy()#deletes old bet
                        ai2BetLabel = Label(tk, text="AI 2 Current Bet: " + str(self.ai2PlayBet))#updates new bet label
                        ai2BetLabel.place(x=450, y=50)#places label
                        self.ai2State = "Stand"#ends ai2 hand
                    if self.ai2State == "Stand" or self.ai2Value<=21:#if ai2 hand should end
                        self.ai2Hand = True#ends ai2 hand
                    if len(self.inv3) == 5 and self.ai2Value<=21:#checks ai2 for 5 card charlie
                        self.ai2State = "5 Card Charlie"#sets state to 5 card charlie
                    cards.showCardsai2(self.inv3)#updates gui to show new cards
                    tk.update()
                    
            #resets variables
            self.dealerState = ""
            time.sleep(2)
            self.Hidden = False
            self.playedCardsAi2 = []
            cards.dealerCards(self.inv4, self.Hidden)
            print("poopoo")
            self.dealerHit = False
            self.dealerHand = False
            self.dealerCounter = 1
            self.dHand = False
            while self.dealerValue<17 and self.dHand == False:#dealer must hit if less then 17 or hand hasnt finished
                if int(self.dealerValue)<17:
                    #hit card
                    self.HitCard=self.deck[0]#card taken from top of deck
                    self.deck.pop(0)#card removed from top of deck
                    self.inv4.append(self.HitCard)#card added to inv4
                    self.playedCardsAi2.append(self.HitCard)#card added to array for ai1 counting
                    self.dealerValueCounter(self.inv4)#finds the value for the dealer
                    self.dealerHit = True#prevents blackjack
                    cards.dealerCards(self.inv4, self.Hidden)#updates gui to show new dealer cards
                    tk.update()
                    if len(self.inv4) == 5:#prevents dealer from having more then 5 cards
                        self.dHand = True#ends dealers hand
            if self.dealerValue == 21 and self.dealerHit == False:#checks for blackjack
                self.dealerHand = True#ends dealer hand
                self.dealerState = "Blackjack"#sets state to blackjack
            elif int(self.dealerValue)>21:#checks for bust
                self.dealerHand = True#ends dealers hand
                self.dealerState = "Bust"#sets state to bust
            if self.dealerValue>16:#if value greater then 17
                self.dealerHand = True#ends dealer hand
            cards.dealerCards(self.inv4, self.Hidden)#updates gui to show new dealer cards


            #ai1
            if self.ai1State == "5 Card Charlie":#checks to see if ai1 has a 5 card charlie
                self.ai1Bet = self.ai1Bet+2*(self.ai1PlayBet)#updates bet as won
                ai1StateLabel = Label(tk, text="5 Card Charlie")#changes label to 5 card charlie
                #5 CARD CHARLIE
            elif self.ai1State == "Blackjack" and self.dealerState == "Blackjack":#checks to see if a blackjack push has occured
                self.ai1Bet = self.ai1Bet+self.ai1PlayBet#bet goes back to original
                #PUSH
                ai1StateLabel = Label(tk, text="Push")#changes label to push
            elif self.ai1State == "Blackjack":#checks to see if ai1 has a blackjack
                self.ai1BlackjackBet = self.ai1PlayBet + int(round((self.ai1PlayBet/2)))#pays out bet 3/2
                self.ai1Bet = self.ai1PlayBet+ self.ai1Bet+self.ai1BlackjackBet
                ai1StateLabel = Label(tk, text="Blackjack")#changes label to blackjack
                #BLACKJACK
            elif self.dealerState == "Blackjack":#checks to see if dealer has a blackjack
                ai1StateLabel = Label(tk, text="Dealer Blackjack")#updates label to dealer blackjack
                #DEALER WON
            elif self.dealerValue>21 and self.ai1Value<=21:#checks to see if dealer bust and ai1 hasnt
                #DEALER BUST
                self.ai1Bet = self.ai1Bet+2*(self.ai1PlayBet)#ai wins round and gets double the bet back
                ai1StateLabel = Label(tk, text="Dealer Bust")#changes label to dealer Bust
            elif self.ai1Value<self.dealerValue and self.dealerValue<22:#checks to see if ai1 value is less then dealer value
                #DEALER HIGHER
                ai1StateLabel = Label(tk, text="Dealer Higher")#set label to dealer high
            elif self.ai1Value == self.dealerValue and (self.ai1Value<=21 or self.dealerValue<=21):#if the dealer and ai have same value while being less then or equal to 21
                self.ai1Bet = self.ai1Bet+self.ai1PlayBet#bet goes back to original
                ai1StateLabel = Label(tk, text="Push")#changes label to push
                #PUSH
            elif self.ai1Value>self.dealerValue and self.ai1Value<=21:#if the ai is higher then the dealer while being less then or equal 21
                self.ai1Bet = self.ai1Bet+ 2*(self.ai1PlayBet)#ai wins round and gets double bet back
                ai1StateLabel = Label(tk, text="Higher than Dealer")#changes label to higher then dealer
                #BEAT DEALER
            elif self.ai1Value>21 or self.ai1Value == "Bust":#if the ai has gone bust
                ai1StateLabel = Label(tk, text="Bust")#changes label to bust
                #BUST
            self.ai1Value = 0
                
            
                
            #player
            if self.pState == "5 Card Charlie":#checks to see if player has 5 card charlie
                self.playerBet = self.playerBet+(2*self.playerPlayBet)#changes bet to won
                pStateLabel = Label(tk, text="5 Card Charlie")#sets label to 5 card charlie
                #5 CARD CHARLIE
            elif self.pState == "Blackjack" and self.dealerState == "Blackjack":#checks if blackjack push occurs
                self.playerBet = self.playerBet+self.playerPlayBet#bet goes back to original
                pStateLabel = Label(tk, text="Push")#label set to push
                #PUSH
            elif self.pState == "Blackjack":#checks if player has blackjack
                self.playerBlackjackBet = self.playerPlayBet + (self.playerPlayBet/2)#bet payed 3/2
                self.playerBet = int(self.playerBet) +int(self.playerPlayBet)+int(self.playerBlackjackBet)
                pStateLabel = Label(tk, text="Blackjack")#set label to blackjack
                #PLAYER BLACKJACK
            elif self.dealerState == "Blackjack":#if dealer has blackjack
                pStateLabel = Label(tk, text="Dealer Blackjack")#sets label to dealer blackjack
                self.playerBet = self.playerBet#bet stays the same
                #DEALER BLACKJACK
            elif self.dealerValue>21 and self.pValue<=21:#checks to see if dealer has bust while player value less then 22
                #DEALER BUST
                self.playerBet = self.playerBet+2*(self.playerPlayBet)#bet changed to won
                pStateLabel = Label(tk, text="Dealer Bust")#set label to dealer bust
            elif self.pValue<self.dealerValue and self.dealerValue<22:#if dealer is higher then player value and less then 22
                #DEALER HIGHER
                pStateLabel = Label(tk, text="Dealer Higher")#set label to dealer higher
                self.playerBet = self.playerBet#bet stays the same
            elif self.pValue == self.dealerValue and (self.pValue<=21 or self.dealerValue<=21):#checks to see if push
                self.playerBet = self.playerBet+self.playerPlayBet#bet set back to original
                pStateLabel = Label(tk, text="Push")#label set to push
                #PUSH
            elif self.pValue>self.dealerValue and self.pValue<=21:#checks to see if player value higher then dealer while less then 22
                self.playerBet = self.playerBet+ 2*(self.playerPlayBet)#bet changed to won
                pStateLabel = Label(tk, text="Higher than Dealer")#label set to higher than dealer
                #BEAT DEALER
            elif self.pValue>21 or self.pValue == "Bust":#checks if player has bust
                pStateLabel = Label(tk, text="Bust")#changes label to bust
                self.playerBet = self.playerBet#bet stays the same
                #BUST
            self.pValue = 0
            int(self.playerBet)
            
                
            #ai2
            if self.ai2State == "5 Card Charlie":#checks to see if ai2 has a 5 card charlie
                self.ai2Bet = self.ai2Bet+2*(self.ai2PlayBet)#updates bet as won
                ai2StateLabel = Label(tk, text="5 Card Charlie")#changes label to 5 card charlie
            elif self.ai2State == "Blackjack" and self.dealerState == "Blackjack":#checks to see if a blackjack push has occured
                self.ai2Bet = self.ai2Bet+self.ai2PlayBet#bet goes back to original
                ai2StateLabel = Label(tk, text="Push")#changes label to push
                #PUSH
            elif self.ai2State == "Blackjack":#checks to see if ai2 has a blackjack
                self.ai2BlackjackBet = self.ai2PlayBet + (self.ai2PlayBet/2)#pays out bet 3/2
                self.ai2Bet = self.ai2PlayBet+self.ai2Bet+self.ai2BlackjackBet
                ai2StateLabel = Label(tk, text="Blackjack")#changes label to blackjack
                #AI2 BLACKJACK
            elif self.dealerState == "Blackjack":#checks to see if dealer has a blackjack
                ai2StateLabel = Label(tk, text="Dealer Blackjack")#updates label to dealer blackjack
                #DEALER BLACKJACK
            elif self.dealerValue>21 and self.ai2Value<=21:#checks to see if dealer bust and ai2 hasnt
                #DEALER BUST
                self.ai2Bet = self.ai2Bet+2*(self.ai2PlayBet)#ai wins round and gets double the bet back
                ai2StateLabel = Label(tk, text="Dealer Bust")#changes label to dealer Bust
            elif self.ai2Value<self.dealerValue and self.dealerValue<22:#checks to see if ai2 value is less then dealer value
                #DEALER HIGHER
                ai2StateLabel = Label(tk, text="Dealer Higher")#set label to dealer high
            elif self.ai2Value == self.dealerValue and (self.ai2Value<=21 or self.dealerValue<=21):#if the dealer and ai have same value while being less then or equal to 21
                self.ai2Bet = self.ai2Bet+self.ai2PlayBet#bet goes back to original
                ai2StateLabel = Label(tk, text="Push")#changes label to push
                #PUSH
            elif self.ai2Value>self.dealerValue and self.ai2Value<=21:#if the ai is higher then the dealer while being less then or equal 21
                self.ai2Bet = self.ai2Bet+ 2*(self.ai2PlayBet)#ai wins round and gets double bet back
                ai2StateLabel = Label(tk, text="Higher than Dealer")#changes label to higher then dealer
                #BEAT DEALER
            elif self.ai2Value>21 or self.ai2Value == "Bust":#if the ai has gone bust
                ai2StateLabel = Label(tk, text="Bust")#changes label to bust
                #BUST
                
            if self.pSplit == True:#if player has chosen to split
                if self.splitState == "5 Card Charlie":#checks for 5 card charlie
                    self.playerBet = self.playerBet+2*(self.playerPlayBet)#changes bet to won
                    pStateLabel = Label(tk, text="5 Card Charlie")#sets label to 5 card charlie
                elif self.dealerState == "Blackjack":#checks if dealer has blackjack
                    splitStateLabel = Label(tk, text="Dealer Blackjack")#changes label to dealer blackjack
                    self.playerBet = self.playerBet#bet stays the same
                    #DEALER BLACKJACK
                elif self.dealerValue>21 and self.splitValue<=21:#checks to see if dealer has bust while split value less then 22
                    #DEALER BUST
                    self.playerBet = self.playerBet+2*(self.splitBet)#changes bet to won
                    splitStateLabel = Label(tk, text="Dealer Bust")#sets label to dealer bust
                elif self.splitValue<self.dealerValue and self.dealerValue<22:#checks to see if dealer value higher
                    #DEALER HIGHER
                    splitStateLabel = Label(tk, text="Dealer Higher")#sets label to dealer higher
                    self.playerBet = self.playerBet#bet stays the same
                elif self.splitValue == self.dealerValue and (self.splitValue<=21 or self.dealerValue<=21):#checks to see if a push has occured underneath 22
                    self.playerBet = self.playerBet+self.splitBet#bet returns to normal
                    splitStateLabel = Label(tk, text="Push")#label set to push
                    #PUSH
                elif self.splitValue>self.dealerValue and self.splitValue<=21:#checks if split value is less then 22 but higher then dealer
                    self.playerBet = self.playerBet+ 2*(self.splitBet)#changes bet to won
                    splitStateLabel = Label(tk, text="Higher than Dealer")#sets label as higher then dealer
                    #BEAT DEALER
                elif self.splitValue>21 or self.splitValue == "Bust":#checks if bust
                    splitStateLabel = Label(tk, text="Bust")#changes label to bust
                    self.playerBet = self.playerBet#bet stays the same
                    
            self.ai2Value = 0
            self.x1 = 850#sets x coord for player incase of split
            if self.pSplit==True:#checks if player has split
                self.x1 = self.x1-90#moves x coord for player label back 90 pixels
                splitStateLabel.place(x=1050, y=400)#places split label
            ai1StateLabel.place(x=1250, y=400)#places ai1 label
            pStateLabel.place(x=self.x1,y=400)#places player label
            ai2StateLabel.place(x=250, y=400)#places ai2 label
            tk.update()
            time.sleep(5)#adds a timer to improve visuals
            #removes labels from being seen
            ai1StateLabel.lower()
            pStateLabel.lower()
            ai2StateLabel.lower()
            if self.pSplit==True:#if player has split
                splitStateLabel.lower()#moves label so cannot be seen
            tk.update()
            #ai do endgame counting for what cards have been dealt after initial count
            if self.countingChance1 ==1:
                print(self.trueCount1)
                self.trueCount1 = counting.ai1EndgameCount(self.playedCardsAI1, self.trueCount1, self.deck)
                self.runTotal_1 = counting.getRunTotal_1()
                print(self.trueCount1)
            if self.countingChance2 ==2:
                print(self.trueCount2)
                self.trueCount2 = counting.ai2EndgameCount(self.playedCardsAi2, self.trueCount2, self.deck)
                self.runTotal_2 = counting.getRunTotal_2()
                print(self.trueCount2)
            
            print(len(self.deck))
            time.sleep(1)#adds timer to improve visuals
            inv = Inventory()
            if self.splitValue>0:#if player split
                splitBetLabel.destroy()#destroys split label
            pBetLabel.destroy()#destroys player label
            ai1BetLabel.destroy()#destroys ai1 label
            ai2BetLabel.destroy()#destorys ai2 label
            tk.update()
            print(len(self.deck))
            if len(self.deck)<104:#checks to see if length of deck is less then half of original lenght
                self.deck = cards.deckingCards()#reshuffles deck with all cards
                self.trueCount1 = 0#resets trueCount1
                self.trueCount2 = 0#resets trueCount2
            self.deck = inv.startInv(self.deck)#sets up inventories for new round
            #gets inventories from inventory class
            self.inv1 = inv.getInv1()#inv1
            self.inv2 = inv.getInv2()#inv2
            self.inv3 = inv.getInv3()#inv3
            self.inv4 = inv.getInv4()#inv4
            #finds values of new inventories
            self.values(self.inv1, self.inv2, self.inv3, self.inv4)
            self.dealerValueCounter(self.inv4)
        gameLabel = Label(tk, text="You have reached over 50,000!\nWell done!\nPress the play button to play again")#if player reaches 50000 cash, this label will be set
        gameLabel.place(x=850, y=350)#label will be placed and game will need to be played again to progress
        tk.mainloop()

        
                
            

    def roundStart(self, countingChance1, countingChance2, inv1, inv2, inv3, inv4, deck):
        self.countingChance1 = random.randint(1,1)#decides if AIs will do counting methods for the rest of the game
        print(self.countingChance1)
        self.countingChance2 = random.randint(2,2)
        print(self.countingChance2)
        #resets variables and arrays
        self.trueCount1 = 0
        self.trueCount2 = 0
        self.playedCards = []
        self.inv5 = []
        self.handClear = PhotoImage(file="Background folder/clearAllCards.png")#accesses Background folder sub folder to assign an image
        backG.create_image(0,444,image=self.handClear,anchor=NW) #places image to cover any cards from player or A1
        self.dealerClear = PhotoImage(file = "Background folder/clearDealerCards.PNG")#accesses Background folder sub folder to assign an image
        backG.create_image(601, 60, image=self.dealerClear,anchor=NW) #places image to cover any dealer cards
        cards = Cards(inv1, inv2, inv3, inv4, self.inv5) #initializes Cards Class
        #creates 4 shuffled deck of cards added together
        self.deck = cards.deckingCards()
        self.deckFull = self.deck #sets deckFull variable to same contents as deck(full length of deck)
        inv = Inventory() #initializes inventory class
        self.deck = inv.startInv(cards.deckOfCards) #adds 2 cards to each inv
        self.inv1 = inv.getInv1()#gets inv1 from inv class
        self.inv2 = inv.getInv2()#gets inv2 from inv class
        self.inv3 = inv.getInv3()#gets inv3 from inv class
        self.inv4 = inv.getInv4()#gets inv4 from inv class
        self.values(self.inv1, self.inv2, self.inv3, self.inv4) # finds the value of each inventory
        #dealer card Values
        self.dealerCardH = self.inv4[0] # finds the hidden card out of dealer inv
        self.dealerCardS = self.inv4[1] # finds the shown card out of dealer inv
        self.dealerValueH = self.dealerCardH[1]#finds the value of the hidden card
        self.dealerAceHand = False #sets booleans to false so no false positives occur
        self.dealerdoubleAce = False
        if self.dealerValueH == "k" or self.dealerValueH == "q" or self.dealerValueH == "j" or self.dealerValueH =="0": #if dealer gets a face or 10 card, value is set to 10
            self.dealerValueH = 10
        elif self.dealerValueH == "a":# sets the value of shown card to 11 and dealerAceHand to True if ace is the hidden dealer card
            self.dealerValueH = 11
            self.dealerAceHand = True
        self.dealerValueS = self.dealerCardS[1]
        if self.dealerValueS == "k" or self.dealerValueS == "q" or self.dealerValueS == "j" or self.dealerValueS =="0": #if dealer gets a face or 10 card, value is set to 10
            self.dealerValueS = 10
        elif self.dealerValueS == "a":# sets the value of shown card to 11 and dealerAceHand to True if ace is the shown dealer card
            self.dealerValueS = 11
            self.dealerAceHand = True
        elif self.dealerValueS == 11 and self.dealerValueH == 11:#sets dealerdoubleAce to true and dealerAceHand to false if dealer inv contains two aces
            self.dealerAceHand = False
            self.dealerdoubleAce = True 
        self.dealerValue = int(self.dealerValueS)+int(self.dealerValueH) #finds the total value of the dealers card
        if self.dealerValue>21 and self.dealerAceHand == True: #if the dealer has an ace and is somehow bust it will remove 10 so isnt bust off start
            self.dealerValue = self.dealerValue-10
        elif self.dealerdoubleAce == True: # if the dealer has two aces it will remove 10 off the total value, so not bust instantly
            self.dealerValue = self.dealerValue-10

        #used to return all inventorys and values of inventorys if needed
        def getRInv1(self):
            return self.inv1
        def getRInv2(self):
            return self.inv2
        def getRInv3(self):
            return self.inv3
        def getRInv4(self):
            return self.inv4
        def getRValue1(self):
            return self.pValue
        def getRValue2(self):
            return self.ai1Value
        def getRValue3(self):
            return self.ai2Value
        def getRValueH4(self):
            return self.dealerValueH
        def getRValueT4(self):
            return self.dealerValue
        

class Inventory():
    def __init__(self):# initializes class by defining all inventorys as empty
        self.inv1 = []
        self.inv2 = []
        self.inv3 = []
        self.inv4 = []
    #creates inventory of all players by adding card to each inventory twice and removes each card from deck
    def startInv(self, deckOfCards):
        self.n = deckOfCards
        for i in range (0,2): #2 cards for each inventory
            self.inv1.append(self.n[0]) #adds card to inv1
            self.n.pop(0)#removes card from deck
            self.inv2.append(self.n[0]) #adds card to inv2
            self.n.pop(0)#removes card from deck
            self.inv3.append(self.n[0]) #adds card to inv3
            self.n.pop(0)#removes card from deck
            self.inv4.append(self.n[0]) #adds card to inv4
            self.n.pop(0)#removes card from deck
        return deckOfCards
    
    #returns all inventorys to the main part of program
    def getInv1(self):
        return self.inv1
    def getInv2(self):
        return self.inv2
    def getInv3(self):
        return self.inv3
    def getInv4(self):
        return self.inv4

def exitGame():
    #closes the game
    exit()
    

    
def backgroundTotal():
    #creating the background of the GUI
    global background
    global JackBlack
    global PausePicture
    global backG
    global pauseButton
    global tk
    b1.destroy()#destroys start game button
    b2.destroy()#destroys load game button
    b3.destroy()#destroys exti game button
    backG = Canvas(tk, width=1800, height=720)#sets the new canvas dimensions
    backG.pack()
    tk.title("JackBlack: A Blackjack Game")
    background = PhotoImage(file='Background folder/Improved Background for nea.png')#opens Background folder to access the background table for the game
    backG.create_image(0,0, image=background, anchor=NW)                            #places the background table on the canvas
    #Adding in a picture of Jack Black (The AI opponent)
    JackBlack = PhotoImage(file='Background folder/Jack Black AI Picture 50x50.png')#opens Background folder to access image for the dealer
    backG.create_image(875,0, image=JackBlack, anchor=NW)                           #places image above dealer hand to simulate the dealer
    #adds pause button to the top right of the game
    pausePicture = PhotoImage(file='Background folder/Pause logo.png')              #accesses Background folder sub folder to access image for button
    pauseButton = Button(tk, image=pausePicture, command=openNewMenu, anchor ='w', borderwidth=0)#creates a button to open a new pause menu, button will appear as an image
    pauseButtonWindow = backG.create_window(5,5, anchor ='nw', window=pauseButton)  #places pause button on canvas
    startPicture = PhotoImage(file='Background folder/Start logo.png')     #opens Background folder subfolder to access image for button
    startButton = Button(tk, image=startPicture, command=gameplay, anchor ='w',borderwidth = 0) #creates a button to carry out gameplay function and appear as an image
    startButton.place(x=80, y=5)                                        #places start button on canvas
    deckPicture = PhotoImage(file='playingCards/BackOfCard150x211.png') #accesses back of card image from playingCards sub folder
    backG.create_image(1350, 15, image = deckPicture, anchor=NW)    #places image to simulate stack of cards
    tk.mainloop()

def gameplay():
    handClear = PhotoImage(file="Background folder/clearAllCards.png") #accesses image from Background folder sub folder
    backG.create_image(0,444,image=handClear,anchor=NW)                #places image ontop of player and AI hands so cards dissappear
    dealerClear = PhotoImage(file = "Background folder/clearDealerCards.PNG")#accesses image from Background folder sub folder
    backG.create_image(601, 60, image=dealerClear,anchor=NW)     #places image ontop of dealer hand so cards dissappear
    playerInv = []          #sets all inventorys to empty so inventorys dont carry over from other games
    aiInv1 = []
    aiInv2 = []
    dealerInv = []
    deckCards = []
    gameRound = Rounds(playerInv, aiInv1, aiInv2, dealerInv, deckCards)    #initializes Rounds Class
    gameRound.gameCycle(0, 0, playerInv, aiInv1, aiInv2, dealerInv, deckCards) #Runs gameCycle method within Rounds Class
    
def loadGame():
    global loadBoolean #sets variable to be global so can be accessed within classes
    loadBoolean = True #sets boolean to true so game will be loaded from file once started
    backgroundTotal()  #automatically runs the background loading part of game
    
def openNewMenu():
    #this def creates a new menu when the pause button is clicked
    global nb1              #sets variables to be global so can be accesed in different functions
    global nb2
    global nb3
    newMenu = Toplevel(tk)
    newMenu.title("Menu") #changes name of window to Menu
    nb1 = Button(newMenu, text="Start New Game", command=gameplay).grid()#creates a button that will start the game again
    nb3 = Button(newMenu, text="Exit Game", command=exitGame).grid()     #creates a button which will quit the game
    
def menu():
    #creates a menu to either start, load or quit game
    global canvas           #sets variables to be global so can be accesed in different functions
    global b1
    global b2
    global b3
    canvas = Canvas(tk, width=300, height=400) #creates a canvas for gui to appear
    tk.title("Menu") #changes name of window to Menu
    b1 = Button(tk, text="Start Game", command=backgroundTotal) #creates a button that will start the game
    b1.pack()
    b2 = Button(tk, text="Load Game", command=loadGame) #creates a button which will allow for a previous save game to be loaded
    b2.pack()
    b3 = Button(tk, text="Exit Game", command=exitGame) #creates a button which will quit the game
    b3.pack()

    
loadBoolean = False #sets the load function
menu()              #runs the menu function

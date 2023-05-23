# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 23:39:22 2022

@author: garcip2
"""
#5/23/23: No changes made, just testing github
from colorama import Fore, Back, Style
colors = [Fore.RED,Fore.GREEN,Fore.YELLOW,Fore.BLUE]
directions = ("nw","n","ne","e","se","s","sw","w")
rings = ("o","m","i")
moves = ("u","d","l","r")

class Ball:
    def __init__(self,player,number,color = colors[0],char="●"):
        self.plr = player
        self.num = number
        self.clr = color
        self.char = char
    def __str__(self):
        return self.clr + self.char + Fore.RESET
    
def display(bd):
    # 13x13 square
    out = bd[0].copy()
    mid = bd[1].copy()
    inn = bd[2].copy()
    board=(out,mid,inn)
    hor = "―"
    vert = "|"
    emp = "◌"
    sp = " "
    for n in board:
        for k in range(0,len(n)):
            if n[k] == 0:
                n[k] = emp
    
    print(out[0], hor*5, out[1], hor*5,out[2], sep="")
    
    print(vert + 5*sp + vert + 5*sp + vert)
    
    print(vert + sp + str(mid[0]) + 3*hor + str(mid[1]) + 3*hor + str(mid[2]) + sp + vert)
    
    print(vert + sp + vert + 3*sp + vert + 3*sp + vert + sp + vert)
    
    print(vert, sp, vert, sp, inn[0], hor, inn[1], hor, inn[2], sp, vert, sp, vert, sep="")
    
    print(vert, sp, vert, sp, vert, 3*sp, vert, sp, vert, sp, vert, sep="")
    
    print(out[7], hor, mid[7], hor, inn[7], 3*sp, inn[3], hor, mid[3], hor, out[3], sep="")
    
    print(vert, sp, vert, sp, vert, 3*sp, vert, sp, vert, sp, vert, sep="")
    
    print(vert, sp, vert, sp, inn[6], hor, inn[5], hor, inn[4], sp, vert, sp, vert, sep="")

    print(vert + sp + vert + 3*sp + vert + 3*sp + vert + sp + vert)

    print(vert, sp, mid[6], 3*hor, mid[5], 3*hor, mid[4], sp, vert, sep="")

    print(vert, 5*sp, vert, 5*sp, vert, sep="")
    
    print(out[6],hor*5,out[5],hor*5,out[4],sep="")


    
def genBoard(bd):
    char = 0
    outer = [char]*8
    middle = [char]*8
    inner = [char]*8
    bd.append(outer)
    bd.append(middle)
    bd.append(inner)
    
def place(bd,ball,ring,direc):
    if direc not in directions:
        print("Not a valid direction")
        return False
    if ring not in rings:
        print("Not a valid ring")
        return False
    rn = rings.index(ring)
    dr = directions.index(direc)
    tile = bd[rn][dr]
    if tile == 0:
        bd[rn][dr] = ball
        return True
    else:
        return False
    
    
def askPlace(bd,player,color,number):
    '''

    Parameters
    ----------
    bd : list
        The board.
    player : int
        Player number, 1 or 2.
    color : Colorama color object
        The color of the piece to be placed.
    number : int
        Number of the piece, 1-9.

    Asks the player for information corresponding to a location on
    the board so the game can attempt to place a piece there. Handles
    errors if the place is invalid.

    '''
    while True:
        ring = input("Select ring (Outer (o), Middle (m), Inner (i)): ").strip().lower()[0]
        direc = input("Input location (North (n), NorthWest (nw), etc): ").strip().lower()
        if place(bd,Ball(player,number,color),ring,direc):
            break
        else:
            print("Invalid placement")
            continue
        
def move(bd,player,ring,direc,move):
    rn = rings.index(ring)
    dr = directions.index(direc)
    tile = bd[rn][dr]
    if type(tile) != Ball:
        print("There is no piece there")
        return False
    else:
        if player != tile.plr:
            print("That is not your piece")
            return False
        else:
            #Piece is valid, time to test move validity
            if move not in moves:
                print("Not a direction")
                return False
            if direc == "nw":
                if (move == "u") or (move == "l"):
                    print("Out of Bounds")
                    return False
                elif move == "d":
                    newRing = ring
                    newDirec = "w"
                elif move == "r":
                    newRing = ring
                    newDirec = "n"
            elif direc == "ne":
                if (move == "u") or (move == "r"):
                    print("Out of Bounds")
                    return False
                elif move == "d":
                    newRing = ring
                    newDirec = "e"
                elif move == "l":
                    newRing = ring
                    newDirec = "n"
            elif direc == "sw":
                if (move == "d") or (move == "l"):
                    print("Out of Bounds")
                    return False
                elif move == "u":
                    newRing = ring
                    newDirec = "w"
                elif move == "r":
                    newRing = ring
                    newDirec = "s"
            elif direc == "se":
                if (move == "d") or (move == "r"):
                    print("Out of Bounds")
                    return False
                elif move == "u":
                    newRing = ring
                    newDirec = "e"
                elif move == "l":
                    newRing = ring
                    newDirec = "s"
            elif direc == "n":
                if ring == "o" and move == "u":
                    print("Out of Bounds")
                    return False
                elif ring == "i" and move == "d":
                    print("Out of Bounds")
                    return False
                pass
            elif direc == "e":
                pass
            elif direc == "s":
                pass
            elif direc == "w":
                pass
            else:
                print("You're not supposed to be here!")
                return False
    
    
    
def gameplay():
    bd = []
    genBoard(bd)
    display(bd)
    p1clr = Fore.RED
    p2clr = Fore.BLUE
    for n in range(18):
        if n%2 == 0:
            print("P1 Turn")
            askPlace(bd,1, p1clr, n//2 + 1)
        else:
            print("P2 Turn")
            askPlace(bd,2, p2clr, n//2 + 1)
        display(bd)
            
    
 
'''
a = []
genBoard(a)
display(a)
'''

#a = Ball(1,1,Fore.BLUE)
#print(a)
gameplay()

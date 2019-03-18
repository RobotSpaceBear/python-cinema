import os
import random
import sys

# ==== CONSTANTES
ROWS  = 8
COLUMNS = 15
OCCUPIED_ASCII = '\u2593'
FREE_ASCII = '\u2591'
# ===============

def exit_app():
    sys.exit()

def make_reservation():
    return

def cancel_reservation():
    return 

def print_theater(seatList):
    totalColWidth = COLUMNS * 3 # Has to be the same number a the format below ex:'{:>3}'.format()
    seatFormat='{:>3}'
    header = ' ECRAN '
    hearderDecorationChar = '='
    headerSideDecorationWidth = int(((totalColWidth - len(header)) / 2) / int(len(hearderDecorationChar)))
    print(hearderDecorationChar * headerSideDecorationWidth 
        + header
        + hearderDecorationChar * headerSideDecorationWidth
        +'\n\n')
    
    #printing the seat number header
    for colNum in range(COLUMNS):
        print(seatFormat.format(colNum), end='')
    print('\n')

    for row in range(ROWS):        
        for col in range(COLUMNS):
            isOccupied = seatList[row][col]
            if(isOccupied):
                print(seatFormat.format(OCCUPIED_ASCII), end='')
            else:
                print(seatFormat.format(FREE_ASCII), end='')
        
        print('{:>4}'.format(str(chr(row+65))), end=' ') #printing the seat row (letter)   
        print('\n')

def display_root_menu():
    print('What do you want to do?\n')
    print('1. See the theater seats.')
    print('2. Make a reservation.')
    print('3. Cancel a reservation.')
    print('4. Exit.')

def ask_for_action():
    display_root_menu()
    
    while True:
        userInput = input('Please type the number of the action and press ENTER: ')
        try:
            userInput = int(userInput)
            if(type(userInput)==int and 1 <= int(userInput) <=4 ): #remember to update with menu number
                break
        except ValueError:
            continue

    menuActions = {1: print_theater(None),
        2: make_reservation(),
        3: cancel_reservation(),
        4: exit_app(),
    } #home made switch with dictionnaries / values bound to functions

    menuActions[int(input)]()




def clear_console():
    os.system('cls' if os.name=='' else 'clear')



######## START ########
clear_console()
print('Welcome to the python-cinema app.')
ask_for_action()

seatList = [[0] * COLUMNS for x in range(ROWS)]
seatList[1][3] = 1
seatList[5][3] = 1
#print_theater(seatList)
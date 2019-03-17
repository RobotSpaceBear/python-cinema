import random
import os

# ==== CONSTANTES
ROWS  = 8
COLUMNS = 15
OCCUPIED_ASCII = '\u2593'#u'\u2593'
FREE_ASCII = '\u2591'#u'\u2591'
# ===============


def clearConsole():
    os.system('cls' if os.name=='nt' else 'clear')

def printTheater():
    totalColWidth = COLUMNS * 3 # Has to be the same number a the format below ex:'{:>3}'.format()
    seatFormat='{:>3}'
    header = ' ECRAN '
    hearderDecorationChar = '='
    headerSideDecorationWidth = int(((totalColWidth - len(header)) / 2) / int(len(hearderDecorationChar)))
    print(hearderDecorationChar * headerSideDecorationWidth 
        + header
        + hearderDecorationChar * headerSideDecorationWidth
        +'\n\n')

    for colNum in range(COLUMNS):
        print(seatFormat.format(colNum), end='')
    print('\n')

    for row in range(ROWS):
        
        for col in range(COLUMNS):
            isOccupied = random.randint(0,1)
            if(isOccupied):
                print(seatFormat.format(OCCUPIED_ASCII), end='')
            else:
                print(seatFormat.format(FREE_ASCII), end='')
        print('{:>4}'.format(str(chr(row+65))), end=' ')   
        print('\n')


clearConsole()
printTheater()
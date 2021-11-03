import random

def play():
    user = input("pilih 'r' untuk batu, 's' untuk gunting, 'p' untuk kertas")
    computer = random.choice (['r','s','p'])

    if user== computer :
        return 'Imbang'

    if is_win (user, computer):
        return 'Lo Menang'

    return 'Kalah'

def is_win (player, component) :
    if(player == 'r' and computer == 's') or (player == 's' and computer == 'p') 
        or (player == 'p' and computer == 'r'):
        return 'lo menang'

        print (play)
    
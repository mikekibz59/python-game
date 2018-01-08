import random
import textwrap


def show_theme_message(dotted_line, width):
    print(dotted_line)
    print("\033[1m" + "Attack of The Orcs v0.0.1: " + "\033[0m")
    msg = (
        ' The war between humans and their arch enemies, Orcs, was in the '
        'offing. Sir Foo, one of the brave knights guarding the southern'
        ' plains began a long journey toward the east through an unknown '
        ' dense forest. On his way, he spotted a small isolated settlement'
        'Tired and hoping to replenish his food stock, he decided to take'
        ' a detour. As he approached the village, he saw five huts. There'
        'was no one to be seen around. Hesitantly, he decide to enter ...')

    print(textwrap.fill(msg, width=width))

def show_game_mission(dotted_line):
    print("\033[1m" + "Mission:" + "\033[0m")
    print("\t Choose a hut where Sir Foo can rest....")
    print("\033[1m" + "Tip: " + "\033[0m")
    print("Be carefull there are many enemies lurking around")
    print(dotted_line)

def occupy_huts(occupants):
    huts = []
    while len(huts) < 5 :
        computer_choice = random.choice(occupants)
        huts.append(computer_choice)
    return huts

def process_user_choice():
    msg = "\033[1m" + " Choose a hut number to enter (1-5): " + "\033[0m"
    user_choice = input("\n" + msg + "\t")
    idx = int(user_choice)
    return idx

def reveal_occupants(huts, idx, dotted_line):
    print("Revealing the occupants")
    msg = ""
    for i in range(len(huts)):
        occupants_info = "<%d:%s>" % (i + 1, huts[i])
        if i + 1 == idx:
            occupants_info = "\033[1m" + occupants_info + "\033[0m"
        msg += occupants_info + " "
    print("\t" + msg)
    print(dotted_line)
    print("\033[1m" + "Entering hut %d ..." % idx + "\033[0m", end=' ')

def get_winner(huts, idx, dotted_line):
    if huts[idx - 1] == 'enemy':
        print("\033[1m" + "YOU LOSE :(BETTER luck next time)" + "\033[0m")
    else:
        print("\033[1m" + "Congratulations!! You win !!" + "\033[0m")
    print(dotted_line)

def run_app():
    keep_playing = 'y'
    occupants = ['enemy', 'friend', 'unoccupied']
    width = 72
    dotted_line = '_' * width
    show_theme_message(dotted_line, width)
    show_game_mission(dotted_line)

    while keep_playing == 'y':
        huts = occupy_huts(occupants)
        idx = process_user_choice()
        reveal_occupants(huts,idx,dotted_line)
        get_winner(huts,idx,dotted_line)
        keep_playing = input("Play again? Yes(y)/No(n): ")


if __name__ == '__main__':
    run_app()








import time
import random
import sys

# just of effects. add a delay of 1 second before performing any action
SLEEP_BETWEEN_ACTIONS = 0.01
MAX_VAL = 100
DICE_FACE = 6

player1_current_position = 0
player2_current_position = 0

# snake takes you down from 'key' to 'value'
snakes = {
    17: 7,
    54: 34,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    99: 78
}

# ladder takes you up from 'key' to 'value'
ladders = {
    4: 14,
    31: 9,
    28: 84,
    20: 38,
    40: 59,
    61: 67,
    63: 81,
    71: 91
}

player_turn_text = [
    "Your turn.",
    "Go.",
    "Please proceed.",
    "Lets win this.",
    "Are you ready?",
    "",
]

snake_bite = [
    "boohoo",
    "bummer",
    "snake bite",
    "oh no",
    "dang"
]

ladder_jump = [
    "woohoo",
    "woww",
    "nailed it",
    "oh my God...",
    "yaayyy"
]


def welcome_msg():
    msg = "Iranian version of snakes and ladders (Childhood memory).\n"
    print(msg)


def get_player_names():
    player1_name = None
    while not player1_name:
        player1_name = raw_input("name for player1: ").strip()

    player2_name = None
    while not player2_name:
        player2_name = raw_input("name for player2: ").strip()

    return player1_name, player2_name


def get_dice_value():
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    dice_value = random.randint(1, DICE_FACE)
    print("Its a " + str(dice_value))
    return dice_value


def got_snake_bite(old_value, current_value, player_name):
    print("\n" + random.choice(snake_bite).upper() + " ~~~~~~~~>")
    print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))


def got_ladder_jump(old_value, current_value, player_name):
    print("\n" + random.choice(ladder_jump).upper() + " ########")
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))


def snake_ladder(player_name, current_value, dice_value):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > MAX_VAL:
        print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value


def check_win(player_name, position):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    if MAX_VAL == position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        sys.exit(1)

def check_kick(player1_current_position,player2_current_position):
    if player1_current_position == player2_current_position:
        return True
    return False


def start():
    welcome_msg()
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    player1_name, player2_name = get_player_names()
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    global player1_current_position
    global player2_current_position
    player1_move_ok = False
    player2_move_ok = False

    while True:
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        input_1 = raw_input("\n" + player1_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        print("\nRolling dice for "+player1_name)
        if not player1_move_ok:
            dice_value = get_dice_value()
            if dice_value == 6:
                print(player1_name+" move ok")
                player1_move_ok = True
            else:
                player1_move_ok = False
        if player1_move_ok:
            dice_value = 0
            while True:
                dice_value = dice_value + get_dice_value()
                if dice_value % 6 != 0:
                    break
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(player1_name + " moving....")
            
            player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)
            check_win(player1_name, player1_current_position)
            if check_kick(player1_current_position,player2_current_position):
                print(player2_name + " Kicked by " + player1_name)
                raw_input()
                player2_move_ok = False
                player2_current_position = 0



        input_2 = raw_input("\n" + player2_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        print("\nRolling dice for "+player2_name)
        if not player2_move_ok:
            dice_value = get_dice_value()
            if dice_value == 6:
                print(player2_name+" move ok")
                player2_move_ok = True
            else:
                player2_move_ok = False
        if player2_move_ok:
            dice_value = 0
            while True:
                dice_value = dice_value + get_dice_value()
                if dice_value % 6 != 0:
                    break
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(player2_name + " moving....")
            player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)

            check_win(player2_name, player2_current_position)
            if check_kick(player1_current_position,player2_current_position):
                print(player1_name + " Kicked by " + player2_name)
                raw_input()
                player1_move_ok = False
                player1_current_position = 0


if __name__ == "__main__":
    start()

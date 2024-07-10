# Refer to the minion game challenge in hacker rank
# 2 players. A string is given. 
# Player 1: has to make letter combos starting with consonants
# Player 2: to make combos starting with vowels
# 1 point for each occurence of the combo in the word

def update_player(string: str, player: dict) -> None:
    if player.get(string):
        player[string] = player[string] + 1
    else:
        player[string] = 1


def get_total_score(player: dict) -> int:
    total_score = 0
    
    for key in player:
        total_score += player[key]

    return total_score


def main():
    string = 'VINOTHANAND'
    string_length = len(string)
    vowels = ['A', 'E', 'I', 'O', 'U']
    p1 = 'Stuart'
    p2 = 'Kevin'

    # Player 1
    player_1 = {}
    player_2 = {}
    p1_total = 0
    p2_total = 0
    for index, letter in enumerate(string):
        # print(index, letter)
        if not letter.isalpha() or not letter.isupper():
            print('Invalid character found. Only upper case alphabets allowed!! Exiting!')
            return                   
            
        if letter in vowels:
            p2_total += (string_length - index)
        else:
            p1_total += (string_length - index)

    # print(player_1)
    # print(player_2)
    # p1_total = get_total_score(player_1)
    # p2_total = get_total_score(player_2)

    print(f'P1: {p1_total}, P2: {p2_total}')
    
    if p1_total > p2_total:
        print(f'{p1} {p1_total}')
    elif p2_total > p1_total:
        print(f'{p2} {p2_total}')
    else:
        print('Draw')


if __name__ == '__main__':
    main()  
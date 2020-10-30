# Andrew Li
# 1824794

player_dict = {}
key_list = []
option = ''

# gets user input and adds to dictionary
for i in range(1, 6):
    jersey_num = input("Enter player {}'s jersey number:\n".format(i))
    player_rating = input("Enter player {}'s rating:\n".format(i))
    print()
    player_dict[jersey_num] = player_rating
# print(player_dict)

# adds dict keys to list to be able to be sorted
for key in player_dict:
    key_list.append(key)


def print_roster():
    key_list.sort(key=int)
    # print(key_list)  # for debugging

    # prints roster created from user inputs

    print("ROSTER")
    for key in key_list:
        print("Jersey number: {}, Rating: {}".format(key, player_dict[key]))


print_roster()
while option != 'q':
    option = ''
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit\n")

    while option != 'a' and option != 'd' and option != 'u' and option != 'r' and option != 'o' and option != 'q':
        option = input('Choose an option:\n')
    if option == 'a':
        new_jersey = input("Enter a new player's jersey number:\n")
        new_rating = input("Enter the player's rating:\n")
        player_dict[new_jersey] = new_rating

    if option == "d":
        pass
    if option == "u":
        pass
    if option == "r":
        pass
    if option == "o":
        key_list.append(new_jersey)
        print_roster()

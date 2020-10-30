# Andrew Li
# 1824794

player_dict = {}
key_list = []
option = ''

for i in range(1, 6):
    jersey_num = input("Enter player {}'s jersey number:\n".format(i))
    player_rating = input("Enter player {}'s rating:\n".format(i))
    player_dict[jersey_num] = player_rating
# print(player_dict)

for key in player_dict:
    key_list.append(key)
key_list.sort()
print()
print("ROSTER")

for key in key_list:
    print("Jersey number: {}, Rating: {}".format(key, player_dict[key]))

while option != 'q':
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
        pass
    if option == "d":
        pass
    if option == "u":
        pass
    if option == "r":
        pass
    if option == "o":
        pass

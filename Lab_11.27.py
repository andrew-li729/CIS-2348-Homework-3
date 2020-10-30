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

for key in key_list:
    print("Jersey number: {}, Rating: {}".format(key, player_dict[key]))


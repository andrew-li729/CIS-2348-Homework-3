# Andrew Li
# 1824794

player_dict = {}

for i in range(1, 6):
    jersey_num = input("Enter player {}'s jersey number:\n".format(i))
    player_rating = input("Enter player {}'s rating:\n".format(i))
    player_dict[jersey_num] = player_rating
print(player_dict)
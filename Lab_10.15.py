# Andrew Li
# 1824794
class Team:
    def __init__(self):
        self.teamname = 'none'
        self.teamwins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return self.teamwins / (self.teamwins + self.team_losses)


win_average = Team()
win_average.teamname = input()
win_average.teamwins = int(input())
win_average.team_losses = int(input())

# print(win_average.get_win_percentage())
if win_average.get_win_percentage() > 0.5:
    print("Congratulations, Team {} has a winning average!".format(win_average.teamname))
else:
    print("Team {} has a losing average.".format(win_average.teamname))

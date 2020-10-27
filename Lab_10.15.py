# Andrew Li
# 1824794
class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)


if __name__ == '__main__':
    win_average = Team()
    win_average.team_name = input()
    win_average.team_wins = int(input())
    win_average.team_losses = int(input())

    # print(win_average.get_win_percentage())
    if win_average.get_win_percentage() >= 0.5:
        print("Congratulations, Team {} has a winning average!".format(win_average.team_name))
    else:
        print("Team {} has a losing average.".format(win_average.team_name))

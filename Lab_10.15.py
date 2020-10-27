# Andrew Li
# 1824794
class Team:
    def __init__(self):
        self.teamname = 'none'
        self.teamwins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return self.teamwins / (self.teamwins + self.team_losses)



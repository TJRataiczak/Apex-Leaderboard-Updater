class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points
    
    def add_points(self, points):
        self.points = self.points + points


all_players = {}

all_players["TJ Rataiczak"] = ['TJ Rataiczak', 20]
all_players["Dylan Ham"] = ['Dylan Ham', 20]
all_players["Ryan Hayes"] = ['Ryan Hayes', 18]

print(all_players['Dylan Ham'][1] + 30)
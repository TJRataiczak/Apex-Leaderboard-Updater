class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points
    
    def add_points(self, points):
        self.points = self.points + points


all_players = {}

all_players["TJ Rataiczak"] = Player('TJ Rataiczak', 25)
all_players["Dylan Ham"] = Player('Dylan Ham', 20)
all_players["Ryan Hayes"] = Player('Ryan Hayes', 18)
class Player:
    def __init__(self, name, points, placing):
        self.name = name
        self.points = points
        self.qualified = False
        self.placings = [placing]
    
    def add_points(self, more_points):
        self.points += more_points
    
    def update_qualification(self, qual):
        self.qualified = qual

    def update_placings(self, new_placing):
        self.placings.append(new_placing)
        self.placings.sort()

players = [
    Player('TJ Rataiczak', 19, 1),
    Player('Franklin Fulks', 25, 2),
    Player('Ryan Hayes', 13, 45)
]

players.sort(key=lambda x: x.points, reverse=True)

print(players[0].points)
print(players[1].points)
print(players[2].points)
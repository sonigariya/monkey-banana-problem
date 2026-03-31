
# Monkey Banana Problem

class MonkeyBanana:
    def __init__(self):
        self.monkey_position = "door"
        self.box_position = "window"
        self.banana_position = "center"
        self.monkey_on_box = False
        self.has_banana = False

    def move(self, position):
        if not self.monkey_on_box:
            print("Monkey moves from", self.monkey_position, "to", position)
            self.monkey_position = position
        else:
            print("Monkey cannot move while on the box")

    def push_box(self, position):
        if self.monkey_position == self.box_position and not self.monkey_on_box:
            print("Monkey pushes the box to", position)
            self.box_position = position
            self.monkey_position = position
        else:
            print("Monkey cannot push the box")

    def climb_box(self):
        if self.monkey_position == self.box_position:
            print("Monkey climbs the box")
            self.monkey_on_box = True
        else:
            print("Box is not here")

    def grab_banana(self):
        if self.monkey_on_box and self.monkey_position == self.banana_position:
            print("Monkey grabs the banana 🍌")
            self.has_banana = True
        else:
            print("Monkey cannot reach the banana")

    def solve(self):
        self.move("window")
        self.push_box("center")
        self.climb_box()
        self.grab_banana()

# Run program
problem = MonkeyBanana()
problem.solve()
class Solution:
    def turnLeft(self, direction):
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        return direction

    def turnRight(self, direction):
        if direction == "north":
            direction = "east"
        elif direction == "west":
            direction = "north"
        elif direction == "south":
            direction = "west"
        elif direction == "east":
            direction = "south"
        return direction

    def moveForward(self, location, direction, steps, obstacles):

        x, y = location
        if direction == "north":
            forward = (0, 1)
        elif direction == "south":
            forward = (0, -1)

        elif direction == "east":
            forward = (1, 0)

        elif direction == "west":
            forward = (-1, 0)

        result = (x, y)
        tmp = (x, y)
        for i in range(steps):
            tmp = (tmp[0] + forward[0], tmp[1] + forward[1])
            if tmp in obstacles:
                break
            else:
                result = tmp

        return result

    def robotSim(self, commands, obstacles):
        location = (0, 0)
        direction = "north"
        current, maximum = None, None
        obstacles = set(tuple(item) for item in obstacles)
        for command in commands:
            if command == -2:
                direction = self.turnLeft(direction)
            elif command == -1:
                direction = self.turnRight(direction)
            elif command >= 1 and command <= 9:
                location = self.moveForward(location, direction, command, obstacles)
            current = location[0] * location[0] + location[1] * location[1]

            if maximum is None or current > maximum:
                maximum = current

        return maximum

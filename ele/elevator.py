import time


class Elevator:
    SPEED = 1

    def __init__(self, max_floor, min_floor=1, current_floor=1):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.current_floor = current_floor

    def move(floor):
        if self.current_floor == floor:
            return

        step = 1 if self.current_floor < floor else -1
        for index in range(self.current_floor, floor, step):
            time.delay(SPEED)
            print("Current floor: %s", index)

        self.current_floor = floor

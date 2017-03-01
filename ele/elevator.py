import time


class MaxFloorError(Exception):
    pass

class MinFloorError(Exception):
    pass

class Elevator:
    SPEED = 1
    DOORS_SPEED = 1

    def __init__(self, max_floor, min_floor=1, current_floor=1):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.current_floor = current_floor
        self.doors_open = False

    def move(floor):
        if self.current_floor == floor:
            return

        if floor > self.max_floor:
            raise MaxFloorError("An elevator cannot go higher then its max floors")

        if floor < self.min_floor:
            raise MinFloorError("An elevator cannot go lower then its min floors")

        step = 1 if self.current_floor < floor else -1
        for index in range(self.current_floor, floor, step):
            time.delay(SPEED)
            print("Current floor: %s", index)

        self.current_floor = floor

    def cycle_doors():
        open_doors()
        close_doors()

    def open_doors():
        if self.doors_open:
            return
        time.delay(DOORS_SPEED)
        self.doors_open = True
        print("Opening doors")

    def close_doors():
        if not self.doors_open:
            return
        time.delay(DOORS_SPEED)
        self.doors_open = False
        print("Closing doors")

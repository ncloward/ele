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
        self.moving = False

    def move(target_floor):
        if self.current_floor == target_floor:
            return

        if target_floor > self.max_floor:
            raise MaxFloorError("An elevator cannot go higher then its max floors")

        if target_floor < self.min_floor:
            raise MinFloorError("An elevator cannot go lower then its min floors")

        self.moving = True
        step = 1 if self.current_floor < target_floor else -1

        for index in range(self.current_floor, target_floor, step):
            time.delay(SPEED)
            self.current_floor = index
            print("Current floor: %s", index)

        self.moving = False

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

    def pirority(target_floor):
        """
        This method will calculate the elevators priority when a target floor
        is passed in.  This will be calculated based on the elevators current floor
        or its direction. If its moving.

        Priority will be based on the distance between the target floor and current
        floor.  A higher priority is not better, because we are calculating the priority
        with the distance the elveator furthest away will have a higher priority. If the
        elevator is moving we can subtract the max floor from the priority to move it to
        the top.  There are probably better ways to calculate this but for now this shoul
        work.
        """
        priority = abs(target_floor - self.current_floor)
        if self.moving:
            priority = self.max_floor - priority
        return priority

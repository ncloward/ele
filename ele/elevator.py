class Elevator:
    def __init__(self, max_floor, min_floor=1, current_floor=1):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.current_floor = current_floor

from ele.elevator import Elevator


def test_initialise_default():
    elevator = Elevator(10)
    assert elevator.min_floor == 1
    assert elevator.max_floor == 10
    assert elevator.current_floor == 1

def test_initialise_min_floor():
    elevator = Elevator(10, min_floor=-1)
    assert elevator.min_floor == -1
    assert elevator.max_floor == 10
    assert elevator.current_floor == 1

def test_initialise_current_floor():
    elevator = Elevator(10, current_floor=2)
    assert elevator.min_floor == 1
    assert elevator.max_floor == 10
    assert elevator.current_floor == 2

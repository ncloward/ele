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

def test_move_up_success():
    # Test the move function for an elevator in the up direction.
    pass

def test_move_up_max_floor():
    # Test the move function for an elevator so it cannot go passed the max floor count
    pass

def test_move_down_success():
    # Test the move function for an elevator in the down direction.
    pass

def test_move_up_min_floor():
    # Test the move function for an elevator so it cannot go passed the min floor count
    pass

def test_open_doors():
    # Test the open_doors function for an elevator
    pass

def test_close_doors():
    # Test the close_doors function for an elevator
    pass

def test_cycle_doors():
    # Test the cycle_doors function for an elevator
    pass

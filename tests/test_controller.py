import ele.controller

def test_process_success():
    assert ele.controller.process(4, 10) is True

def test_request_elevator():
    # Tests requesting an elevator, evaluating the priority and
    # picking the elevator with the lowest priority.
    pass

def test_request_elevator_moving():
    # Tests requesting an elevator, evaluating all the elevators priorities
    # and then making sure the elevator that is moving passed the target
    # floor responds to the request.
    pass

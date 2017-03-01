from ele.elevator import Elevator


def process(elevator_count, max_floor):
    elevators = []
    for index in range(elevator_count):
        elevators = Elevator(max_floor)

    # TODO: When the the controller would get a request for the closest elevator to go to a
    # specific target floor it would calculate the priority for each elevator and call
    # the move on the elevator with the lowest priority and move it to the correct floor.

    # TODO: Implement a way to asynchronously communicate with each elevator.
    # This could be using threading or asyncio.  It would allow the elevators to
    # use more of an event communication with the controller.  This would make it easier
    # to interupt the moving elevator as it moves passed a floor that has requested
    # and elevator.

    return True

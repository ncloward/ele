#!/usr/bin/env python3
import ele.controller

ELEVATOR_COUNT = 4
FLOOR_COUNT = 10

def main():
    result = ele.controller.process(ELEVATOR_COUNT, FLOOR_COUNT)
    print(result)

if __name__ == "__main__":
    main()

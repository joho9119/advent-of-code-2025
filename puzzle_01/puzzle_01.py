from enum import Enum
from typing import Self

try:
    from .puzzle_01_raw_list import PARSED_LIST
except ImportError:
    PARSED_LIST = [] # you can add your own here.

class Direction(Enum):
    RIGHT = 1, "right"
    LEFT = -1, "left"

    def multiplier(self):
        return self.value[0]

    def display(self):
        return self.value[1]

    @classmethod
    def from_movement(cls, m: str) -> Direction:
        if m[0] == "R":
            return cls.RIGHT
        else:
            return cls.LEFT
        

class Spin:
    current_position: int = 50 # starts at 50
    index = 0
    position_history: list[dict] # index, start position, end position

    def __init__(self, movements: list[str]):
        self.movements = movements
        self.position_history = []
        self.hits_on_zero_first = 0
        self.hits_on_zero_second = 0
        self.max_index = len(movements)

    def __iter__(self):
        """Using this as a chance to play with the __iter__ and __next__ dunders."""
        return self.movements

    def __next__(self) -> Self:
        try:
            self._set_current_position()
            self.index += 1
        except IndexError:
            print(f"Turns complete (total turns: {self.index})")
            print(f"Total times crossed zero: {self.hits_on_zero_second} "
                  f"Total times landed on zero after end: {self.hits_on_zero_first}")

    @classmethod
    def get_example(cls):
        example_movements = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
        return cls(movements=example_movements)

    @classmethod
    def get_parsed_list(cls):
        return cls(movements=PARSED_LIST)

    def run(self):
        for _ in range(self.max_index):
            next(self)

    def display_stats(self):
        for k, v in self.__dict__.items():
            print(f"{k}: {v}")

    def display_history(self):
        for d in self.position_history:
            print(d)

    def _set_current_position(self) -> None:
        i = self.index
        movement = self.movements[i]

        direction = Direction.from_movement(movement)
        steps = int(movement[1:])
        inc_or_dec = direction.multiplier()

        start = self.current_position
        print(f"Starting from {start}. "
              f"Shifting {steps} steps to the {direction.display()}.")

        for step in range(steps):
            self.current_position += 1 * inc_or_dec

            if self.current_position == 100:
                self.current_position = 0

            if self.current_position == -1:
                self.current_position = 99

            if self.current_position == 0:
                self.hits_on_zero_second += 1

        if self.current_position == 0:
            print("CLICK! Landed on 0 after turn ended.")
            self.hits_on_zero_first += 1

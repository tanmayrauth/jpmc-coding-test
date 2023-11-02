import os
import json
from constants import SEAT_FILE_PATH, SEAT_ROWS, SEATS_IN_ROW


def load_reserved_seats():
    """
        This load function helps in maintaing the stateful behaviour ofn this application (i.e to maintain the state of reserved seats)
    """

    if os.path.exists(SEAT_FILE_PATH):
        with open(SEAT_FILE_PATH, "r") as file:
            return json.load(file)
    else:
        return {}

def save_reserved_seats(seats):
    """
        This save function helps in storing the stateful behaviour ofn this application (i.e to store the state of reserved seats)
    """
    with open(SEAT_FILE_PATH, "w") as file:
        json.dump(seats, file)


def is_valid_seat(row, seat):
    return row in range(SEAT_ROWS) and seat in range(SEATS_IN_ROW)



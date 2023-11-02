import os
import json
from constants import SEAT_FILE_PATH, SEAT_ROWS, SEATS_IN_ROW, Command, Result


def load_reserved_seats():
    if os.path.exists(SEAT_FILE_PATH):
        with open(SEAT_FILE_PATH, "r") as file:
            return json.load(file)
    else:
        return {}

def save_reserved_seats(seats):
    with open(SEAT_FILE_PATH, "w") as file:
        json.dump(seats, file)


def is_valid_seat(row, seat):
    return row in range(SEAT_ROWS) and seat in range(SEATS_IN_ROW)



from enum import StrEnum

# Constants
SEAT_ROWS = 20
SEATS_IN_ROW = 8
SEAT_FILE_PATH = "storage/reserved_seats.json"


class Command(StrEnum):
    BOOK = "BOOK"
    CANCEL = "CANCEL"

class Result(StrEnum):
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"
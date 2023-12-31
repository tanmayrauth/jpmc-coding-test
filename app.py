import sys
from constants import  Command, Result
from helper import load_reserved_seats
from commands import get_command


def run_command(command, row, seat, num_seats, reserved_seats):
    """
    Executes the specified command (BOOK or CANCEL) based on the provided arguments.
    
    Args:
        command (function): The command function (BOOK or CANCEL) to execute.
        row (int): The row number of the seat.
        seat (int): The seat number within the row.
        num_seats (int): The number of seats to book or cancel.
        reserved_seats (dict): A dictionary representing the current reserved seats.
    """

    if not command:
        print(Result.FAIL)
        return
    
    if command(row, seat, num_seats, reserved_seats):
        print(Result.SUCCESS)
    else:
        print(Result.FAIL)


def main():

    if len(sys.argv) != 4:
        print(Result.FAIL)
        return
    
    action, seat_identifier, num_seats = sys.argv[1], sys.argv[2], int(sys.argv[3]) # Loading command and seat info from sys args
    row, seat = ord(seat_identifier[0].upper()) - ord('A'), int(seat_identifier[1])

    reserved_seats = load_reserved_seats()
    command = get_command(action)

    run_command(command, row, seat, num_seats, reserved_seats )
    


if __name__ == "__main__":
    main()

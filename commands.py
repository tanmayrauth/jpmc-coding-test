from helper import save_reserved_seats, is_valid_seat
from constants import  Command, Result


def book_seats(row, start_seat, num_seats, reserved_seats):
    if not (is_valid_seat(row, start_seat) and is_valid_seat(row, start_seat + num_seats - 1)):
        return False
    
    for seat in range(start_seat, start_seat + num_seats):
        if reserved_seats.get(str(row), {}).get(str(seat)):
            return False
    
    for seat in range(start_seat, start_seat + num_seats):
        reserved_seats.setdefault(str(row), {})[str(seat)] = True
    
    save_reserved_seats(reserved_seats)
    return True


def cancel_seats(row, start_seat, num_seats, reserved_seats):
    for seat in range(start_seat, start_seat + num_seats):
        if not is_valid_seat(row, seat) or not reserved_seats.get(str(row), {}).get(str(seat)):
            return False
    
    for seat in range(start_seat, start_seat + num_seats):
        del reserved_seats[str(row)][str(seat)]
    
    if not reserved_seats[str(row)]:
        del reserved_seats[str(row)]
    
    save_reserved_seats(reserved_seats)
    return True



def get_command(action):

    action_mapping = { Command.BOOK : book_seats, Command.CANCEL : cancel_seats }
    return action_mapping.get(action, None)

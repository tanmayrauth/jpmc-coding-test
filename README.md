# Flight Booking System

## Project Structure

- **app.py:** Main file of the application. Contains the entry point and user interface logic.
- **commands.py:** File containing functions for handling booking (`BOOK`) and cancellation (`CANCEL`) commands.
- **constants.py:** File containing constant values used in the application.
- **helper.py:** File containing helper functions for persistence (LOAD) and (STORE) functions using json file
- **test_app.py:** Unit test file for testing functions in `app.py`.
- **test_commands.py:** Unit test file for testing functions in `commands.py`.

## Run Program

To run the application, execute `app.py` in a Python environment:
- To book a seat: 
- To cancel a reservation:

```bash
python3 app.py BOOK A1 2
python3 app.py CANCEL A1 2
```


## Unit Tests
To run the unit tests, execute the respective test files:

```bash
python3 test_app.py
python3 test_commands.py
```

The project does not have external dependencies beyond Python's standard library.

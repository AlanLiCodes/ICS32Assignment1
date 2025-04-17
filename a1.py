# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Alan Li
# liy70@uci.edu
# STUDENT ID
from command_parser import CommandParser

def main():
    parser = CommandParser()
    while True:
        try:
            command = input("").strip()
            if command.upper() == 'Q':
                break
            parser.parse_and_execute(command)
        except Exception:
            print("ERROR")

if __name__ == "__main__":
    main()


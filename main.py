from functions import *

def main():
    while True:
        welcome()
        game()
        if play_again():
            continue
        else:
            break


if __name__ == "__main__":
    main()
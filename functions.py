import random
import datetime
import time

def separator():
    print("-" * 30)


def welcome():
    print("Hi there!")
    separator()
    print("I have generated a random 4 digit number for you.", "Let's play a bulls and cows game.", sep="\n")
    separator()
    print("Enter a number:")
    separator()


def generate():
    repeat = True
    while repeat:
        answer = str(random.randint(1000, 9999))
        for digit in answer:
            if answer.count(digit) > 1:
                break
            else:
                continue
        else:
            repeat = False
    return answer

def find_duplicates(n):
    for char in n:
        counts = n.count(char)
        if counts > 1:
            return True
        else:
            continue
    else:
        return False


def correct_input():
    while True:
        n = str(input())
        if n[0] == "0" or find_duplicates(n) or len(n) != 4:
            print("Input number does not follow the game rules, please try again.")
            continue
        else:
            return n



def game():
    start_time = time.time()
    answer = generate()
    n_tries = 1
    while True:
        n = correct_input()
        bulls = []
        cows = []
        for index, digit in enumerate(n):
            if digit == answer[index]:
                bulls.append(1)
                cows.append(0)
            elif digit in answer:
                bulls.append(0)
                cows.append(1)
            else:
                cows.append(0)
                bulls.append(0)
        n_bulls = sum(bulls)
        n_cows = sum(cows)
        outcome = "{} {}, {} {}".format(n_bulls, "bulls" if n_bulls != 1 else "bull", n_cows,
                                      "cows" if n_cows != 1 else "cow")
        print(outcome)
        separator()
        if n_bulls == 4:
            date = datetime.datetime.now()
            end_time = time.time()
            full_time = round(end_time - start_time, 2)
            break
        else:
            n_tries += 1
            continue
    statistics(answer, n_tries, full_time)
    return end(n_tries, answer, full_time)



def end(n_tries, answer, full_time):
    tries = "tries" if n_tries != 1 else "try"
    print(f"Congratulations, you have guessed the correct number {answer}, it took you {n_tries} {tries} and {full_time} seconds.")


def play_again():
    while True:
        question = input("Do you want to play again? Y/N ")
        if question == "Y" or question == "y":
            return True
        else:
            return False

def statistics(number, n_tries, time):
    with open("game_stat", "a") as f:
        f.write("{}, {}, {}, {} \n".format(datetime.datetime.now(), number, n_tries, time))

if __name__ == "__main__":
    while True:
        welcome()
        game()
        if play_again():
            continue
        else:
            break
import random


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


def game():
    answer = generate()
    print(answer)
    n_tries = 1
    while True:
        n = str(input())
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
        vypis = "{} {}, {} {}".format(n_bulls, "bulls" if n_bulls != 1 else "bull", n_cows,
                                      "cows" if n_cows != 1 else "cow")
        print(vypis)
        separator()
        if n_bulls == 4:
            break
        else:
            n_tries += 1
            continue
    return end(n_tries, answer)


def end(n_tries, answer):
    print(f"Congratulations, you have guessed the correct number {answer}, it took you {n_tries} tries.")


def main():
    welcome()
    game()


main()
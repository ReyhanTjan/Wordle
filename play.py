from wordle import Wordle
from letter_state import LetterState
from colorama import Fore
import random


def main():
    word_set = load_word_set(r"data\wordle5_letter.txt")
    secret = random.choice(list(word_set))
    print("Hello Wordle!")
    wordle = Wordle(secret)

    while wordle.can_attempt:
        x = input(Fore.WHITE + '\nType your guess: ')

        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f'word must be {wordle.WORD_LENGTH} characters long!'+ Fore.RESET)
            continue 
        if not x.upper() in word_set:
            print(Fore.RED + x.upper() + " is not a valid word!")
            continue

        wordle.attempt(x)
        # result = wordle.guess(x)
        # print(*result, sep= '\n')
        display_results(wordle)
            

    if wordle.is_solved:
        print('You have solved the puzzle')
    else:
        print('Better luck next time')
        print(f'The word is: {secret}')
            

def display_results(wordle: Wordle):
    print("\nGuess:")
    lines = []
    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)
    for _ in range(wordle.remaining_attempts):
        lines.append(" ".join(["_"] * wordle.WORD_LENGTH))
    
    draw_boarder(lines)
    

def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for i in f.readlines():
            word = i.strip().upper()
            word_set.add(word)
    return word_set


def convert_result_to_color(result: list[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)
    return " ".join(result_with_color)


def draw_boarder(lines: list[str], size: int=9, pad: int=1):
    content_length = size + pad * 2
    top_boarder = Fore.RESET + "┌" + "─"* content_length + "┐"
    bottom_boarder = "└" + "─"* content_length + "┘"
    space = " " * pad
    print(top_boarder)
    for i in lines:
        print("│" + space + i + space + "│")
    print(bottom_boarder)


if __name__ == '__main__':
    main()
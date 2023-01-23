import random
import re
import sys
from rich.console import Console
from rich.theme import Theme

warning = 10

def main():

    custom_theme = Theme({
        'correct': ' bold black on green',
        'wrong': 'bold black on yellow',
        'unexist': 'bold black on white',
        'default' : 'bold black on black'
    })

    console_theme = Console(theme=custom_theme)
    welcome()
    level = ask_level()
    equation = game_setup(level)
    equation = '24+18=42'
    #print(equation) #for trial
    # count the lenght of equation, use that as the length of answer.
    digit = len(equation)

    letters = [[{'   ': 'default'} for i in range(digit)] for j in range(6)]
    for i in range(6):

        '''show all attempts'''
        for word in letters:
            for letter in word:
                for key, value in letter.items():
                    console_theme.print(key, style = value, end="")
                    console_theme.print(' ', end="")
            print()
            print()


        answer = get_answer(level, digit)
        validation , result = assessment(equation, answer)
        letters = comparison(answer, letters, result, i)
        print(f'Your Guess: {answer}')
        if validation:
            break

    for word in letters:
            for letter in word:
                for key, value in letter.items():
                    console_theme.print(key, style = value, end="")
                    console_theme.print(' ', end="")
            print()
            print()

    if equation != answer:
        print('Game Over!!!!! You have no chances left, and your guess still not right')
        print(f'The right answer is {equation}')
    else:
        print('You are right, Congratulation!!! You win the game')

def welcome():
    print("               Welcome to ARITHMATHGEEK! \n               Let's see how good you at math.")
    print('Instruction:\n' +
    '1. You need to guess the right arithmetic expression. it contains only addition and substraction.\n'
    '2. You win only when you guess it right with the chances you have.\n'
    '3. You have to input the character as much as the number of the block in a row.\n'
    '4. The block initially black. it means that you still not guess it. the number of the black row is decreased incrementally as you guess it.\n'
    '5. You have to input your guess by input the expression ( include equal sign, operator, and with no spaces between each character.\n'
    '6. The block turns green (🟩)if the character you put into the expression is both exist in the answer and in right position.\n'
    '7. The block turns yellow (🟨) if the character you put into the expression is exist in the answer but in the wrong position.\n'
    '8. The blok turns white (⬜) if the character you put into expession is not exist in the answer.\n'
    '9. You have 6 chances to guess right the math equation\n'
    '10. You have to follow the instruction by the game, you have 10 warnings. everytime you break the rule, the warning decreased by 1.\n'
    '11. Until you have no warning left. and you still break the law. you quit from the game\n'
    '12. You can exit the game anytime using (ctrl + d)'
    )

    print("\n before we start the game, choose which dificulties you wanna play.\n 1. Easy\n 2. Medium\n 3. Hard\n To choose the difficulties, input just the number not words, e.g. type 1 to choose easy.")


def comparison(answer, letters, result, i):
    for n in range(len(answer)):
        if result[n] == '2':
            x = ' ' + answer[n] + ' '
            letters[i][n] = { x : 'correct'}
        elif result[n] == '1':
            x = ' ' + answer[n] + ' '
            letters[i][n] = { x : 'wrong'}
        else:
            x = ' ' + answer[n] + ' '
            letters[i][n] = { x : 'unexist'}
    return letters

##Level Setup
# ask user to choose level(1,2,3)
def ask_level():
    global warning
    while True:
        try:
            level = int(input('What difficulties you wanna play: '))
            if level_verification(level):
                return level
        except EOFError:
            sys.exit('\nYou choose to exit the game. Thank you for playing, see you next time')
        except ValueError:
            print('Value inputted is wrong, please input the right one')
            warning -= 1
            if warning < 0:
                sys.exit('You lose the game because you keep violate the rule')
            print(f"There's only {warning} warnings left")
            pass
        # Level 1 = 1 digit (0-9)
    # Level 2 = 2 digit (10-99)
    # level 3 = 3 digit (100-999)

def level_verification(n):
    if not 1 <= int(n) <= 3:
        raise ValueError
    return True

##Game Setup
def game_setup(s):
    def pick_num(n):
        match n:
            case 1:
                z = 9
            case 2:
                z = 99
            case 3:
                z = 999
        return random.randint(0,z)
    A = pick_num(s)
    B = pick_num(s)
    operator = ['+','-']
    C = random.choice(operator)
    D = '='
    if C == '+':
        E = A + B
    else:
        if int(A) < int(B):
            A, B = B, A
        E = A - B
    # B = pick random number between 0-9, how many digit is depend on the level
    # C = pick random beween [+, -]
    # D = '='
    # E = A C B
    equation1 = str(E) + D + str(A) + C + str(B)
    equation2 = str(E) + D + str(B) + C + str(A)
    equation3 = str(A) + C + str(B) + D + str(E)
    equation4 = str(B) + C + str(A) + D + str(E)
    arrangement1 = [equation1, equation2, equation3, equation4]
    arrangement2 = [equation1, equation3]

    if C == '+':
        equation = random.choice(arrangement1)
    else:
        equation = random.choice(arrangement2)
    return equation
# if C == '+'
    # equation option (pick one of them by random)
        # E D A C B
        # E D B C A
        # A C B D E
        # B C A D E
# if C == '-'
    # euation option (pick one of them by random)
        #if A < B:
            # A, B = B, A
        # E D A C B
        # A C B D E

# A = pick random number between 0-9, how many digit is depend on the level

##game realization
#loop for guess
    # loop for user input
        # ask the user for input
        # process the input using the Regular expression, make sure the equation input by user is right. based on the result or format
            # ask back if the input not match RE

def get_answer(m, n):
    global warning
    k = m + 1
    while True:
        try:
            print(f'The equation is {n} character.')
            answer = input('Enter your answer, please: ').strip()
            if len(answer) != n:
                raise ValueError (f'Your input is not {n} character')
#myregex still need to be edited, how to make variable in regex
            my_regex1 = r"^([0-9]{1,4})=([0-9]{1,3})(\+|-)([0-9]{1,3})$"
            #my_regex1 = r"^([0-9]{1," + str(k) + "})=([0-9]{1," + str(m) + "})(\+|-)[0-9]({1," + str(m) + "})$"
            #print(my_regex1)
            #my_regex2 = r"^([0-9]{1," + str(m) + "})(\+|-)([0-9]{1," + str(m) + "})=([0-9]{1," + str(k) + "})$"
            my_regex2 = r"^([0-9]{1,3})(\+|-)([0-9]{1,3})=([0-9]{1,4})$"
            #print(my_regex2)
            if x := re.search(my_regex1, answer):
                if x.group(3) == '+':
                    if int(x.group(1)) != int(x.group(2)) + int(x.group(4)):
                        print('The equation you input is not right, C is not equal to A + B  ( C !=A + B ). Please input the right one !!')
                        raise ValueError
                else:
                    if int(x.group(1)) != int(x.group(2)) - int(x.group(4)):
                        print('The equation you input is not right, C is not equal to A - B  ( C !=A - B ). Please input the right one !!')
                        raise ValueError

            elif x := re.search(my_regex2, answer):
                if x.group(2) == '+':
                    if int(x.group(4)) != int(x.group(1)) + int(x.group(3)):
                        print('The equation you input is not right, A + B is not equal to C (A + B != C). Please input the right one !!')
                        raise ValueError
                else:
                    if int(x.group(4)) != int(x.group(1)) - int(x.group(3)):
                        print('The equation you input is not right, A - B is not equal to C (A - B != C). Please input the right one !!')
                        raise ValueError
            else:
                print('Your input is not accepted because of wrong format. input should have no spaces')
                raise ValueError
            return answer
        except EOFError:
            sys.exit('\nYou choose to exit the game. Thank you for playing, see you next time')
        except ValueError:
            warning -= 1
            if warning < 0:
                sys.exit('You lose the game because you keep violate the rule')
            print(f"There's only {warning} warnings left")
            pass
# if Value Error, back to the first of the loop

# input validation
        # first wall of the input validation
        # second wall of the input validation
    # show the result back to the user
def assessment(x, y):
    validation = True
    result = ''
    guess_progress = ''
    only_in = ''
    for i in range(len(y)):
            if y[i]== x[i]:
                guess_progress += y[i]

    for i in range(len(y)):
        code = 0
        if y[i] in x:
            if x[i] == y[i]:
                code = 2
            elif (x.count(y[i]) - (guess_progress.count(y[i]) + only_in.count(y[i]))) >= 1:
                code = 1
                only_in += y[i]
        result += str(code)

    for i in range(len(x)):
        if result[i] != '2':
            validation = False
            break
    return (validation, result)

if __name__ == '__main__':
    main()
from questions import QUESTIONS
from random import randint

def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''

    return question["answer"] == answer      #remove this


def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    ques = QUESTIONS[ques]
    delete_key_count = 0
    while delete_key_count <= 2:
        temp = randint(1,4)
        if ques["answer"] != temp:
            temp = "option" + str(temp)
            ques[temp] = ""
            delete_key_count += 1
    return ques
    



def kbc():
    '''pass
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    min_reward = 0
    prize = 0
    lifeline_used = False
    
    
    i = 0
    while i < 15:
        print(f'\tQuestion {i + 1}: {QUESTIONS[i]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')

        # check for the input validations
        if ans.lower() == 'quit' : break
        elif ans.lower() == 'lifeline' and not lifeline_used and i != 14 or ans.lower() == 'll': 
            if not lifeline_used and i<14:
                lifeline_used = True
                question = lifeLine(i)
                print(f'\tQuestion {i + 1}: {question["name"]}' )
                print(f'\t\tOptions:')
                print(f'\t\t\tOption 1: {question["option1"]}')
                print(f'\t\t\tOption 2: {question["option2"]}')
                print(f'\t\t\tOption 3: {question["option3"]}')
                print(f'\t\t\tOption 4: {question["option4"]}')
                ans =  ans = input('Your choice ( 1-4 ) : ')
            else:
                print("Lifeline already used!!")
                continue
        if '1'<=ans.lower()>='4':
            print("Invalid Input!!")
            continue

        
        if isAnswerCorrect(QUESTIONS[i], int(ans) ):
            # print the total money won.
            # See if the user has crossed a level, print that if yes
            if i == 4:
                min_reward = 10000
            elif i == 10:
                min_reward = 320000
            prize += QUESTIONS[i]["money"]
            print('\nCorrect !')

        else:
            # end the game now.
            # also print the correct answer
            prize = min_reward
            print('\nIncorrect !')
            break
        i += 1
    # print the total money won in the end.
    print("Amount you win is ", prize)


kbc()
import re

ACCEPTED = "Accepted"
PRESENTATION = "Presentation Error"
WRONG = "Wrong Answer"


def print_answer(case, verdict):
    print("Run #" + str(case) + ": " + verdict)


def compare_numeric(correct_answers, team_answers):
    correct_answers_combined = ""
    team_answers_combined = ""

    for line in correct_answers:
        correct_answer = re.sub('[\W_]+', '', line.strip())
        correct_answer = re.sub('[a-zA-Z]+', '', correct_answer.strip())

        correct_answers_combined += correct_answer

    for line in team_answers:
        team_answer = re.sub('[\W_]+', '', line.strip())
        team_answer = re.sub('[a-zA-Z]+', '', team_answer.strip())

        team_answers_combined += team_answer

    return correct_answers_combined == team_answers_combined


def check_accepted(correct_answers, team_answers):
    if len(correct_answers) == len(team_answers):
        for index in range(0, len(correct_answers)):
            if correct_answers[index] != team_answers[index]:
                return False

        return True
    else:
        return False


def check_presentation(correct_answers, team_answers):
    # all digits match
    if compare_numeric(correct_answers, team_answers):
        # we're in the presentation error domain
        correct_answers_combined = ""
        team_answers_combined = ""

        for answer in correct_answers:
            correct_answers_combined += answer + '\n'

        for answer in team_answers:
            team_answers_combined += answer + '\n'

        # if they don't match then the presentation error is valid
        # if they match then the presentation error is not valid
        return correct_answers_combined != team_answers_combined
    else:
        # digits don't match so we're not in the presentation error
        return False


def evaluate_answer(correct_answers, team_answers):
    # check if accepted: all characters should match
    if check_accepted(correct_answers, team_answers):
        return ACCEPTED
    else:
        # check presentation
        if check_presentation(correct_answers, team_answers):
            return PRESENTATION
        else:
            return WRONG


count = 1

while True:
    try:
        correct_answer_count = int(input())

        if correct_answer_count == 0:
            break

        correct_answers = []

        for a_count in range(0, correct_answer_count):
            correct_answers.append(input())

        team_answer_count = int(input())
        team_answers = []

        for a_count in range(0, team_answer_count):
            team_answers.append(input())

        print_answer(count, evaluate_answer(correct_answers, team_answers))

        count += 1

    except EOFError:
        break

import re

INVALID_PROBLEMS_ERROR = "Error: Too many problems."
INVALID_OPERATORS_ERROR = "Error: Operator must be '+' or '-'."
INVALID_OPERANDS_ERROR = "Error: Numbers must only contain digits."
INVALID_OPERANDS_LENGTH_OF_NUMBERS = "Error: Numbers cannot be more than four digits."
FOUR_WHITESPACE = "    "


def calculate(problems, showResult):
    result = ""
    first_row = ""
    second_row = ""
    third_row = ""
    result_row = ""
    for problem in problems:
        input1, input2, operator = problem
        max_len = max(len(str(input1)), len(str(input2)))
        first_row += f"{input1:>{max_len+2}}" + FOUR_WHITESPACE
        second_row += f"{operator} {input2:>{max_len}}" + FOUR_WHITESPACE
        third_row += "-"*(max_len+2) + FOUR_WHITESPACE
        if showResult:
            ans = input1+input2 if operator == '+' else input1-input2
            result_row += f"{ans:>{max_len+2}}" + FOUR_WHITESPACE
    first_row = first_row.rstrip()
    second_row = second_row.rstrip()
    third_row = third_row.rstrip()
    result += f"{first_row}\n{second_row}\n{third_row}"
    if showResult:
        result_row = result_row.rstrip()
        result += f"\n{result_row}"
    return result


def arithmetic_arranger(problems, showResult=False):
    valid_problems = []
    if len(problems) > 5:
        return INVALID_PROBLEMS_ERROR

    for problem in problems:

        if '+' not in problem and '-' not in problem:
            return INVALID_OPERATORS_ERROR

        input1, input2 = re.split(' \+ | - ', problem)
        try:
            input1 = int(input1)
            input2 = int(input2)
        except ValueError:
            return INVALID_OPERANDS_ERROR

        if len(str(input1)) > 4 or len(str(input2)) > 4:
            return INVALID_OPERANDS_LENGTH_OF_NUMBERS
        operator = '+' if '+' in problem else '-'
        valid_problems.append((input1, input2, operator))

    arranged_problems = calculate(valid_problems, showResult)
    return arranged_problems


result = arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)
print(result)


def fix_parentheses(string: str) -> str:
    new_string = ""
    count_open = 0
    count_close = 0
    for i in range(len(string)):
        if string[i] == ")" and len(string) == 1:
            new_string += "()"
        if string[i] == ")" and i < len(string) - 1:
            if string[i + 1] == ")":
                count_close += 1
            elif string[i] == ")" and string[i + 1] == "(":
                count_close += 1
                if i > 0 and string[i - 1] == "(" or string[i] == "(" and string[i + 1] == ")":
                    new_string += (count_close * ")")
                else:
                    new_string += (count_close * "(")
                    new_string += (count_close * ")")
                count_close = 0
            elif string[i] == ")" and i > 0:
                if string[i - 1] == ")" or string[i - 1] == "(":
                    count_close -= 1
            elif i == 0 and string[i + 1] == "(":
                new_string += "()"
        if string[i] == "(" and i != len(string):
            count_open += 1
            new_string += string[i]
            if i < len(string) - 1:
                if string[i] == "(" and string[i + 1] == ")":
                    count_open -= 1
                    if len(string) == 2:
                        new_string += ")"
            elif string[i] == "(" and i == len(string):
                new_string += ")"
    if count_open > 0:
        new_string += (count_open * ")")
    if count_close > 0:
        new_string += count_close * "("
        new_string += count_close * ")"
    return new_string

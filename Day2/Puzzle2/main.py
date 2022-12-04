
def game_outcome(opp_choice, req_outcome):
    # outcome now is a list of two, the int outcome and the string my_choice
    outcome = [0, '']

    if (req_outcome == 'X'):
        outcome[0] = 0
    elif (req_outcome =='Y'):
        outcome[0] = 3
    else:
        outcome[0] = 6

    if(opp_choice == 'A'):
        if(req_outcome == 'X'):
            outcome[1] = 'Z'
        elif(req_outcome == 'Y'):
            outcome[1] = 'X'
        else:
            outcome[1] = 'Y'
    elif(opp_choice == 'B'):
        if(req_outcome == 'X'):
            outcome[1] = 'X'
        elif(req_outcome == 'Y'):
            outcome[1] = 'Y'
        else:
            outcome[1] = 'Z'
    else:
        if(req_outcome == 'X'):
            outcome[1] = 'Y'
        elif(req_outcome == 'Y'):
            outcome[1] = 'Z'
        else:
            outcome[1] = 'X'

    return outcome


def process_input():
    file = open('input.txt', 'r')

    total_sum = 0
    outcome = []

    for line in file:
        line_list = line.split()
        outcome = game_outcome(line_list[0], line_list[1])
        total_sum += outcome[0]
        if (outcome[1] == 'X'):
            total_sum += 1
        elif (outcome[1] == 'Y'):
            total_sum += 2
        else:
            total_sum += 3

    return total_sum

def main():
    # process input file
    total_score = process_input()
    print(total_score)



if __name__ == "__main__":
    main()
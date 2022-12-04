
def game_outcome(opp_choice, my_choice):
    outcome = 0
    if(opp_choice == 'A'):
        if(my_choice == 'X'):
            outcome = 3
        elif(my_choice == 'Y'):
            outcome = 6
        else:
            outcome = 0
    elif(opp_choice == 'B'):
        if(my_choice == 'X'):
            outcome = 0
        elif(my_choice == 'Y'):
            outcome = 3
        else:
            outcome = 6
    else:
        if(my_choice == 'X'):
            outcome = 6
        elif(my_choice == 'Y'):
            outcome = 0
        else:
            outcome = 3

    return outcome


def process_input():
    file = open('input.txt', 'r')

    total_sum = 0
    outcome = 0

    for line in file:
        line_list = line.split()
        total_sum += game_outcome(line_list[0], line_list[1])
        if (line_list[1] == 'X'):
            total_sum += 1
        elif (line_list[1] == 'Y'):
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
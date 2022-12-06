
def check_elf_pair(elf_1_bounds, elf_2_bounds):
    # input is two lists, each with a lower and upper bound, inclusive
    elf_1_lower_bound, elf_1_upper_bound = elf_1_bounds[0], elf_1_bounds[1]
    elf_2_lower_bound, elf_2_upper_bound = elf_2_bounds[0], elf_2_bounds[1]

    if (elf_2_lower_bound <= elf_1_lower_bound <= elf_2_upper_bound or elf_2_lower_bound <= elf_1_upper_bound <= elf_2_upper_bound):
        return True
    elif (elf_1_lower_bound <= elf_2_lower_bound <= elf_1_upper_bound or elf_1_lower_bound <= elf_2_upper_bound <= elf_1_upper_bound):
        return True
    else:
        return False


def find_overlaps(elf_1_list, elf_2_list):
    total_overlaps = 0

    for pair in range(len(elf_1_list)):
        if (check_elf_pair(elf_1_list[pair], elf_2_list[pair])):
            total_overlaps += 1

    return total_overlaps

def process_input():
    # return two lists of lists of bounds
    file = open('input.txt', 'r')

    elf_1_list = []
    elf_2_list = []

    for line in file:
        filtered_line_1, filtered_line_2 = line.split(',')
        
        elf_1_starting_bound, elf_1_ending_bound = filtered_line_1.split('-')
        elf_2_starting_bound, elf_2_ending_bound = filtered_line_2.split('-')
        
        elf_1_bounds = [int(elf_1_starting_bound), int(elf_1_ending_bound)]
        elf_2_bounds = [int(elf_2_starting_bound), int(elf_2_ending_bound)]
        
        elf_1_list.append(elf_1_bounds)
        elf_2_list.append(elf_2_bounds)

    return elf_1_list, elf_2_list



def main():
    # process input file
    elf_1_list, elf_2_list = process_input()

    total_overlaps = find_overlaps(elf_1_list, elf_2_list)

    print(total_overlaps)


if __name__ == "__main__":
    main()
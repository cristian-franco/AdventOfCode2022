

def process_input():
    elf_list = []

    file = open('input.txt', 'r')

    single_elf_sum = 0
    for line in file:
        if(line != '\n'):
            single_elf_sum += int(line)
        else:
            elf_list.append(single_elf_sum)
            single_elf_sum = 0

    return elf_list


def main():
    # process input file
    elf_list = process_input()

    # sort list in descending order
    elf_list.sort(reverse=True)
    print(elf_list[0] + elf_list[1] + elf_list[2])
    



if __name__ == "__main__":
    main()
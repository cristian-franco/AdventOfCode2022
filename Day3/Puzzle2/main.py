
def find_similar_item(overall_items):
    shared_item = ''

    for item in overall_items:
        if (overall_items[item] == 2):
            shared_item = item

    return shared_item


def process_input():
    # return list of chars that we will then score
    file = open('input.txt', 'r')

    shared_items = []

    elf_counter = 1
    hashmap1 = {}
    hashmap2 = {}
    hashmap3 = {}
    hashmap4 = {}

    for line in file:
        elf_items = line.rstrip()
        if (elf_counter == 1):
            for item in elf_items:
                hashmap1[item] = 0
        elif (elf_counter == 2):
            for item in elf_items:
                hashmap2[item] = 0
        else:
            for item in elf_items:
                hashmap3[item] = 0

            elf_counter = 0
            unique_items_1 = list(hashmap1.keys())
            unique_items_2 = list(hashmap2.keys())
            unique_items_3 = list(hashmap3.keys())

            for unique_item in unique_items_1:
                if (unique_item in hashmap4):
                    hashmap4[unique_item] += 1
                else:
                    hashmap4[unique_item] = 0

            for unique_item in unique_items_2:
                if (unique_item in hashmap4):
                    hashmap4[unique_item] += 1
                else:
                    hashmap4[unique_item] = 0

            for unique_item in unique_items_3:
                if (unique_item in hashmap4):
                    hashmap4[unique_item] += 1
                else:
                    hashmap4[unique_item] = 0

            shared_items.append(find_similar_item(hashmap4))
            hashmap1.clear()
            hashmap2.clear()
            hashmap3.clear()
            hashmap4.clear()

        elf_counter += 1    

    return shared_items

def main():
    # process input file
    shared_items = process_input()

    sum_priorities = 0

    for item in shared_items:
        if (item >= 'a' and item <= 'z'):
            sum_priorities += ord(item) - 96
        else:
            sum_priorities += ord(item) - 38

    print(sum_priorities)


if __name__ == "__main__":
    main()
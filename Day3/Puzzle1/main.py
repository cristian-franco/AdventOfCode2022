

def process_input():
    # return list of chars that we will then score
    file = open('input.txt', 'r')

    shared_items = []

    for line in file:
        compartment_1, compartment_2 = line[:len(line)//2], line[len(line)//2:]
        hashmap = {}

        for item in compartment_1:
            hashmap[item] = 0
        
        for item2 in compartment_2:
            if(item2 in hashmap):
                shared_items.append(item2)
                break

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
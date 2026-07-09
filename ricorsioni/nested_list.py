def count_leaf_nodes(input_list):
    if len(input_list) == 0:
        return 0
    else:
        counter = 0
        for element in input_list:
            #check if element is a list
            if type(element) == list:
                #if it's a list, we count its elements and call the function recursively
                counter += count_leaf_nodes(element)
            else:
                #else we add 1
                counter += 1
        return counter
if __name__ == "__main__":
    names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
    print(count_leaf_nodes(names))
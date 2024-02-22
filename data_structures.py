class DataProcessor:
    def sort_tuple(self, input_tuple):
        return tuple(sorted(input_tuple))

    def append_to_list(self, input_list, element):
        input_list.append(element)
        return input_list

    def update_dictionary(self, input_dict, key, value):
        input_dict[key] = value
        return input_dict

    def remove_from_set(self, input_set, element):
        input_set.discard(element)
        return input_set

if __name__ == "__main__":
    # Create an instance of DataProcessor
    processor = DataProcessor()

    # Test sorting a tuple
    tuple_to_sort = (4, 2, 7, 1, 9)
    sorted_tuple = processor.sort_tuple(tuple_to_sort)
    print("Sorted Tuple:", sorted_tuple)

    # Test appending to a list
    list_to_append = [1, 2, 3]
    appended_list = processor.append_to_list(list_to_append, 4)
    print("Appended List:", appended_list)

    # Test updating a dictionary
    dict_to_update = {'a': 1, 'b': 2}
    updated_dict = processor.update_dictionary(dict_to_update, 'c', 3)
    print("Updated Dictionary:", updated_dict)

    # Test removing from a set
    set_to_remove_from = {1, 2, 3, 4, 5}
    removed_set = processor.remove_from_set(set_to_remove_from, 3)
    print("Set after removal:", removed_set)

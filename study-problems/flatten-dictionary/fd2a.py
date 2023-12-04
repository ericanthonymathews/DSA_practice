def flatten_dictionary(dictionary):
    '''
    input: dictionary
    output: dictionary
    edgecases: empty keys, empty dictionary
    outliers: none

    0. recursive function
    0.5. perhaps the recursive function pseudorecursive
    1. iterate over the dictionary
        - if the input is a dictionary
        -> pass the dictionary into the function
        -> each recursive call of the function will write onto the result dictionary
        -> keep track of the key string somehow
    2. return result

    '''
    result = {}

    def dictionary_recursion(sub_dictionary, key):
        for key_name in sub_dictionary:
            if isinstance(sub_dictionary[key_name], dict):
                if key != '':
                    dictionary_recursion(
                        sub_dictionary[key_name], key + '.' + key_name)
                else:
                    dictionary_recursion(sub_dictionary[key_name], key_name)
            elif key_name != '':
                if key != '':
                    result[key + '.' + key_name] = sub_dictionary[key_name]
                else:
                    result[key_name] = sub_dictionary[key_name]
            else:
                result[key] = sub_dictionary[key_name]
    dictionary_recursion(dictionary, '')
    return result

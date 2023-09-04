def flatten_list(input_list):
    flattened = []
    for item in input_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        elif isinstance(item, int):
            
            flattened.append(item)
    return flattened

input_list = [1, 2, [3, 4, [5], [6]], 7, 8, 9]
result = flatten_list(input_list)
print(result)  
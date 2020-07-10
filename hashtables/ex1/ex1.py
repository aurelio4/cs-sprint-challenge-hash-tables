def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    data = {}

    for i in range(length):
        data[weights[i]] = i 

    for i in range(length):
        target = limit - weights[i]
        if target in data:
            if data[target] > i:
                return (data[target], i)
            else:
                return (i, data[target])

    return None
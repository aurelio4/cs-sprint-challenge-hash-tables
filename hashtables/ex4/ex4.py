def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    storage = {}
    result = []
    
    for num in a:
        storage[num] = 1
    
    for num in a:
        if (num*-1) in storage and num > 0:
            result.append(num)

    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

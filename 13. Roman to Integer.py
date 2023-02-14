def romanToInteger(list):

    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    total = 0

    for i in range(len(list)):
        if i + 1 < len(list) and values[list[i]] < values[list[i+1]]:
            total -= values[list[i]]
        else:
            total+= values[list[i]]
    return total




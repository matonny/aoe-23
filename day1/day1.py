f = open("input.txt", "r")
data = f.readlines()

def edgeDigits(target):
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    result = [0,0]
    for index, elem in enumerate(target):
        foundNum = False
        if elem.isnumeric():
            result[0] = elem
            break
        for num_index, word in enumerate(words):
            if target[index:index+len(word)] == word:
                result[0] = str(num_index + 1)
                foundNum = True
                break
        if foundNum:
            break
        
    for index, elem in enumerate(reversed(target)):
        foundNum = False
        if elem.isnumeric():
            result[1] = elem
            break
        for num_index, word in enumerate(words):
            if target[-index-len(word): -index] ==(word):
                result[1] = str(num_index + 1)
                foundNum = True
                break
        if foundNum:
            break
    return result
result = sum([int("".join(edgeDigits(x))) for x in data])
print(result)


def find_occurance(neddle, haystack):
    for i in range(len(haystack)):
        if haystack[i:len(neddle)] == neddle:
            return i
    return -1


print(find_occurance('world', 'helloworld'))
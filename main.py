
def find_occurance(neddle, haystack):
    for i in range(len(haystack)):
        print(haystack[i: len(neddle)])
        print(haystack[i:i+ len(neddle)])
        if haystack[i:i+len(neddle)] == neddle:
            return i
    return -1


print(find_occurance('world', 'helloworld'))
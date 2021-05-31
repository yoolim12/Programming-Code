N = int(input())

def groupword(word):
    word_set = set(word)
    if len(word_set) == len(word):
        return 1
    else:
        return 0
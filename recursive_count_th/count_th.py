'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

counter = []

def count_th(word):

    #counter = []

    if len(word) <= 1:
        return len(counter)

    #for i in range(len(word) - 1):
    if word[0] == "t" and word[1] == "h":
        #counter += 1
        counter.append('a')
        return count_th(word[2:])
        
    else:
        return count_th(word[1:])

word = "abcthxyz"

print(count_th(word))
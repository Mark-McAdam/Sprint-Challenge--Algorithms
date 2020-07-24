'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # string we are looking for
    str = 'th'
    
    # base case - str not found return 0
    if str not in word:
        return 0
    # recursive case 
    # if found do something 
    if str in word:
        
        # replace the th with foundit so its 
        # not counted on the next pass of recursion 
        word = word.replace(str, 'found', 1)
        #increment the count of found words 
        return count_th(word) + 1 
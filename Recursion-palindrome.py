def ispalindrome(word):
    word = word.lower().replace(" ", "")
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return ispalindrome(word[1:-1])

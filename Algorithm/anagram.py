def anagram(word1,word2):
    word1 = word1.replace(" ","").lower()
    word2 = word2.replace(" ","").lower()

    if len(word1)!=len(word2):
        return False
    
    dict = {}

    
    for letter in word1:                     # looping every letter in word1
        if letter not in dict:
            dict[letter] = 1
        else: dict[letter] += 1
    
    for letter in word2:                     # looping every letter in word2
        if letter in dict:
            dict[letter] -= 1
        else: return False

    for k in dict:
        if dict[k] != 0: return False
        pass

    return True

print(anagram("gokul kumar","ramuk lukog"))


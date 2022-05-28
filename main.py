# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = ''.join(word.split())
    anagram = ''.join(anagram.split())  
    if (sorted(word) == sorted(anagram)):
        return True
    else:
        return False

print(find_anagram("conversation", "voices rant on"))

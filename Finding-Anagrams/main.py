# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word= word.lower()
    anagram = anagram.lower()
    word= word.strip()
    anagram= anagram.strip()

    if sorted(word)==sorted(anagram):
        return "true"

    else: 
        return "false"
print (find_anagram("hello", "check"))
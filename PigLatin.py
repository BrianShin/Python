vowels = 'aeiou'

def piglatin(word):
    first = word[0] #checking the first letter of the word
    if first in vowels:
        word = word + 'yay'
        return word
    else:
        #keeps moving the first letter to the back until a vowel
        while word[0] not in vowels:
            word = word[1:] + word[0]
        word = word + 'ay'
        return word

sentence = input('into piglatin: ')
split = sentence.split()#splits the words in the sentence into variables

#taking each word in the sentence and putting it back into a list
translated = [piglatin(word) for word in split]
#combining the word list with a space between each word
translated = " ".join(translated)
print(translated)
    

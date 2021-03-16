sentence = input('enter the sentence')
characterCount = 0
wordCount = 0
for character in sentence:
        characterCount = characterCount + 1
        if(character == ' '):
                wordCount = wordCount + 1
print('number of character is')
print(characterCount)
print('number of words is')
print(wordCount)

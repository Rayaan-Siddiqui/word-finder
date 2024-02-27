guess_letters = input("Enter letters: ")
word_array = []
for i in guess_letters:
    word_array.append(i)

matched_words = []

wordsFile = open("./words.txt")

for y in wordsFile:
    if len(y) - 1 == len(guess_letters):
        counter = 0
        for x in y:
            for z in word_array:
                if x == z:
                    counter += 1
                continue
        if counter == len(guess_letters):
            matched_words.append(y)

    else:
        continue
print(matched_words)
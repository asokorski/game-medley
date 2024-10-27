



# word = ["a", "p", "p", "l", "e"]

# actual_word = ''.join(word)
# print(actual_word)


word = "apple"
hidden_word = []
for letter in word:
    hidden_word.append("_ ")
hidden_word = ''.join(hidden_word)
print(hidden_word)
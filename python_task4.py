def count_chars_occurences(sentence: str) -> dict:
    chars_occurences = {}
    for char in sentence:
        if char in chars_occurences:
            chars_occurences[char] += 1
        else:
            chars_occurences[char] = 1
    return chars_occurences

sentence = "pythonnohtyppy"
print(sentence)
print(count_chars_occurences(sentence))
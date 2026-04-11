def most_com_char(text: str) -> str:
    if text == '':
        return None

    max_char = text[0]

    for char in text:
        if text.count(char) > text.count(max_char):
            max_char = char

    return max_char


text = ""
result = most_com_char(text)
print(result)
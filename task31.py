def count_letters(text: str) -> dict[str, int]:
    letter_counts = {}


    for char in enumerate(text):
        if char[1].isalpha():
            if char[1] in letter_counts:
                letter_counts[char[1]] += 1
            else:
                letter_counts[char[1]] = 1
    return letter_counts

print(count_letters("assalomu alaykum"))
#print(count_letters("hello world"))
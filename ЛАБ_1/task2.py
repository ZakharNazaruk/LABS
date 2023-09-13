text = input("Введите текст: ").lower()

vowels = set("ёеыаоэяиюуeyuioa")

vowel_count = 0
consonant_count = 0

vowel_list = []

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
            vowel_list.append(char)
        else:
            consonant_count += 1

print("Количество гласных букв:", vowel_count)
print("Количество согласных букв:", consonant_count)

if vowel_count == consonant_count:
    print("Гласные буквы в тексте:", ' '.join(vowel_list))

words = text.split()
word_count = len(words)
print("Количество слов в тексте:", word_count)
text = "List comprehension"
vowels = [character for character in text if character.lower() in "aeiou"]

print(vowels)
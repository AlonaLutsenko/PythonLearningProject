word = input("Enter your word: ")
letter = input("Enter your letter: ")

if letter in word:
    print(f"This letter - '{letter}' is in the word - '{word}'")
else:
    print(f"This letter - '{letter}' is not in the word - '{word}'")
word = input("Enter a word:")

for ch in word:
    if ch in "aeiouAEIOU":
        print('First vowel found', ch)
    else:
        print("No vowel found.")
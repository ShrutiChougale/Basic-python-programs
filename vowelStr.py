s = input("Enter string: ")
count = 0

for char in s.lower():
    if char in "aeiou":
        count += 1

print("Vowels:", count)

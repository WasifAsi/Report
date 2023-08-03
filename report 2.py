#Variable

#Input
character = input("Enter the character stream: ")
character_count = {}

# Prosses and Output
for i in character:
    if i.isalpha() and i != ' ':
        i = i.lower()
        if i in character_count:
            character_count[i] += 1
        else:
            character_count[i] = 1

print("Alphabetical Character Count -")
for i, count in sorted(character_count.items()):
    print("\t", i, "=", count)

non_alphabetic_count = len(character.replace(" ", "")) - sum(character_count.values())
print("\nNon-Alphabetical Count -", non_alphabetic_count)
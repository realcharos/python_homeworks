txt = input(">> ")

vowels = "aeiou"
result = ""
count = 0

for i in range(len(txt)):
    result += txt[i]
    count += 1

    if count % 3 == 0 and i != len(txt) - 1:
        if txt[i] in vowels or (i + 1 < len(txt) and txt[i + 1] == "_"):
            continue
        result += "_"

print(result)

# file=open("my_file.txt")
# contents=file.read()

with open("my_file.txt") as file:
    contents=file.read()
    print(contents)

with open("my_file.txt",mode="w") as file:
    contents=file.write("LOLLOLOLOL")

with open("text.txt") as numbers:
    number_lst=numbers.readlines()
    number_lst = list(map(lambda s: s.strip(), number_lst))

print(number_lst)
print(contents)


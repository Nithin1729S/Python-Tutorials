with open("/Users/sures/Desktop/new_text.txt",mode="w") as file:
    file.write("Hi There Hello!!!")


with open("/Users/sures/Desktop/new_text.txt",mode="r") as file:
    contents=file.read()
    print(contents)

with open("../../newtxt.txt",mode='w') as file:
    file.write("World Hunger Solved")

with open("/Users/sures/PycharmProjects/newtxt.txt") as file:
    print(file.read())


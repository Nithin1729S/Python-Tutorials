enemies=1
def increase_enemies():
    #enemies+=1  This will create an error as this variable is not defined yet.
    global enemies #Allows to take the global enemies into the fucntion and modify it
    enemies +=1   #Usually dont modify global variables.Instead use return enemies + 1
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

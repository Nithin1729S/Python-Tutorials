enemies=1

def increase_enemies():
    enemies=2 #Here we are creating a completely new variable with local scope.We are not changing the value of the variable
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#Topic:Local Scope
#Exists within a function
def drink_potion():
    potion_strength=2 #Remember:This is created inside a function and can be used only inside the function.It has local scope.
    print(potion_strength)

drink_potion()
#print(potion_strength)  This gives an error.You have defined potion strenght inside the function and you cannot access it from outside the function.

#Topic:Global Scope
player_health=10 #This is globally defined variable.It is available inside and as well as outside a fucntion

def game():
    def drink_potion():
        potion_strength=2
        print(player_health) #Even though playerhealth was not defiined inside the function it can be used inside this function as it has global scope.

#Note:No such thing as block scope in python unlike c. If while for do not count as creating a local scoped variables.
game_level=3
def create_enemy():
    devils=["Skeleton","Zombie","Alien"]
    if game_level<5:
        new_devil=devils[0]
    print(new_devil)#new_devil is defined outside if statement too
#Remember:If you create a variable within a function then it is only available within that fucntion.But if you create a variable within an if block or while loop or a for loop or anything which has a indentation and a colon then that does not count as creating a seperate local scope.





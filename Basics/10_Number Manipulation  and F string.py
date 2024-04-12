print(8/3)
print(int(8/3))    #Type casting to a integer just chops off the extra stuff .It's not correct estimation.
print(round(8/3))
#you can even determine the precision of the estimation
print(round(8/3,2))  #Estimation to two decimal places
print(round(2.66666666,3))

result = 4/2
result /= 2    #result again divided by 2(this is a shorthad)
print(result)

Score = 0
Score += 1   #adds one again.Takes the previous version of the score and adds one to it
print(Score)

#F String : We cut down on a lot of manual labour with this
score = 0      #Integer
height = 1.7   #Floating Point
isWinning = True  #Boolean
#To print all these datatypes we need to typecast a lot .....to avoid that we use F String
print(f"Your score is {score} , your height is {height},you are winning is {isWinning}")
#this does all the work behind the scenes.f should be outside the quotes
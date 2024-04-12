import pandas
data=pandas.read_csv("squirrel_count.csv")
grey_squirrel_count=len(data[data["Primary Fur Color"]=="Gray"]) #contains all rows consisting gray squireels
red_squirrel_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrel_count=len(data[data["Primary Fur Color"]=="Black"])
print(grey_squirrel_count,black_squirrel_count,red_squirrel_count)

data_dict={
    "Fur Color":["Grey","Cinnamon","Black"],
    "Count":[grey_squirrel_count,red_squirrel_count,black_squirrel_count]
}

df=pandas.DataFrame(data_dict)
df.to_csv("squirrelcount.csv")



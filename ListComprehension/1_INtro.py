
numbers=[1, 2, 3, 4, 5]
new_list=[n+1 for n in numbers]
print(new_list)

name="Nithin"
lst=[letter for letter in name]
print(lst)

range_list=[2*i for i in range(1,5)]

names=["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]

short_names=[i for i in names if len(i)<5]
upperd_case=[i.upper() for i in names if len(i)>=5]
print(short_names,upperd_case)























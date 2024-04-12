import pandas
student_dict={'student':['Angela',"James","Lily"],
              "scores":[56,76,98]}

data=pandas.DataFrame(student_dict)

for (key,value) in student_dict.items():
    print(key,value)

for (idx,row) in data.iterrows():
    if row.student=="Angela":
        print(row)












































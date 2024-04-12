
def addition(n):
    return n + n

numbers = [1, 2, 3, 4]
result = map(addition, numbers)
print(result)
print(list(result))



string="".join(map(str,numbers))
print(string)

twotimes=list(map(lambda x:x+x,numbers))
print(twotimes)

ls1=[1,2,3]
ls2=[2,2,5]

sumlst=list(map(lambda x,y:x+y ,ls1,ls2))
print(sumlst)
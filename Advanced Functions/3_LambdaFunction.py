cube=lambda x:x*x*x
print(cube(3))


avg=lambda x,y,z:(x+y+z)/2
print(avg(3,5,5))

def appl(fx,value):
    return 6+fx(value)

print(appl(lambda x:x*x*x,2))

def paint_calc(height,width,cover):
    number_of_cans=round((height*width)/coverage)
    print(f"You'll need {number_of_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)    #Positional Arguments are used here


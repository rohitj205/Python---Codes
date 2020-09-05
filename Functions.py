def print_pattern(n):
    for i in range(n):
        s = ''
        for j in range(i + 1):
            s = s + '*'
        print(s)
n = int(input("Enter the Number:"))
print_pattern(n)


def calculate_area(dimension1,dimension2,shape="triangle"):

    if shape == "triangle":
        area = 1 / 2 * (dimension1 * dimension2)  # Triangle area is : 1/2(Base*Height)
    elif shape == "rectangle":
        area = dimension1 * dimension2  # Rectangle area is: Length*Width
    else:
        print("***Error: Input shape is neither triangle nor rectangle.")
        area = None  # If user didn't supply "triangle" or "rectangle" as shape then return None
    return area

# ------------------ Shape area exercise ------------------------- #
# Calculate area of triangle whose base is 10 and height is 5

base=10
height=5
triangle_area=calculate_area(base,height,"triangle")
print("Area of triangle is:",triangle_area)

# Calculate area of a rectangle whose length is 20 and width is 30
length=20
width=30
rectangle_area=calculate_area(length,width,"rectangle")
print("Area of rectangle is:",rectangle_area)

# Calculate area of a triangle without supplying shape argument in a function call
triangle_area=calculate_area(base,height) # Here third argument is missing
print("Area of triangle with no shape supplied: ",triangle_area)
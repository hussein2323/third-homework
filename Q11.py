def rectangle(Length, Width):
    area = Length * Width
    return area

# Example usage:
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print("The area of the rectangle is:", rectangle(length, width))
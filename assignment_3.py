
# Question 1

def draw_diamond(height):
    if height % 2 == 0:
        print("Height must be an odd number.")
        return
        
    mid = height // 2

    for i in range(height):
        spaces = ' ' * abs(mid-i)
        hashes = '#' * (height - 2 * abs(mid-i))
        print(spaces + hashes)

print("Diamond height 3:")
draw_diamond(3)

print("\nDiamond height 7:")
draw_diamond(7)

print("\nDiamond height 9:")
draw_diamond(9)

print("\nDiamond height 11:")
draw_diamond(11)

# Question 2

def draw_right_triangle(height):
    for i in range(1, height + 1):
        print('#' * i)

print("Right triangle height 3:")
draw_right_triangle(3)

print("\nRight triangle height 7:")
draw_right_triangle(7)

print("\nRight triangle height 9:")
draw_right_triangle(9)

print("\nRight triangle height 11:")
draw_right_triangle(11)

#Question 3

def compound_interest(principal, rate, years):
    for year in range(1, years + 1):
        interest = principal * rate
        principal += interest
        print(f"Year {year}: ${round(principal, 2)}")
    return principal

print("Compound interest for $1112 at 7% for 3 years:")
compound_interest(1112, 0.07, 3)

print("\nCompound interest for $2121 at 7% for 3 years:")
compound_interest(2121, 0.07, 3)

#Question 4

def draw_hollow_square(size, thickness):
    for row in range(size):
        for col in range(size):
            if row < thickness or row >= size - thickness:
                print('#', end='')
            elif col < thickness or col >= size - thickness:
                print('#', end='')
            else:
                print(' ', end='')
        print()    
print("Hollow square size 11, thickness 3:")
draw_hollow_square(11,3)

print("\nHollow square size 12, thickness 3:")
draw_hollow_square(12,3)

print("\nHollow square size 12, thickness 5:")
draw_hollow_square(12,5)



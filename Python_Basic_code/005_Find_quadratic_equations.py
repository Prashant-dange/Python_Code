import cmath  # For complex numbers

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    D = b**2 - 4*a*c
    
    # Calculate the roots based on the discriminant
    if D > 0:
        x1 = (-b + D**0.5) / (2 * a)
        x2 = (-b - D**0.5) / (2 * a)
        return (x1, x2)
    elif D == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        real_part = -b / (2 * a)
        imaginary_part = cmath.sqrt(abs(D)) / (2 * a)
        x1 = complex(real_part, imaginary_part)
        x2 = complex(real_part, -imaginary_part)
        return (x1, x2)

# Get user input
def main():
    print("Solve the quadratic equation ax^2 + bx + c = 0")
    a = float(input("Enter coefficient a (not zero): "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    if a == 0:
        print("Coefficient 'a' cannot be zero.")
        return
    
    roots = solve_quadratic(a, b, c)
    
    if len(roots) == 2:
        print(f"The roots are: {roots[0]} and {roots[1]}")
    elif len(roots) == 1:
        print(f"The root is: {roots[0]}")
    else:
        print("No real roots.")

if __name__ == "__main__":
    main()

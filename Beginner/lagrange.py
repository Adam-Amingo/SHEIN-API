def lagrange_interpolation(x, y, xp):
    n = len(x)
    yp = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p *= (xp - x[j]) / (x[i] - x[j])
        yp += p * y[i]
    return yp

def newtons_divided_difference(x, y, xp):
    n = len(x)
    dd_table = [y.copy()]

    for level in range(1, n):
        row = []

        # no division by 0 
        for i in range(n - level):
            denominator = x[i + level] - x[i]

            # denominator check == 0 ; x is duplicate
            if denominator == 0:
                raise ValueError("Duplicate x-values found, which causes division by zero.")
            diff = (dd_table[level - 1][i+1] - dd_table[level - 1][i]) / denominator
            row.append(diff)
        dd_table.append(row)
    
    result = dd_table[0][0]
    product_term = 1
    for i in range(1, n):
        product_term *= (xp - x[i - 1])
        result += dd_table[i][0] * product_term
    return result

# error handling and valida..
def get_validated_input(prompt, allow_negative=False):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Input cannot be empty. Try again.")
            continue

        parts = user_input.split(',')
        try:
            values = [float(p.strip()) for p in parts]
        except ValueError:
            print("All entries must be numeric. Try again.")
            continue

        if not allow_negative and any(v < 0 for v in values):
            print("Negative values are not allowed. Try again.")
            continue

        return values

def main():
    # getting user input with valid..
    print("Enter values separated by commas (e.g., 1, 2, 3)")
    x = get_validated_input("Enter time values (x): ", allow_negative=False)
    y = get_validated_input("Enter temperature values (y): ")

    if len(x) != len(y):
        print("Time and temperature lists must be the same length.")
        return

    # checking dupicate x-values
    if len(set(x)) != len(x):
        print("Time values must be unique (no duplicates).")
        return

    while True:
        #user input for xp vaildation
        try:
            xp = float(input("Enter the time to estimate temperature for: "))
            if xp < 0:
                print("Time cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for time.")

    # Perform interpolation
    yp_lagrange = lagrange_interpolation(x, y, xp)
    yp_newton = newtons_divided_difference(x, y, xp)

    print(f"\n Interpolated Temperature at time {xp} using Lagrange: {yp_lagrange:.2f} °C")
    print(f"Interpolated Temperature at time {xp} using Newton  : {yp_newton:.2f} °C")

# run the program
main()

# 2022/07/12

import sys
from math import sqrt, isclose

BAR = "#" * 50

def input_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def display_polynomial(a, b, c):
    terms = []

    if not isclose(a, 0.0):
        if a == 1:
            terms.append("x²")
        elif a == -1:
            terms.append("-x²")
        else:
            terms.append(f"{a:.2f}x²")

    if not isclose(b, 0.0):
        sign = "+" if b > 0 else "-"
        abs_b = abs(b)
        if abs_b == 1:
            terms.append(f" {sign} x")
        else:
            terms.append(f" {sign} {abs_b:.2f}x")

    if not isclose(c, 0.0):
        sign = "+" if c > 0 else "-"
        abs_c = abs(c)
        terms.append(f" {sign} {abs_c:.2f}")

    poly_str = "".join(terms).strip()
    print(f"Polynomial: {poly_str} = 0")

def solve_quadratic(a, b, c):
    if isclose(a, 0.0):
        if isclose(b, 0.0):
            print("No valid polynomial (a and b are zero).")
        else:
            x = -c / b
            print(f"Linear solution: x = {x:.4f}")
        return

    delta = b**2 - 4*a*c
    print(f"Delta = {delta:.4f}")

    if isclose(delta, 0.0):
        x = -b / (2*a)
        print(f"Solution: x = {x:.4f}")
    elif delta > 0:
        sqrt_delta = sqrt(delta)
        x1 = (-b + sqrt_delta) / (2*a)
        x2 = (-b - sqrt_delta) / (2*a)
        print(f"Solutions: x₁ = {x1:.4f}, x₂ = {x2:.4f}")
    else:
        print("No real solutions.")

def main():
    while True:
        a = input_number("a: ")
        b = input_number("b: ")
        c = input_number("c: ")

        display_polynomial(a, b, c)
        solve_quadratic(a, b, c)

        print(BAR)
        ex = input("Exit (y/n): ").strip().lower()
        print(BAR)
        if ex == 'y':
            print("Goodbye.")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt :
        print("\nExiting ...")
    except Exception as e:
        print(f"ERROR: {e}")

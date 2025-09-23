def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    print("Temperature Converter")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")

    choice = input("Enter your choice (1 or 2): ").strip()
    if choice == "1":
        try:
            c = float(input("Enter temperature in Celsius: ").strip())
            f = celsius_to_fahrenheit(c)
            print(f"{c:.2f} °C is {f:.2f} °F")
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "2":
        try:
            f = float(input("Enter temperature in Fahrenheit: ").strip())
            c = fahrenheit_to_celsius(f)
            print(f"{f:.2f} °F is {c:.2f} °C")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

main()

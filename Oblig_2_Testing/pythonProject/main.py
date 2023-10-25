from leap_year import is_leap_year

def main():
    while True:
        try:
            year = int(input("Enter a year to check if it's a leap year (or type 'exit' to quit): "))
            if is_leap_year(year):
                print(f"{year} is a leap year!")
            else:
                print(f"{year} is not a leap year!")
        except ValueError:
            print("Please enter a valid year or type 'exit' to quit.")

        user_input = input("Do you want to check another year? (yes/no): ").lower()
        if user_input != 'yes':
            break

if __name__ == "__main__":
    main()

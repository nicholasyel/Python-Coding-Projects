def main():
    print("This program converts US dollars to Russian rubles")
    print()

    dollars = eval(input("Enter amount in dollars: "))

    rubles = convert_to_rubles(dollars)

    print("That is", rubles, "rubles.")


convert_to_rubles = lambda dollars: dollars * 93.32

main()
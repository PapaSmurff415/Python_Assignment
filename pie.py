#Calculate the value of π from the infinite series
#π =4 – 4/3+4/5-4/7+4/9-4/11+…
#Write a program to print a table that shows the value of π approximated by one term of this
#series, by two terms, by three terms, etc. 
#How many terms of this series do you have to use before you first get
#3.14? 3.1.41? 3.1415? 3.14159?

def calculate_pi_approximation(terms):
    pi_approximation = 0
    sign = 1

    for i in range(1, 2 * terms, 2):
        pi_approximation += sign * 4 / i
        sign *= -1

    return pi_approximation

def find_required_terms(target_value):
    terms = 1
    current_approximation = calculate_pi_approximation(terms)

    while abs(current_approximation - target_value) > 0.00001:
        terms += 1
        current_approximation = calculate_pi_approximation(terms)

    return terms

def print_pi_table():
    targets = [3.14, 3.141, 3.1415, 3.14159]

    print("Terms\t\tApproximation to π")
    print("------------------------------")

    for target in targets:
        terms_required = find_required_terms(target)
        pi_approximation = calculate_pi_approximation(terms_required)
        print(f"{terms_required}\t\t{pi_approximation:.5f}")

if __name__ == "__main__":
    print_pi_table()
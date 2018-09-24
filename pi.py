# pi.py
def main():
    print("Uses number of terms in series to appx pi")
    print()
    # n variable for number of terms to sum
    n = int(input("Amount of terms? "))

    total = 0.0
    #sgn used to extract/alternate sign of terms
    sgn = 1.0   
    for denom in range(1, 2*n, 2):
        total = total + sgn * 4.0/denom
        sgn = -sgn #- used to flip the signum

    print("Approximation to pi:", total)
    print("Difference from 'math.pi' to test accuracy:", math.pi - total)
main()
git add pi.py
git commit --amend -m

# rover.py
# program to calculate how long it takes a photo from Curiosity to reach NASA when Mars is at its closest orbit to Earth, a distance of about 34 million miles
# speed of light 186000 m / s

def main():
    sol = 186000
    dist = 34000000
    
# dist divided by speed shows time taken
    time = dist / sol
    print("The time for a picture to reach Earth is", time, "seconds")

main()


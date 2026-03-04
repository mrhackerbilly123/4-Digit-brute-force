def error():
    if len(user_password) == 4 and user_password.isdigit():
        print("Valid input")
    else:
        print("Error. You must enter exactly 4 digits.")
        exit()

import time

while True:
    user_password = input("Please enter a 4 DIGIT password: ")
    error()

    print("Cracking passwords...")

    for i in range(10000):   
        guess = str(i).zfill(4)
        print("Trying:", guess)
        time.sleep(0.01)

        if guess == user_password:
            print("Password found")
            print("Password is:", guess)
            break

    break   # stops the while loop after cracking

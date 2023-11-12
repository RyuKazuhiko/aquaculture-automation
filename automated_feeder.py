print("Automated Feeder")
print("*-----------------------------------------------*")

while True:
    user_input = input("""
(A) Set Time
or
(B) Reset Time
""").upper()

    if user_input == "A":
        print("\nPlease input the feeding time in the 24-hour format:")
        while True:
            feeding_time = input().upper()
            print("\nYour fish will be fed in " + feeding_time + " hours.\n\n*******\n")
            break

        continue
    
    elif user_input == "B":
        print("\nFeeding time has been reset.\n\n*******\n")
        continue

    else:
        print("Exiting the program.")
        break

print("*-----------------------------------------------*")
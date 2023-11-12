print("Automated Oxygen Level Management")
print("*-----------------------------------------------*")

while True:
    user_input = input("""
(A) Manual Switch 
or
(B) Oxygen Sensor
or
(AB) Both
""").upper()

    if user_input == "A":
        print("\nMANUAL SWITCH is turned ON. Action: Aeration System increasing oxygen MANUALLY.\n*******\n")
        continue
           

    elif user_input == "B":
        print("\nOxygen Sensor reported LOW, Action: ACTIVATING Aeration System AUTOMATICALLY.\n*******\n")
        continue
    
    elif user_input == "AB":
        print("\nAeration System increasing Oxygen.\n\n*******\n")
        continue

    else:
        print("Exiting the program.")
        break

print("*-----------------------------------------------*")
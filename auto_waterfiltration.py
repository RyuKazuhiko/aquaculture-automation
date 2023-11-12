print("Automatic Water Filtration")
print("*-----------------------------------------------*")

while True:
    user_input = input("""
(A) Dirty Water 
or
(B) Actual Time to Clean 
or
(AB) Both
""").upper()

    if user_input == "A":
        print("\nWater Quality Sensor: Dirt DETECTED, Activating Water Filter. \n*******\n")
        continue
           

    elif user_input == "B":
        print("\nWater Filtration ACTIVATED based on time set. \n*******\n")
        continue
    
    elif user_input == "AB":
        print("\nWater Quality Sensor: Dirt DETECTED! \nAutomated Water Filtration ACTIVATING based on time set.\n\n*******\n")
        continue

    else:
        print("Exiting the program.")
        break

print("*-----------------------------------------------*")
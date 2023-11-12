print("Automatic Water Temperature Monitor")
print("*-----------------------------------------------*")

while True:
    user_input = input("""
(A) Optimum Water Temperature of 24-30 Celcius Degree 
or
(B) High Turbidity of Water
or
(AB) Both
""").upper()

    if user_input == "A":
        print("\nWater Temperature Sensor: Water Temperature is in Optimum Temperature, NO ACTION taking place. \n*******\n")
        continue
           

    elif user_input == "B":
        print("\nWater Temperature Sensor: Tubidity is SENSED, Auto setting water temperature or pumping out new water to optimize water temperature. \n*******\n")
        continue
    
    elif user_input == "AB":
        print("\nPumping out new water to optimize water temperature based on time.\n\n*******\n")
        continue

    else:
        print("Exiting the program.")
        break

print("*-----------------------------------------------*")
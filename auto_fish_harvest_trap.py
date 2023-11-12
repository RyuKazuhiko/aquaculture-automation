print("Automatic Fish Harvesting Trap")
print("*-----------------------------------------------*")

while True:
    user_input = input("""
(A) Fishes Enter, Lift Net 
or
(B) Open Fish Trap
or
(AB) Both
""").upper()

    if user_input == "A":
        print("\nFished are detected. Action: Fish Net is LIFTED UP.\n*******\n")
        continue
           

    elif user_input == "B":
        print("\nNo Fish are detected, Action: None.\n*******\n")
        continue
    
    elif user_input == "AB":
        print("\nFishes are detected. Action: Fish net is LIFTED UP, Open Fish Trap.\n\n*******\n")
        continue

    else:
        print("Exiting the program.")
        break

print("*-----------------------------------------------*")
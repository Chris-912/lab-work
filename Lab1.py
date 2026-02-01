# Ohm's Law Calculator with Power Calculation
while True:
    try:
        # Task 2: Handle invalid inputs  
        voltage = float(input("\nEnter voltage (V): "))
        resistance = float(input("Enter resistance (Ohms): "))
        if resistance != 0:
            # Calculate Current
            current = voltage / resistance
            # Task 3: Calculate Power (P = V * I)
            power = voltage * current
            print("Current (A):", current)
            print("Power (W):", power)   
        else:
            print("Error: Resistance cannot be zero.")
    except ValueError:
        print("Invalid input! Please enter numbers only.")
    # Task 1: Allow multiple calculations
    repeat = input("\nDo you want to calculate again? (yes/no): ")
    if repeat != "yes":
        print("END!")
        break

import random
import time
import matplotlib.pyplot as plt
temps = []
humidities = []
times = []
for i in range(10):
    try:
        # Generate random data
        current_temp = 25 + random.uniform(-1, 1)
        current_hum = 50 + random.uniform(-5, 5)  # Task 1: Add humidity
        # Add to lists
        temps.append(current_temp)
        humidities.append(current_hum)
        times.append(i)
        # Task 2 & 3: File operations with Error Handling
        filename = "datalog.csv"
        with open(filename, "a") as f:
            # Writing in CSV format: Time, Temp, Humidity
            f.write(f"{i},{current_temp:.2f},{current_hum:.2f}\n")
        print(f"Logged: Time={i}s, Temp={current_temp:.2f}C, Hum={current_hum:.2f}%")
        # Simulate delay
        time.sleep(0.5)
    except IOError:
        print("Error: Could not write to file! Check if it's open elsewhere.")
    except Exception as e:
        print("An unexpected error occurred:", e)
# Plotting
plt.figure()
plt.plot(times, temps, label="Temperature (C)", color="red")
plt.plot(times, humidities, label="Humidity (%)", color="blue")
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.title("Environmental Data Log")
plt.legend()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

#load logged data
df = pd.read_csv("plc_data.csv")

#convert time stamp to datetime
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df["Seconds"] = (df["Timestamp"]-df["Timestamp"].min()).dt.total_seconds()


#Plot the trend of the PLC values over time
plt.figure(figsize=(10,5))
plt.plot(df["Seconds"],df["Value_0"],label="PLC Setpoint", marker="o")
plt.xlabel("Time (Seconds)")
plt.ylabel("Setpoint Value")
plt.title("PLC Setpoint Trends Over Time")
plt.legend()
plt.grid()
plt.show()
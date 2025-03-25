import snap7
import time
import pandas as pd
from snap7.util import get_uint

# PLC Connection Details
PLC_IP = "192.168.115.180"  # Change to your PLC IP
RACK = 0
SLOT = 1
DB_NUMBER = 1  # Change this based on your setup
TOTAL_BYTES = 6  # Adjust based on the total DB size

# Connect to PLC
plc = snap7.client.Client()
plc.connect(PLC_IP, RACK, SLOT)

# Data Storage
data_log = []

try:
    print("📡 Starting real-time PLC data collection...")

    while True:
        if plc.get_connected():
            # Read the entire Data Block
            full_data = plc.db_read(DB_NUMBER, 0, TOTAL_BYTES)

            values = []
            for i in range(0, TOTAL_BYTES, 2):  # Read every 2 bytes as UInt
                value = get_uint(full_data, i)
                values.append(value)

            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            data_log.append([timestamp] + values)

            # Print collected data
            print(f"[{timestamp}] Read Values: {values}")

            # Save Data Every 10 Readings
            if len(data_log) % 10 == 0:
                column_names = ["Timestamp"] + [f"Value_{i}" for i in range(len(values))]
                df = pd.DataFrame(data_log, columns=column_names)
                df.to_csv("plc_data.csv", index=False)

            time.sleep(1)  # Adjust polling interval as needed

except KeyboardInterrupt:
    print("🛑 Stopping data collection...")

finally:
    plc.disconnect()

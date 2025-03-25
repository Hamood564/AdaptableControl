from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd



#load logged data
df = pd.read_csv("plc_data.csv")

#convert time stamp to datetime
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df["Seconds"] = (df["Timestamp"]-df["Timestamp"].min()).dt.total_seconds()

# Prepare Data for Training
X = df[["Seconds"]]  # Time as input feature
y = df["Value_0"]  # PLC setpoint as the target

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train ML Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict Next Setpoint
next_time = np.array([[df["Seconds"].max() + 1]])  # Predict next step
predicted_setpoint = model.predict(next_time)

print(f"🔹 Predicted Next Setpoint: {predicted_setpoint[0]}")


from scipy.io import loadmat

# Load the MATLAB battery dataset
data = loadmat("B0053.mat")

# Display the variables stored in the file
print("Variables in MATLAB file:")
print(data.keys())

# Inspect the battery data
battery = data["B0053"]

print("\nBattery structure:")
print(battery.shape)
print(battery.dtype)


cycles = battery["cycle"][0, 0]

print("Number of recorded operations:", cycles.size)
print("Cycle fields:", cycles.dtype.names)


from collections import Counter

operation_types = []

for cycle in cycles[0]:
    operation = cycle["type"][0]
    operation_types.append(operation)

print("Operation counts:")
print(Counter(operation_types))



# Extract capacity from each discharge operation

cycle_numbers = []
capacities = []

for cycle in cycles[0]:
    operation_type = cycle["type"][0]

    if operation_type == "discharge":
        discharge_data = cycle["data"][0, 0]
        capacity = float(discharge_data["Capacity"][0, 0])

        cycle_numbers.append(len(cycle_numbers) + 1)
        capacities.append(capacity)

print("\nDischarge cycle | Capacity (Ah)")
print("--------------------------------")

for number, capacity in zip(cycle_numbers, capacities):
    print(f"{number:15d} | {capacity:.4f}")



import pandas as pd

df = pd.DataFrame({
    "Cycle": cycle_numbers,
    "Capacity": capacities
})

print(df.head())
print(df.shape)


print(df.tail(10))
print(df.describe())


print("\nRecords with zero capacity:")
print(df[df["Capacity"] == 0])

df_clean = df[df["Capacity"] > 0].copy()

print(df_clean.shape)


# Features and target
X = df_clean[["Cycle"]]
y = df_clean["Capacity"]

# Chronological 80/20 split
split_index = int(len(df_clean) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))



from sklearn.linear_model import LinearRegression

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict capacity for the test cycles
y_pred = model.predict(X_test)

print("Predicted capacities:")
print(y_pred)


print("Slope (m):", model.coef_[0])
print("Intercept (b):", model.intercept_)


from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("MAE:", mae)
print("RMSE:", rmse)

results = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

print(results)


import matplotlib.pyplot as plt

plt.scatter(X_train["Cycle"], y_train, label="Training data")
plt.scatter(X_test["Cycle"], y_test, label="Actual test data")
plt.plot(
    df_clean["Cycle"],
    model.predict(df_clean[["Cycle"]]),
    label="Linear Regression"
)

plt.xlabel("Discharge Cycle")
plt.ylabel("Capacity (Ah)")
plt.title("NASA Battery Capacity Prediction")
plt.legend()
plt.grid(True)
plt.show()


from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)

print("R-squared (R²):", r2)



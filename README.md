
NASA Battery Capacity Prediction
Exploratory machine-learning study  |  NASA B0053  |  Python and linear regression
Project overview
This project explores lithium-ion battery capacity degradation using NASA B0053 discharge measurements. A simple linear regression model estimates battery capacity (Ah) from discharge-cycle number. The goal is to evaluate how well an interpretable model trained on earlier cycles predicts later observations.
Scope: An educational baseline model, not a validated battery health, safety, or remaining-useful-life estimator.
Dataset and method
•	NASA B0053 MATLAB (.mat) battery dataset; 56 discharge observations initially reviewed.
•	An anomalous zero-capacity observation at cycle 56 was excluded for this experiment, leaving 55 usable cycles.
•	Input: discharge-cycle number. Target: measured capacity in ampere-hours (Ah).
•	Chronological train/test split: first 44 cycles for training; following 11 cycles for evaluation.
•	Linear regression fitted to the training portion; MAE and RMSE calculated on the held-out test data.
Evaluation results
Metric	Result
Training observations	44
Test observations	11
Test MAE	0.0469 Ah
Test RMSE	0.0517 Ah
MAE is the average absolute prediction error. RMSE gives larger errors greater weight.
Battery capacity prediction graph
 ![Battery capacity prediction](NASA_battery_capacity_prediction.png)
Figure 1. Measured training and test capacities with the fitted linear regression trend.
The regression line captures an overall decline in battery capacity as discharge cycles increase. However, later test observations fluctuate and are generally above the fitted predictions. That gap is an important result: an overall trend can be informative while still showing bias on unseen measurements.
Key findings
•	Capacity generally declines over the observed cycles, although individual discharge measurements fluctuate.
•	A chronological split better represents forecasting later cycles than randomly mixing early and late observations.
•	The linear model gives an interpretable baseline, but its later-cycle underprediction highlights model limitations.
•	The excluded zero-capacity point deserves investigation rather than being assumed to be faulty.
Limitations and next steps
This analysis contains only one battery and 55 usable observations, with cycle number as the sole model input. Future experiments could examine additional battery cells, test non-linear models, and incorporate properly aligned voltage, temperature, and current measurements while avoiding time-series leakage.

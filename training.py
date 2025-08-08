import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
data = pd.read_csv('One_Plus_Phones_With_Missing.csv')

# Drop rows where either X or y is missing
data = data.dropna(subset=['Discounted_Price', 'Rating'])

# Define features and target
X = data[['Discounted_Price']]   # Must be 2D
y = data['Rating']               # Target variable

# Train model
model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, 'model.pkl')


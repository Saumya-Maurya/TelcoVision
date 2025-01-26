from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd

def train_model(df):
    """Train a Random Forest model."""
    X = df[['tenure', 'MonthlyCharges', 'TotalCharges']]  # Add more features after encoding
    y = df['Churn']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    return model

# Example Usage
if __name__ == "__main__":
    df = pd.read_csv("data/telco_cleaned.csv")
    model = train_model(df)

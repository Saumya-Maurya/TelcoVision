import pandas as pd

def load_data(filepath):
    """Load the dataset."""
    return pd.read_csv(filepath)

def preprocess_data(df):
    """Preprocess the dataset."""
    # Convert TotalCharges to numeric
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df = df.dropna(subset=['TotalCharges'])  # Drop rows with missing TotalCharges

    # Create tenure category
    df['tenure_category'] = pd.cut(df['tenure'], bins=[0, 12, 24, 36, 48, 60], labels=['0-12', '13-24', '25-36', '37-48', '49-60'])

    # Encode target variable
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
    return df

# Example Usage
if __name__ == "__main__":
    filepath = "data/raw_data.csv"
    df = load_data(filepath)
    cleaned_df = preprocess_data(df)
    cleaned_df.to_csv("data/telco_cleaned.csv", index=False)

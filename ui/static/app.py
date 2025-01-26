import os
from flask import Flask, render_template, url_for
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

# Load dataset
data_path = "data/telco_cleaned.csv"
df = pd.read_csv(data_path)

@app.route('/')
def home():
    # Calculate key metrics
    churn_rate = round(df['Churn'].mean() * 100, 2)
    total_customers = len(df)
    avg_monthly_charges = round(df['MonthlyCharges'].mean(), 2)
    avg_tenure = round(df['tenure'].mean(), 2)

     # Ensure the images directory exists
    images_dir = "/ui/static/images/"
    os.makedirs(images_dir, exist_ok=True)


    # Create a churn distribution graph
    plt.figure(figsize=(6, 4))
    df['Churn'].value_counts().plot(kind='bar', color=['skyblue', 'orange'])
    plt.title('Churn Distribution')
    plt.xlabel('Churn (0 = No, 1 = Yes)')
    plt.ylabel('Customer Count')
    graph_path = "../ui/static/images/churn_distribution.png"
    plt.savefig(graph_path)  # Save the graph
    plt.close()

    # Pass metrics and graph to the template
    metrics = {
        "churn_rate": churn_rate,
        "total_customers": total_customers,
        "avg_monthly_charges": avg_monthly_charges,
        "avg_tenure": avg_tenure,
    }
    return render_template('dashboard.html', metrics=metrics, graph_path=graph_path)

if __name__ == '__main__':
    app.run(debug=True)

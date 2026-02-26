# app.py
from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    # Read CSV (Simulating Database connection)
    df = pd.read_csv('club_data.csv')
    
    # Convert entire dataset to JSON for the frontend to process
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
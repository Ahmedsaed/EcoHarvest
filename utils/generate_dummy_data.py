import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Function to generate dummy data
def generate_dummy_data(num_records=100):
    start_date = datetime(2023, 1, 1)
    end_date = start_date + timedelta(days=num_records - 1)

    date_range = pd.date_range(start=start_date, end=end_date, freq='D')

    data = {
        'timestamp': date_range,
        'temperature': np.random.uniform(20, 30, size=num_records),
        'light_intensity': np.random.uniform(100, 1000, size=num_records),
        'co2_level': np.random.uniform(300, 800, size=num_records),
        'water_ph_value': np.random.uniform(6, 8, size=num_records),
    }

    df = pd.DataFrame(data)
    return df

# Generate dummy data and save it to a CSV file
dummy_data = generate_dummy_data()
dummy_data.to_csv('dummy_data.csv', index=False)

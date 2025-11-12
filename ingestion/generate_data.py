from faker import Faker
from datetime import datetime, timedelta
import random
import csv
import os

fake = Faker()

def generate_csv(path="sample_data/transactions.csv", n=100000):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    start = datetime(2020,1,1)
    with open(path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["transaction_id","user_id","item_id","amount","timestamp","country"])
        for i in range(1, n+1):
            timestamp = start + timedelta(seconds=random.randint(0, 60*60*24*365*3))
            writer.writerow([
                i,
                fake.uuid4(),
                fake.random_int(min=1, max=100000),
                round(random.uniform(1.0,500.0),2),
                timestamp.isoformat(),
                fake.country()
            ])
    print("Wrote", path)

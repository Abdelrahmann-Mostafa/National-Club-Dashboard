# generate_data.py
import pandas as pd
import random
from faker import Faker
import datetime

fake = Faker()
NUM_RECORDS = 800  # More data for better charts

# Domain Lists
BRANCHES = ['Cairo', 'Alexandria', 'Giza', 'Luxor', 'Aswan', 'Hurghada']
GAMES = ['Football', 'Tennis', 'Squash', 'Swimming', 'Basketball', 'Volleyball']
RANKS = ['Junior', 'Amateur', 'Semi-Pro', 'Professional', 'Captain']
MEMBERSHIP = ['Standard', 'Gold', 'VIP', 'Platinum']

data = []

for _ in range(NUM_RECORDS):
    rank = random.choice(RANKS)
    
    # 1. Realistic Income Logic
    base_income = {'Junior': 1000, 'Amateur': 3000, 'Semi-Pro': 7000, 'Professional': 15000, 'Captain': 28000}
    income = base_income[rank] + random.randint(-1000, 3000)
    
    # 2. Age correlates with Rank (roughly)
    if rank == 'Junior': age = random.randint(14, 19)
    elif rank == 'Amateur': age = random.randint(18, 25)
    else: age = random.randint(22, 38)

    # 3. Performance & Attendance
    perf_score = random.randint(50, 100) # 0-100 scale
    attendance = random.randint(60, 100) # Percentage

    # 4. Join Date (Last 5 years)
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2025, 12, 1)
    time_between = end_date - start_date
    days_between = time_between.days
    random_days = random.randrange(days_between)
    join_date = start_date + datetime.timedelta(days=random_days)

    data.append({
        'PlayerName': fake.name(),
        'Branch': random.choice(BRANCHES),
        'Game': random.choice(GAMES),
        'Rank': rank,
        'Income': income,
        'Gender': random.choice(['Male', 'Female']),
        'Certificates': random.randint(0, 15),
        'Age': age,
        'JoinDate': join_date.strftime("%Y-%m-%d"),
        'MembershipType': random.choice(MEMBERSHIP),
        'PerformanceScore': perf_score,
        'Attendance': attendance
    })

df = pd.DataFrame(data)
df.to_csv('club_data.csv', index=False)
print("✅ Mega dataset generated with 12 columns!")
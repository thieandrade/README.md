import csv, random
from datetime import date, timedelta

random.seed(42)
n = 300
models = ['ford f-150', 'toyota camry', 'honda civic', 'chevrolet silverado 1500',
          'ford focus', 'nissan altima', 'jeep grand cherokee', 'honda cr-v',
          'ford escape', 'toyota corolla', 'chevrolet equinox', 'ram 1500']
conditions = ['excellent', 'good', 'like new', 'fair', 'salvage']
fuels = ['gas', 'diesel', 'hybrid', 'electric']
transmissions = ['automatic', 'manual', 'other']
types_ = ['sedan', 'SUV', 'truck', 'coupe', 'wagon', 'van']
colors = ['white', 'black', 'silver', 'blue', 'red', 'grey', '']

rows = []
start = date(2019, 1, 1)
for _ in range(n):
    model_year = random.randint(1995, 2019)
    odometer = random.randint(0, 300000)
    price = max(500, round(25000 - (2020 - model_year) * 700 - odometer * 0.03 + random.gauss(0, 1500)))
    cylinders = random.choice([3, 4, 4, 5, 6, 6, 8])
    is_4wd = 1 if random.random() < 0.4 else ''
    days_listed = random.randint(1, 120)
    date_posted = start + timedelta(days=random.randint(0, 365))
    if random.random() < 0.03:
        model_year = ''
    if random.random() < 0.03:
        odometer = ''
    rows.append({'price': price, 'model_year': model_year, 'model': random.choice(models),
                 'condition': random.choice(conditions), 'cylinders': cylinders,
                 'fuel': random.choice(fuels), 'odometer': odometer,
                 'transmission': random.choice(transmissions), 'type': random.choice(types_),
                 'paint_color': random.choice(colors), 'is_4wd': is_4wd,
                 'date_posted': date_posted.isoformat(), 'days_listed': days_listed})

with open('vehicles_us.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
print('vehicles_us.csv criado com', len(rows), 'linhas')

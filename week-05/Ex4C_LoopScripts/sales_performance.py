sales_data = [
    ('Marcus Webb', 'East', 4250.00),
    ('Priya Sharma', 'West', 5875.50),
    ('DeShawn Carter', 'East', 3100.75),
    ('LaTonya Ricers', 'South', 6420.00),
    ('Bob Ngyren', 'West', 4980.25),
]

for name, region, sales in sales_data:
    print(f"{name} ({region}): ${sales:,.2f}")
    if sales > 5000:
        print("^ Top performer!")
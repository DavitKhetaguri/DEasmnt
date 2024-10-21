import random
from datetime import datetime, timedelta



str = """insert into deasmnt.sales_transactions(transaction_id,
purchase_date,
total_amount)
values({id},'{date}',{amount});
"""
def random_date(start, end):
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")
    random_days = random.randint(0, int((end_date - start_date).days))
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")


for i in range(200):
    
    formatted_str = str.format(
        id=i,
        date=random_date(start="2024-04-01", end="2024-11-01"),
        amount=round(random.uniform(0.1, 100), 2)
    )
    print(formatted_str)
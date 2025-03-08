stocks=[215,265,250,200,240,260,230]

min_price=float('inf')
max_Profit=0

for i in stocks:
    min_price=min(min_price,i)
    max_Profit=max(max_Profit,i-min_price)
print(max_Profit)

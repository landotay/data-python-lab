import matplotlib.pyplot as plt
import numpy as np

open_file = open('CupcakeInvoices.csv')
# Part 2 - 3
# for row in open_file:
#     print(row)

#Part 2 - 4
# for row in open_file:
#     values = row.split(',')
#     print(values[2])

# for row in open_file:
#     values = row.split(',')
#     quantity = float(values[3])
#     price = float(values[4])
#     total = quantity * price 
#     print(total)

# invoice_total = 0 
# for row in open_file:
#     values = row.split(',')
#     quantity = float(values[3])
#     price = float(values[4])
#     total = quantity * price 

#     invoice_total += total
    
# print(invoice_total)

chocolate_total = 0
vanilla_total = 0
strawberry_total = 0

for row in open_file:
    values = row.split(',')
    quantity = float(values[3])
    price = float(values[4])
    total = quantity * price

    if values[2] == 'Chocolate':
        chocolate_total += total
    elif values[2] == 'Vanilla':
        vanilla_total += total
    else:
        strawberry_total += total

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
flavors = ['Chocolate', 'Vanilla', 'Strawberry']
totals = [chocolate_total, vanilla_total, strawberry_total]
ax.bar(flavors, totals)
plt.show()

open_file.close()




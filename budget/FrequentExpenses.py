"""from Expense import Expenses

import collections

expenses = Expenses()

expenses.read_expenses('../data/spending_data.csv')

spendingCategories = []

for expense in expenses.list:
    spendingCategories.append(expense.category)

spendingCounter = collections.Counter(spendingCategories)
print(spendingCategories)"""

from Expense import *
import collections
import matplotlib.pyplot as plt

expenses = Expenses()
expenses.read_expenses('../data/spending_data.csv')
spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)
print(spending_counter)

top5 = spending_counter.most_common(5)
print(top5)

categories,count = zip(*top5)
fig, ax = plt.subplots()
ax.bar(categories,count)
ax.set_title('# of Purchases by Category')
plt.show()






import pandas as pd
import matplotlib.pyplot as plt
# Bekwai Municipal Assembly -Internal Audit Analysis
# Accounting with Computing -level 200 -George Opoku Mensah
# Load data ( we will create Excel in next step)
# df =
pd.read-excel('Bekwai-Municipal-Expenses.xlsx')
# For demo, sample data
data = {
  'Department':['Sanitation','Education', 'Health', 'Roads', 'Admin'],
  'Amount-GHS':[60616, 55876, 54873, 51941,51175]
}
import pandas as pd 
df =pd.DataFrame(data)
print("Total Expenditure:",
df['Amount-GHS'].sum(),"GHS")      
print(df)
# Chart for audit report
df.plot(kind='barh',x='Department',
y='Amount-GHS',color='green',
legend=False)
plt.title('Bekwai Municipal-Expenditure by Department (GHS)')
plt.xlabel('Total Amount GHS')
plt.tight-layout()
plt.savefig('chart.png')
plt.show()

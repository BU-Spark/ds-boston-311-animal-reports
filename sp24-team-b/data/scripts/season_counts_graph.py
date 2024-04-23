import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('season_counts.csv') # csv compiled from running getseason.py

line_data = data[data['Year'] != 'amount']
years = line_data['Year']
spring = line_data['Spring']
summer = line_data['Summer']
fall = line_data['Fall']
winter = line_data['winter']

colors = {
    'Spring': '#64db3b',
    'Summer': '#f7e200',
    'Fall': '#eb2f3d',
    'Winter': '#5edff4'  
}

plt.figure(figsize=(12, 6))

plt.plot(years, spring, marker='o', label='Spring', linewidth=2, color=colors['Spring'])
plt.plot(years, summer, marker='o', label='Summer', linewidth=2, color=colors['Summer'])
plt.plot(years, fall, marker='o', label='Fall', linewidth=2, color=colors['Fall'])
plt.plot(years, winter, marker='o', label='Winter', linewidth=2, color=colors['Winter'])

plt.title('Seasonal Counts 2013-2023', fontsize=18, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Count', fontsize=14)

plt.legend(fontsize=12)

plt.xticks(rotation=45, fontsize=10, color='grey')
plt.yticks(fontsize=12, color='grey')
plt.grid(True, color='lightgray', linewidth=0.5, alpha=0.5)
ax = plt.gca() 
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False) 
ax.spines['right'].set_visible(False) 
amount_data = data[data['Year'] == 'amount'].iloc[0, 1:].values
seasons = ['Spring', 'Summer', 'Fall', 'Winter'] 
plt.tight_layout()
plt.savefig('season_counts_line_chart.png', dpi=300)
plt.show()
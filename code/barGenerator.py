import matplotlib.pyplot as plt
import numpy as np

# Data for Cloud and Local
metrics_key = ['User time (seconds)', 'System time (seconds)', 'Percent of CPU', 
           'Elapsed time (seconds)', 'Max resident set size (kbytes)', 
           'Major page faults', 'Minor page faults', 
           'Voluntary context switches', 'Involuntary context switches']

metrics = ['10MB','50MB', '100MB']
i=8

#10MB
cloud_values_10 = [0.84, 0.15, 94, 1.06, 131044, 0, 35601, 85, 49]
local_values_10 = [1.31, 0.33, 60, 2.71, 210092, 2, 56966, 312, 271]

#50MB
cloud_values_50 = [3.12, 0.65, 89, 4.19, 450432, 0, 159974, 283, 184]
local_values_50 = [3.29, 0.88, 75, 5.54, 684684, 0, 240132, 556, 227]

#100MB
cloud_values_100 = [6.05, 0.99, 99, 7.04, 876116, 4, 290931, 43, 219]
local_values_100 = [6.29, 1.61, 81, 9.65, 1269760, 0, 438017, 785, 1320]

cloud_values = [cloud_values_10[i], cloud_values_50[i], cloud_values_100[i]]
local_values = [local_values_10[i], local_values_50[i], local_values_100[i]]

# Bar width and index for each group
bar_width = 0.35
index = np.arange(len(metrics))

# Plotting the bar graph
fig, ax = plt.subplots(figsize=(10, 6))

bar1 = ax.bar(index, cloud_values, bar_width, label='Cloud', color='blue')
bar2 = ax.bar(index + bar_width, local_values, bar_width, label='Local', color='green')

# Adding labels and title
ax.set_xlabel('Metrics', fontsize=12)
ax.set_ylabel('Values', fontsize=12)
ax.set_title('Cloud vs Local ' + metrics_key[i] + ' Comparison', fontsize=14)
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(metrics, rotation=45, ha="right", fontsize=10)

ax.legend()

# Show the graph
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Sample data: Measurement ranges for each size
sizes = ['S', 'M', 'L', 'XL']
chest = [(85, 90), (91, 96), (97, 102), (103, 108)]
waist = [(70, 75), (76, 81), (82, 87), (88, 93)]
hip = [(90, 95), (96, 101), (102, 107), (108, 113)]

# Convert tuples to numpy arrays for plotting
chest_min, chest_max = zip(*chest)
waist_min, waist_max = zip(*waist)
hip_min, hip_max = zip(*hip)

x = np.arange(len(sizes))

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(x - 0.2, chest_min, width=0.2, label='Chest Min', color='skyblue')
plt.bar(x, chest_max, width=0.2, label='Chest Max', color='blue')
plt.bar(x + 0.2, waist_min, width=0.2, label='Waist Min', color='lightgreen')
plt.bar(x + 0.4, waist_max, width=0.2, label='Waist Max', color='green')
plt.bar(x + 0.6, hip_min, width=0.2, label='Hip Min', color='lightcoral')
plt.bar(x + 0.8, hip_max, width=0.2, label='Hip Max', color='red')

plt.xticks(x + 0.4, sizes)
plt.xlabel('Size')
plt.ylabel('Measurement (cm)')
plt.title('Size Chart Distribution: Chest, Waist, and Hip Measurements')
plt.legend()
plt.show()
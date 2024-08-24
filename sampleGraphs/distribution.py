import matplotlib.pyplot as plt
import numpy as np
# Sample data: Predicted size distribution
sizes = ['S', 'M', 'L', 'XL']
size_distribution = [20, 35, 30, 15]  # Hypothetical distribution

# Plotting
plt.figure(figsize=(8, 8))
plt.pie(size_distribution, labels=sizes, autopct='%1.1f%%', colors=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'])
plt.title('Distribution of Predicted Sizes Among Users')
plt.show()
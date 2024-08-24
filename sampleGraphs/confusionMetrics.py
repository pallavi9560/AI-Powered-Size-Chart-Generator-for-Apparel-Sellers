import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Sample data: Actual and predicted sizes
actual_sizes = ['M', 'L', 'L', 'S', 'M', 'M', 'XL', 'S', 'L', 'XL', 'M', 'S', 'L', 'XL', 'M']
predicted_sizes = ['M', 'M', 'L', 'S', 'M', 'L', 'XL', 'S', 'M', 'XL', 'M', 'S', 'L', 'L', 'M']

# Define the size labels to ensure consistency in ordering
size_labels = ['S', 'M', 'L', 'XL']

# Generate the confusion matrix
cm = confusion_matrix(actual_sizes, predicted_sizes, labels=size_labels)

# Display the confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=size_labels)
disp.plot(cmap=plt.cm.Blues)

plt.title('Confusion Matrix for Size Prediction')
plt.show()

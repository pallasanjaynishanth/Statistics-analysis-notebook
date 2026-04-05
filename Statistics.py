import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Style
plt.style.use('seaborn-v0_8')

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Plot
ax.plot(x, y, color='blue', linewidth=2.5, label='Sine Wave')

# Fill area under curve
ax.fill_between(x, y, color='blue', alpha=0.1)

# Titles and labels
ax.set_title("Beautiful Sine Wave Visualization", fontsize=16, fontweight='bold')
ax.set_xlabel("X Values", fontsize=12)
ax.set_ylabel("sin(x)", fontsize=12)

# Grid and legend
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()

# Remove top and right borders (for cleaner look)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Show plot
plt.show()
import matplotlib.pyplot as plt

# Data
batch_sizes = [2, 4, 8, 16, 32]

prefill_2xA6000 = [41.54, 76.88, 147.34, 287.09, 563.69]
prefill_1xA6000 = [56.14, 110.46, 211.36, 430.87, 886.88]
prefill_A5000 = [103.02, 194.65, 361.25, 756.05, 1396.86]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(batch_sizes, prefill_2xA6000, marker='o', label='2x ADA A6000')
plt.plot(batch_sizes, prefill_1xA6000, marker='s', label='1x ADA A6000')
plt.plot(batch_sizes, prefill_A5000, marker='^', label='A5000')

# Add titles and labels
plt.title('Average Prefill Time vs. Batch Size')
plt.xlabel('Batch Size')
plt.ylabel('Average Prefill Time (ms)')
plt.xticks(batch_sizes)
plt.legend()
plt.grid(True)

# Save the plot as a PNG file
plt.savefig('average_prefill_time_vs_batch_size.png', dpi=300)

# Display the plot (optional)
# plt.show()

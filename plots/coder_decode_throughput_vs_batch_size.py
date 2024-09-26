import matplotlib.pyplot as plt

# Data
batch_sizes = [2, 4, 8, 16, 32]

decode_throughput_2xA6000 = [169.65, 333.31, 622.18, 1165.25, 1989.16]
decode_throughput_1xA6000 = [102.59, 203.26, 407.73, 788.17, 1454.29]
decode_throughput_A5000 = [83.77, 165.47, 323.29, 612.65, 1155.57]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(batch_sizes, decode_throughput_2xA6000, marker='o', label='2x ADA A6000')
plt.plot(batch_sizes, decode_throughput_1xA6000, marker='s', label='1x ADA A6000')
plt.plot(batch_sizes, decode_throughput_A5000, marker='^', label='A5000')

# Add titles and labels
plt.title('Decode Throughput vs. Batch Size')
plt.xlabel('Batch Size')
plt.ylabel('Throughput (tokens/sec)')
plt.xticks(batch_sizes)
plt.legend()
plt.grid(True)

# Save the plot as a PNG file
plt.savefig('decode_throughput_vs_batch_size.png', dpi=300)

# Display the plot (optional)
# plt.show()

import matplotlib.pyplot as plt

# Data
batch_sizes = [2, 4, 8, 16, 32]

decode_token_time_2xA6000 = [11.79, 12.00, 12.86, 13.73, 16.09]
decode_token_time_1xA6000 = [19.49, 19.68, 19.62, 20.30, 22.00]
decode_token_time_A5000 = [23.87, 24.17, 24.75, 26.12, 27.69]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(batch_sizes, decode_token_time_2xA6000, marker='o', label='2x ADA A6000')
plt.plot(batch_sizes, decode_token_time_1xA6000, marker='s', label='1x ADA A6000')
plt.plot(batch_sizes, decode_token_time_A5000, marker='^', label='A5000')

# Add titles and labels
plt.title('Average Decode Time per Token vs. Batch Size')
plt.xlabel('Batch Size')
plt.ylabel('Average Decode Time per Token (ms)')
plt.xticks(batch_sizes)
plt.legend()
plt.grid(True)

# Save the plot as a PNG file
plt.savefig('average_decode_time_per_token_vs_batch_size.png', dpi=300)

# Display the plot (optional)
# plt.show()

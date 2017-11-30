from crypto.cyphers.RC4 import RC4
from crypto.key.generate import generate_key
from collections import Counter
import matplotlib.pyplot as plt
'''
Requires matplotlib, install with
python -mpip install -U pip
python -mpip install -U matplotlib
'''

result = []
for _ in range(100000):
    key = generate_key(16, 8)
    rc4 = RC4(key)

    output = rc4.generate_multiple(2)
    result.append(output[1])

c = Counter(result)
print(c.most_common())

# Show the resulting histogram.
num_bins = 256
fig, ax = plt.subplots()
n, bins, patches = ax.hist(result, num_bins, normed=1)

# Set the axis labels and the title of the plot.
ax.set_xlabel('Output value of second generated value')
ax.set_ylabel('Probability density')
ax.set_title('Distribution of second output generated with RC4 with random keys')

# Show the plot.
plt.show()
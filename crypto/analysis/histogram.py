import matplotlib.pyplot as plt
'''
Requires matplotlib, install with
python -mpip install -U pip
python -mpip install -U matplotlib
'''


def plot(data, num_bins):
    # Show the resulting histogram.
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(data, num_bins, normed=1)

    # Set the axis labels and the title of the plot.
    ax.set_xlabel('Output value of second generated value')
    ax.set_ylabel('Probability density')
    ax.set_title('Distribution of second output generated with RC4 with random keys')

    # Show the plot.
    plt.show()

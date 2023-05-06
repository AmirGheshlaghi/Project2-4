def price_prediction(name):

    import matplotlib.pyplot as plt
    import numpy as np

    # File loading
    try:

        file = open(name, 'r')

    except FileNotFoundError :

        name = name + '.csv'

        file = open(name, 'r')

    # Calling the close values
    data = file.read()
    lines = data.split('\n')
    values_close = []
    for i in range(1, len(lines)-1):

        col_B = lines[i].split(',')
        values_close.append(int(col_B[5]))

    values_close.reverse()
    kernel_size = 12   # Moving average period

    kernel = np.ones((1, kernel_size))
    mov_avg = np.ones((1, len(values_close)-kernel_size+1))

    # Determine the moving average of the price
    for i in range(len(values_close)-kernel_size+1):
    	close_little = values_close[i:i+kernel_size]
    	mov_avg[0, i] = (close_little * kernel).mean()

    # Display price and moving average
    x = range(kernel_size-1, len(values_close))
    plt.plot(values_close, label='price')
    plt.plot(x, mov_avg[0], 'r', label='moving average')
    plt.xlabel('day')
    plt.ylabel('price value')
    plt.title('price & moving average')
    plt.legend()
    plt.show()

price_prediction('project_data')
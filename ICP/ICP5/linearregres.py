import csv
import numpy as np
import matplotlib.pyplot as plt

males = []
females = []
def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)  # skipping column names
        for row in csvFileReader:
            #print(', '.join(row))
            males.append(float(row[0]))
            females.append(float(row[1]))
    return

def estimate_coef(x, y):
	# number of observations/points
	n = np.size(x)

	# mean of x and y vector
	m_x, m_y = np.mean(x), np.mean(y)

	# calculating cross-deviation and deviation about x
	SS_xy = np.sum(y*x - n*m_y*m_x)
	SS_xx = np.sum(x*x - n*m_x*m_x)

	# calculating regression coefficients
	b_1 = SS_xy / SS_xx
	b_0 = m_y - b_1*m_x

	return(b_0, b_1)

def plot_regression_line(x, y, b):
	# plotting the actual points as scatter plot
	plt.scatter(x, y, color = "m",
			marker = "o", s = 30)

	# predicted response vector
	y_pred = b[0] + b[1]*x

	# plotting the regression line
	plt.plot(x, y_pred, color = "g")

	# putting labels
	plt.xlabel('x')
	plt.ylabel('y')

	# function to show plot
	plt.show()

def main():
	# observations
    get_data('unemp.csv')
    x = np.array(males)
    y = np.array(females)

    # estimating coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients:\nb_0 = {} \
		\nb_1 = {}".format(b[0], b[1]))

    # plotting regression line
    plot_regression_line(x, y, b)
    print('The equation is y = ' + str(b[0]) + ' + ' + str(b[1]) + 'x')

if __name__ == "__main__":
	main()

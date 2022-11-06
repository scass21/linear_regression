
import pandas as pd

def denorm(x, rv):
    return (x * (rv.maxPrice[0] - rv.minPrice[0]) + rv.minPrice[0])

def norm(x, rv):
    return (x - rv.minKm[0]) /(rv.maxKm[0] - rv.minKm[0])

def estimatePrice(theta0, theta1, mileage): #estimatePrice(mileage) = θ0 + (θ1 ∗ mileage)
	price = theta0 + (theta1 * mileage)
	return price

def predict(x):
	price = 0
	try:
		rv = pd.read_csv('reference_values.csv')
		mileage = norm(x, rv)
		price = denorm(estimatePrice(rv.theta0[0], rv.theta1[0], mileage), rv)
	except Exception as er:
		print("\033[1;31mError: \033[0m", er)
	return price

if __name__ == '__main__':
	mileage = input('Enter mileage value:')
	print('\033[1;32mEstimate price: \033[0m', predict(float(mileage)))
import pandas as pd

def estimatePrice(theta0, theta1, mileage):
	price = theta0 + (theta1 * mileage)
	return price

def calculateTheta(df, theta0, theta1):
    learningRate = 0.01
    m = len(df)
    tmp_theta0 = sum([(estimatePrice(theta0, theta1, i['km']) - i['price']) for i in df.to_dict('records')])
    tmp_theta1 = sum([((estimatePrice(theta0, theta1, i['km']) - i['price'] ) * i['km']) for i in df.to_dict('records')])
    theta0 -= learningRate * (tmp_theta0 / m) # Шаг градиентного спуска 
    theta1 -= learningRate * (tmp_theta1 / m)
    return theta0, theta1

def dataPreparation(df):
	# normalization of data to the value 0 - 1
	minKm = df['km'].min()
	maxKm = df['km'].max()
	minPrice = df['price'].min()
	maxPrice = df['price'].max()
	df['km'] = df['km'].apply(lambda x: (x - minKm) /(maxKm - minKm))
	df['price'] = df['price'].apply(lambda x: (x - minPrice) /( maxPrice - minPrice))
	# save reference value for predict
	data = {'minKm' :  [minKm], 'maxKm' : [maxKm], 'minPrice' :  [minPrice], 'maxPrice' :  [maxPrice]}
	referenceValue = pd.DataFrame(data)
	return df, referenceValue

def mse(df):
	# mse = pow((y - y_predict), 2)/ len(y) Mean squared error (MSE) или Mean squared deviation (MSD) - среднеквадратическая ошибка
	return ((df.price - df.pred_price)**2).mean()

def saveValues(rv, theta0, theta1, df):
	rv.assign(theta0=[theta0], theta1=theta1).to_csv('reference_values.csv', index=False)
	df.to_csv('norm_data.csv', index=False)

def train():
	theta0, theta1 = 0, 0
	current_error = 1000
	previous_error = 0
	try:
		df = pd.read_csv("data.csv")
		df, rv = dataPreparation(df)
		while abs(current_error - previous_error) > 0.00000001:
			previous_error = current_error
			theta0, theta1 = calculateTheta(df, theta0, theta1)
			df['pred_price'] = df['km'].apply(lambda x: estimatePrice(theta0, theta1, x))
			current_error = mse(df)
		saveValues(rv, theta0, theta1, df)
	except Exception as er:
		print("\033[1;31mError: \033[0m", er)


if __name__ == '__main__':
	train()

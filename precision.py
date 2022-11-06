
import pandas as pd

# Coefficient of determination - R2
def precision(df):
	#  Sum of Squares Regression (SSR) SSR = Σ(ŷi – y)2
	ssr = sum(pow(df.pred_price - df.price.mean(), 2))
	# Sum of Squares Error (SSE) SSE = Σ(ŷi – yi)2
	sse = sum(pow(df.price - df.pred_price, 2))
	#  Sum of Squares Total (SST)  SST = Σ(yi – y)2
	sst = sum(pow(df.price - df.price.mean(), 2))
	# R2 = 1 - SSE / SST or  R2 = SSR / SST
	precision = 1 - sse/sst
	# precision = ssr / sst
	return precision * 100

if __name__ == '__main__':
	norm_df = pd.read_csv('norm_data.csv')
	print(precision(norm_df))
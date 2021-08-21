import pandas as pd

test = int(input(("Enter test cases")))

df = pd.read_csv("data.csv")
g1 = df.groupby(['flu'])
g2 = df.groupby(['chills', 'flu'])
g3 = df.groupby(['runny nose', 'flu'])
g4 = df.groupby(['headache', 'flu'])
g5 = df.groupby(['fever', 'flu'])

apriori_prob = g1.size().div(len(df))
conditional_prob = [g2.size().div(len(df)).div(apriori_prob, axis=0, level='flu'),
                    g3.size().div(len(df)).div(apriori_prob, axis=0, level='flu'),
                    g4.size().div(len(df)).div(apriori_prob, axis=0, level='flu'),
                    g5.size().div(len(df)).div(apriori_prob, axis=0, level='flu')]


def check(test):
	class1, class2 = apriori_prob[1], apriori_prob[0]

	for i, j in zip(test, conditional_prob):
		class1 *= j[i]['Y']
		class2 *= j[i]['N']

	if class1 > class2:
		return "YES FLU"
	else:
		return "NO FLU"

r=[]
for i in range(test):
	t=input().split()
	r.append(check(t))

for i in r:
	print(i)

print()
print("A PRIORI PROBABILITIES")
print(apriori_prob)
print()
print("CONDITIONAL PROBABILITIES")
print(conditional_prob)
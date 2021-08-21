import pandas as pd

test = int(input("Enter test cases"))

ds = pd.read_csv("data1.csv")
g1 = ds.groupby('class')
g2 = ds.groupby(['tyres', 'class'])

apriori_prob = g1.size().div(len(ds))
conditional_prob = g2.size().div(len(ds)).div(apriori_prob, axis=0, level='class')
conditional_prob = conditional_prob.unstack(fill_value=0).stack()

def check(test):
	class1 = apriori_prob['auto rickshaw'] * conditional_prob[test]['auto rickshaw']
	class2 = apriori_prob['car'] * conditional_prob[test]['car']
	class3 = apriori_prob['cycle'] * conditional_prob[test]['cycle']

	result = max(class1, class2, class3)
	if result == class1:
		return 'auto rickshaw'
	elif result == class2:
		return 'car'
	else:
		return 'cycle'


r=[]
for i in range(test):
	t=int(input())
	r.append(check(t))

for i in r:
	print("CLASS BELONGINGNESS IS :",i)

print()
print("APRIORI PROBABILITIES")
print(apriori_prob)
print()
print("CONDITIONAL PROBABILITIES")
print(conditional_prob)
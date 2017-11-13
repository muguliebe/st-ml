import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

# load csv
csv = pd.read_csv('data/iris.csv')

# extract column data
csv_data = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
csv_label = csv['Name']

# split data
train_data, test_data, train_label, test_label = train_test_split(csv_data,
                                                                  csv_label)

# train & predict
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

# scoring
ac_score = metrics.accuracy_score(test_label, pre)
print('score:', ac_score)

from sklearn import svm, metrics
import random, re

# load csv
csv = []
with open('data/iris.csv', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()     # remove line feed
        cols = line.split(',')  # split via comma

        # convert string to number
        fn = lambda n: float(n) if re.match(r'^[0-9\.]+$', n) else n
        cols = list(map(fn, cols))
        csv.append(cols)

# remove line of head
del csv[0]

# shuffle
random.shuffle(csv)

# split data
total_len = len(csv)
train_len = int(total_len * 2 / 3)
train_data = []
train_label = []
test_data = []
test_label = []

#
for i in range(total_len):
    data = csv[i][0:4]
    label = csv[i][4]
    if i < train_len:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)

# predict
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

# scoring
print('pre:', pre)
ac_score = metrics.accuracy_score(test_label, pre)
print('score:', ac_score)

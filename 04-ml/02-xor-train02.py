import pandas as pd
from sklearn import svm, metrics

xor_data = [
    #P, Q, result
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]


# split data
xor_df = pd.DataFrame(xor_data)
xor_data = xor_df.ix[:,0:1]
xor_label = xor_df.ix[:,2]

# predict
clf = svm.SVC()
clf.fit(xor_data, xor_label)
pre = clf.predict(xor_data)

# accuracy
ac_score = metrics.accuracy_score(xor_label, pre)
print('score:', ac_score)


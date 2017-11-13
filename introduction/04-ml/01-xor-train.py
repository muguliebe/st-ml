from sklearn import svm

xor_data = [
    #P, Q, result
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

data = []
label = []
for row in xor_data:
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p, q])
    label.append(r)

# train
clf = svm.SVC()
clf.fit(data, label)

# predict
pre = clf.predict(data)
print('predict:', pre)

# result
ok = 0
total = 0
for idx, answer in enumerate(label):
    p = pre[idx]
    if p == answer:
        ok += 1
    total +=1
print('result:', ok, '/', total, '=', ok/total)
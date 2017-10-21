import urllib.request as req
import gzip, os, os.path

# prepare for download
savepath = './mnist'
baseurl = 'http://yann.lecun.com/exdb/mnist'
files = [
    'train-images-idx3-ubyte.gz',
    'train-labels-idx1-ubyte.gz',
    't10k-images-idx3-ubyte.gz',
    't10k-labels-idx1-ubyte.gz'
]

# download
if not os.path.exists(savepath):
    os.mkdir(savepath)

for f in files:
    url = baseurl + '/' + f
    loc = savepath + '/' + f
    print('download:', url)
    if not os.path.exists(loc):
        req.urlretrieve(url, loc)

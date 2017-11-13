import os


def test():
    print('test')
    pass


def makeDataDicrectory():
    directory = '../data'
    if not os.path.exists(directory):
        os.makedirs(directory)

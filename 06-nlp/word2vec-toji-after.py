from gensim.models import word2vec

model = word2vec.Word2Vec.load('toji.model')
temp = model.most_similar(positive=['땅'])

print(temp)
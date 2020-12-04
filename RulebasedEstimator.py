#having collected lexical information (words and their frequencies) from corpus, explored ways to find adjectives in the data

from nltk.corpus import wordnet as wn

# create a list with all the adjectives in WordNet

sy = []

for synset in list(wn.all_synsets('a'))[:]:
    sy.append(synset)
    
print(len(sy))

adjList=[]
adjTweets=[]

# take the adjectives from the list obtained from WordNet because the type of the variable was a WordNet type
# iterate over the list of flattened tweet words and also over the list with the adjectives from WordNet
# add the adjectives that are on both lists to a new one

for i in sy:
    adjList.append(str(i)[8:-7])
 
for j in fTW:
    if j in adjList:
        adjTweets.append(j)
    
print (len(adjTweets))
print (adjTweets)

#frequency
fdist = nltk.FreqDist(adjTweets)

# We can print the most common words:
fdist.most_common(50)


def word_counts={}
    document={}
    for word in document:
        if word in word_counts():
            word_counts[word]+=1
        else:
            word_counts[word]=1

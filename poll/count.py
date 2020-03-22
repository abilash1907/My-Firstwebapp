import operator
def counter(art):
    words=art.split()
    word=len(words)
    dict_word={}
    for i in words:
        if i in dict_word:
            dict_word[i]+=1
        else:
            dict_word[i]=1
    var=sorted(dict_word.items(),key=operator.itemgetter(1),reverse=True)
    return var,word

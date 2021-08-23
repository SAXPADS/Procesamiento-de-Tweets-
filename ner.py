import spacy
import pandas as pd
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
tweets=pd.read_csv('Messi.csv')
def hacer_corpus(tweets):
    corpus = []
    for i in range(0, len(tweets)):
        #eliminamos los links y hasgtags
        tweets['text'][i] = " ".join([word for word in tweets['text'][i].split()
                                        if 'http' not in word and '@' not in word and '#' not in word])
        #definimos caracteres que pueden leer
        title = re.sub('[^a-zA-ZáéíóúñÁÉÍÓÚ]', ' ', tweets['text'][i])
        #transformamos las mayusculas en minusculas
        #title = title.lower()
        #generamos los arreglos respectivos para los tweets con los carcteres aceptados
        title = title.split()
        #print(title)
        #eliminamos aquellas palabras que esten en el stopwords del español
        #title = [word for word in title if (not word in FinalStopWords and word != "rt")]
        #volvemos a crear el corpus con las palabras aceptadas
        title = ' '.join(title) + " "
        corpus.append(title)
    return corpus
tw=hacer_corpus(tweets)
nlp=spacy.load("es_core_news_sm")
from spacy import displacy
#for twit in tw:
#    doc=nlp(twit)
#    print("===============")
#    print(twit)
#    print(doc.ents)
#    print("Sintagmas nominales:", [chunk.text for chunk in doc.noun_chunks])
#    print("Verbs:", [token for token in doc if token.pos_ == "VERB"])
#    print("asdsadsa")
#    for token in doc:
#        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#                token.shape_, token.is_alpha, token.is_stop)
#    print("asdsadsadsaaaaaaaaaa")
#    for entity in doc.ents:
#        print(entity.text, entity.label_)
df=pd.DataFrame()
verbo=[]
Det=[]
Prop=[]
adj=[]
for twit in tw:
    doc=nlp(twit)
    for token in doc:
        df[token.text]=None
        df.loc[token.pos_]=None
        
df = df.fillna(0)
for twit in tw:
    doc=nlp(twit)
    for token in doc:
        df[token.text][token.pos_]=df[token.text][token.pos_]+1
        if(token.pos_=="VERB"):
            verbo.append(token.text)
        if(token.pos_=="NOUN"):
            Det.append(token.text)
        if(token.pos_=="PROPN"):
            Prop.append(token.text)
        if(token.pos_=="ADJ"):
            adj.append(token.text)
        
           
    
print(df)

def MostrarNube(arreglo,Titulo):
    
    word_string=" ".join(arreglo)
    wordcloud = WordCloud(stopwords=STOPWORDS,
                              background_color='white', 
                          max_words=300
                             ).generate(word_string)
    plt.clf()
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.title(Titulo)
    plt.show()
                        
MostrarNube(tw,"Todo")
MostrarNube(verbo,"Verbo")
MostrarNube(Det,"Determinista")
MostrarNube(adj,"Adjetivo")
MostrarNube(Prop,"Nombre propio")

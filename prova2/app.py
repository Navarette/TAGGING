import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
#Moduli,librerie... da installare
# pip install scikit-learn
#pip install pandas


# preparazione data, text = input(es, recensioni), tags = sono i tag correspodenti
data = pd.read_csv('/workspace/PCTO/dataset/MOD_Amazon_Unlocked_Mobile.csv')  
# data per l'allenamento dell'AI
train_data = data['Product Name'][:280000]    
train_tags = data['Brand Name'][:280000]

# parte di data che verra' usata per valutare l'AI
test_data = data['Product Name'][280000:]     

# trasformo i dati da text in valori numerici con questa classe della libreria di sklearn
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(train_data)

# LogisticRegression serve per solvere problemi di classificazione binaria
# dove il variabile target puo' avere uno dei due classi, in questo caso positive o negative 
classifier = LogisticRegression()
# allenamento 
classifier.fit(X_train, train_tags)

# trasformo i dati da text in valori numerici come prima
X_test = vectorizer.transform(test_data)
#predizione
predictions = classifier.predict(X_test)

# print risultato
for i, text in enumerate(test_data[:11]):
    print(f"Text: {text} \t\t Predicted Tag: {predictions[i]}")
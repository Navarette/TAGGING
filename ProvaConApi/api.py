import pandas as pd
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Preparazione dei dati
api_endpoint = 'https://gutendex.com/books'  # Endpoint dell'API

# Eseguo una richiesta GET per ottenere i dati dall'API
response = requests.get(api_endpoint)
data = response.json()

# Suddivido i dati in set di addestramento e test
train_data = data['title'][:80]
train_tags = data['url'][:80]


# Creo un oggetto TfidfVectorizer e trasformo i dati di addestramento
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(train_data)

# Creo un classificatore di regressione logistica e lo addestro
classifier = LogisticRegression()
classifier.fit(X_train, train_tags)

# Trasformo i dati di test e faccio le previsioni
X_test = vectorizer.transform(test_data)
predictions = classifier.predict(X_test)

# Stampo i risultati
for i, text in enumerate(test_data):
    print(f"Text: {text} \t\t Predicted Tag: {predictions[i]}")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Läs in data
data = pd.read_csv('./combined_data/combined_data.csv')

# Separera attribut (texten av e-postmeddelandet) och målvariabel (spam eller inte spam)
X = data['text']
y = data['label']

# Dela datan i tränings- och testuppsättningar
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Skapa en vektorisering av texten
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Skapa och träna en Naive Bayes-modell
model = MultinomialNB()
model.fit(X_train_vectorized, y_train)

# Gör förutsägelser på testdatan
y_pred = model.predict(X_test_vectorized)

# Öppna en fil för att skriva resultatet
with open('klassificering_resultat.txt', 'w') as file:
    # Skapa en lista för att lagra index för missklassificerade meddelanden
    misclassified_indices = []

    # För varje testmeddelande, dess förutsägelse och faktiska etikett
    for i, (message, predicted_label, true_label) in enumerate(zip(X_test, y_pred, y_test)):
        # Skriv meddelandet och dess förutsägelse till filen
        file.write(f"Meddelande: {message}\n")
        file.write(f"Faktisk klassificering: {'Spam' if true_label == 1 else 'Inte spam'}\n")
        file.write(f"Modellens klassificering: {'Spam' if predicted_label == 1 else 'Inte spam'}\n")
        file.write("-" * 50 + "\n")

        # Om modellen har missat klassificeringen, lägg till index i listan
        if predicted_label != true_label:
            misclassified_indices.append(i)

# Skriv ut index för missklassificerade meddelanden
print("Index för missklassificerade meddelanden:", misclassified_indices)


# Utvärdera modellen
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

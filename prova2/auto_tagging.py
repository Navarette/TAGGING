import spacy
from spacy.matcher import PhraseMatcher

# pip install spacy
# python -m spacy download en_core_web_sm

# Taxonomy list
taxonomy = [
    "functional", "old", "smooth", "operating system", "good", "smartphone", "smartphones", "phone", "phones", "mobile device",
    "android", "ios", "windows phone", "ui (user interface)", "touchscreen", "processor", "technology", "mobile phones",
    "ram (random access memory)", "internal storage", "camera", "megapixels", "dual camera",
    "battery capacity", "mah (milliampere-hour)", "charging technology", "fast charging",
    "wireless charging", "display", "screen size", "resolution", "pixel density", "gorilla glass",
    "water resistance", "ip rating", "fingerprint sensor", "face recognition",
    "biometric authentication", "nfc (near field communication)", "bluetooth", "wi-fi", "5g", "lte",
    "sim card", "expandable storage", "usb type-c", "headphone jack", "smartphone brand",
    "apple", "samsung", "google", "huawei", "xiaomi", "oneplus", "sony", "lg", "motorola", "nokia",
    "htc", "blackberry", "lenovo", "oppo", "vivo", "realme", "asus", "zte", "alcatel", "honor",
    "meizu", "infinix", "tecno", "itel", "micromax", "panasonic", "sharp", "tcl", "leeco", "gionee",
    "lava", "nubia", "redmi", "poco", "moto", "vodafone", "jio", "mtn", "telstra"
]


def tag_text(text, taxonomy):
    # language model
    nlp = spacy.load('en_core_web_sm')

    # Processo il testo
    doc = nlp(text)

    # creo un PhraseMatcher per controllare la frase con tutte le parole nella lista di tassonomia
    matcher = PhraseMatcher(nlp.vocab)
    for phrase in taxonomy:
        # converto tutti un lettere minuscole
        matcher.add("Taxonomy", [nlp(phrase.lower())])

    # prendo le parole che coincidono con quelli dentro la lista di tassonomia
    matches = matcher(doc)

    # prendo i tag - list e set sono per far si' che i tag non si ripetino
    tags = list(set(doc[start:end].text for _, start, end in matches))

    return tags


# input
text = input("Enter the text you want to tag: ")


# richiamo la classe
tags = tag_text(text, taxonomy)
# stampo il risultato
print("Text:", text)
print("Tags:", tags)

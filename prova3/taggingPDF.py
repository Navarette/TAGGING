import spacy
from spacy.matcher import PhraseMatcher
from pdfminer.high_level import extract_text

# Taxonomy list
taxonomy = [
    # Programming Languages
    "Python", "JavaScript", "Java", "C++", "C#", "Ruby", "Go", "Swift", "Rust", "PHP",

    # Technology Companies
    "Tesla", "Apple", "Microsoft", "Google", "Amazon", "Facebook", "IBM", "Intel", "Nvidia", "Samsung",

    # News and Media
    "Breaking news", "Hea.dlines", "Journalism", "Broadcast", "Press release", "Media coverage",
    "Editorial", "Op-ed", "Investigative reporting", "Public relations",

    # Scientific Fields
    "Physics", "Chemistry", "Biology", "Astronomy", "Geology", "Mathematics", "Psychology",
    "Sociology", "Anthropology", "Economics",

    # Arts and Entertainment
    "Film", "Music", "Literature", "Theater", "Visual arts", "Dance", "Television", "Gaming",
    "Photography", "Fashion",

    # Sports
    "Soccer", "Basketball", "Tennis", "Golf", "Baseball", "Athletics", "Swimming", "Cricket",
    "Rugby", "Volleyball",

    # Global Issues
    "Climate change", "Human rights", "Poverty", "Education", "Healthcare", "Sustainability",
    "Gender equality", "Social justice", "Conflict resolution", "Immigration",

    # Business and Finance
    "Entrepreneurship", "Startups", "Investments", "Stock market", "Financial planning", "Banking",
    "Insurance", "Marketing", "E-commerce", "Supply chain",

    # Travel and Tourism
    "Destinations", "Hotels", "Airlines", "Vacation packages", "Sightseeing", "Adventure travel",
    "Sustainable tourism", "Travel insurance", "Cultural experiences", "Backpacking",

    # Health and Wellness
    "Nutrition", "Exercise", "Mental health", "Yoga", "Meditation", "Alternative medicine",
    "Wellness retreats", "Healthy living", "Stress management", "Self-care",

    # Smartphone-related terms
    "Smartphone", "Mobile device", "Operating system", "Android", "iOS", "Windows Phone",
    "UI (User Interface)", "Touchscreen", "Processor", "RAM (Random Access Memory)",
    "Internal storage", "Camera", "Megapixels", "Dual camera", "Battery capacity",
    "mAh (milliampere-hour)", "Charging technology", "Fast charging", "Wireless charging",
    "Display", "Screen size", "Resolution", "Pixel density", "Gorilla Glass",
    "Water resistance", "IP rating", "Fingerprint sensor", "Face recognition",
    "Biometric authentication", "NFC (Near Field Communication)", "Bluetooth", "Wi-Fi",
    "5G", "LTE", "SIM card", "Expandable storage", "USB Type-C", "Headphone jack",
    "Smartphone brand", "Apple", "Samsung", "Google", "Huawei", "Xiaomi", "OnePlus",
    "Sony", "LG", "Motorola", "Nokia", "HTC", "BlackBerry", "Lenovo", "Oppo",
    "Vivo", "Realme", "ASUS", "ZTE", "Alcatel", "Honor", "Meizu", "Infinix",
    "Tecno", "Itel", "Micromax", "Panasonic", "Sharp", "TCL", "LeEco", "Gionee",
    "Lava", "Nubia", "Redmi", "Poco", "Moto", "Vodafone", "Jio", "MTN", "Telstra"
]

# classe per estrarre il testo dal pdf


def extract_text_from_pdf(file_path):
    return extract_text(file_path)


def tag_pdf(file_path, taxonomy):
    # Estrai il testo dal PDF
    text = extract_text_from_pdf(file_path)

    # Carica il modello linguistico
    nlp = spacy.load('en_core_web_sm')

    # Processa il testo
    doc = nlp(text)

    # Crea il PhraseMatcher per controllare le frasi con le parole nella tassonomia
    matcher = PhraseMatcher(nlp.vocab)
    for phrase in taxonomy:
        # Converti tutto in minuscolo
        matcher.add("Taxonomy", [nlp(phrase.lower())])

    # Trova le corrispondenze con la tassonomia nel testo
    matches = matcher(doc)

    # Ottieni i tag - utilizza una lista e un set per evitare duplicati
    tags = list(set(doc[start:end].text for _, start, end in matches))

    return tags


# Input
file_path = input("Enter the path of the PDF file: ")

# Richiama la funzione per il tagging del PDF
tags = tag_pdf(file_path, taxonomy)

# Stampa il risultato
print("Tags:", tags)

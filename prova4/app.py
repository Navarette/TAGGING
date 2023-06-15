import spacy
from spacy.matcher import PhraseMatcher
from pdfminer.high_level import extract_text
import PyPDF2
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
library = []

def tag_pdf(file_path, taxonomy):
    # Open the PDF file
    with open(file_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfFileReader(file)

        # Get the total number of pages
        total_pages = pdf_reader.numPages

        # Load the language model
        nlp = spacy.load('en_core_web_sm')

        # Create the PhraseMatcher to check phrases with words in the taxonomy
        matcher = PhraseMatcher(nlp.vocab)
        for phrase in taxonomy:
            # Convert everything to lowercase
            matcher.add("Taxonomy", [nlp(phrase.lower())])

        # Get the tags and their page numbers
        tags_with_page = {}
        for page_number in range(total_pages):
            # Extract the text from the current page
            page = pdf_reader.getPage(page_number)
            page_text = page.extractText()

            # Process the text
            doc = nlp(page_text)

            # Find the matches with the taxonomy in the text
            matches = matcher(doc)

            for match_id, start, end in matches:
                tag_text = doc[start:end].text
                if tag_text in tags_with_page:
                    if (page_number + 1) not in tags_with_page[tag_text]:  # Add 1 to page_number to convert from zero-based index
                        tags_with_page[tag_text].append(page_number + 1)
                else:
                    tags_with_page[tag_text] = [page_number + 1]  # Add 1 to page_number to convert from zero-based index

        return tags_with_page

file_paths = [
    '/workspace/TAGGING/prova4/pdf/art.pdf',
    '/workspace/TAGGING/prova4/pdf/programmingLanguage.pdf',
    '/workspace/TAGGING/prova4/pdf/smartphone.pdf'
]


for file_path in file_paths:
    tags_with_page = tag_pdf(file_path, taxonomy)
    library.append({'file_path': file_path, 'tags_with_page': tags_with_page})

# Print the resulting library
for item in library:
    print("File Path:", item['file_path'])
    print("Tags with Page Numbers:")
    for tag, page_numbers in item['tags_with_page'].items():
        print("Tag:", tag)
        print("Page Numbers:", page_numbers)
        print()
    print()
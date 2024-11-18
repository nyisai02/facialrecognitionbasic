import pyttsx3
import PyPDF2

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Adjust the rate (words per minute) - you can tweak this to suit your preference
rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate - 30)  # Slowing down the speech rate

# Adjust the volume (0.0 to 1.0)
volume = speaker.getProperty('volume')
speaker.setProperty('volume', 0.2)  # Max volume

# Select a voice - you can list available voices and choose one
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)  # You can change the index to select a different voice

# Open the PDF file
with open('JavaScript-Book-by-Ei-Maung.pdf', 'rb') as book:
    pdfReader = PyPDF2.PdfReader(book)
    pages = len(pdfReader.pages)
    print(pages)
    
    # Read and process a specific page
    page = pdfReader.pages[1]
    text = page.extract_text()
    
    # Speak the text
    if text.strip():  # Check for non-empty text
        speaker.say(text)
        speaker.runAndWait()

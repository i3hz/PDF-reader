import pyttsx3
import fitz 
import os
from multiprocessing import Pool

def main():
    file_path = input("Enter the path to the PDF file: ")
    output_file = input("Enter the name of the output audio file: ")

    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return

    try:
        text_chunks = extract_text_from_pdf(file_path)
    except Exception as e:
        print(f"An error occurred while extracting text from the PDF: {str(e)}")
        return

    try:
        with Pool() as p:
            p.map(text_to_speech, [(text, f"{output_file}_{i}.mp3") for i, text in enumerate(text_chunks)])
    except Exception as e:
        print(f"An error occurred while converting text to speech: {str(e)}")
        return

    print("The text-to-speech conversion was successful!")

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text_chunks = []
    for page in doc:
        text_chunks.append(page.get_text().strip().replace("\n", " "))
    return text_chunks

def text_to_speech(args):
    text, output_file = args
    speaker = pyttsx3.init()
    speaker.save_to_file(text, output_file)
    speaker.runAndWait()

if __name__ == "__main__":
    main()

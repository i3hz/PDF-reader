import pyttsx3
import PyPDF2
import os

def main():
    file_path = input("Enter the path to the PDF file: ")
    output_file = input("Enter the name of the output audio file: ")

    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return

    try:
        text = extract_text_from_pdf(file_path)
    except Exception as e:
        print(f"An error occurred while extracting text from the PDF: {str(e)}")
        return

    try:
        text_to_speech(text, output_file)
    except Exception as e:
        print(f"An error occurred while converting text to speech: {str(e)}")
        return

    print("The text-to-speech conversion was successful!")

def extract_text_from_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text.strip().replace("\n", " ")

def text_to_speech(text, output_file):
    speaker = pyttsx3.init()
    speaker.save_to_file(text, f"{output_file}.mp3")
    speaker.runAndWait()

if __name__ == "__main__":
    main()

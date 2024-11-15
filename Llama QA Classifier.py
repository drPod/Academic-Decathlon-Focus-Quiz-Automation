from llama_cpp import Llama
import PyPDF2


def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file."""
    text = []
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text.append(page.extract_text())
    return "\n".join(text)


def split_into_segments(text):
    """Split text into potential Q&A segments.
    You might need to adjust this based on your PDF structure."""
    # This is a simple split - adjust the logic based on your PDF format
    segments = text.split("\n")
    return [s.strip() for s in segments if s.strip()]


def classify_segment(llm, text):
    """Use Llama to classify if text is a question or answer."""
    prompt = f"""Determine if the following text is a question or an answer. 
    Respond with only 'QUESTION' or 'ANSWER'.
    
    Text: {text}
    Classification:"""

    response = llm(prompt, max_tokens=20, temperature=0)
    result = response["choices"][0]["text"].strip()

    return result


def process_pdf(pdf_path, model_path):
    """Process PDF and classify text segments."""
    # Initialize Llama
    llm = Llama(
        model_path=model_path,
        n_ctx=512,  # Adjust context window if needed
        n_threads=4,  # Adjust based on your CPU
    )

    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)

    # Split into segments
    segments = split_into_segments(text)

    # Classify each segment
    questions = []
    answers = []

    for segment in segments:
        if segment:  # Skip empty segments
            classification = classify_segment(llm, segment)
            if classification == "QUESTION":
                questions.append(segment)
            elif classification == "ANSWER":
                answers.append(segment)

    return questions, answers


def export_to_canvas_format(questions, answers, output_file):
    """Export Q&A pairs in a format ready for Canvas import."""
    # You'll need to adjust this based on Canvas's specific import format
    with open(output_file, "w") as f:
        for q, a in zip(questions, answers):
            f.write(f"Question: {q}\n")
            f.write(f"Answer: {a}\n")
            f.write("-" * 50 + "\n")


def main():

    pdf_path = "Math Focus Quizzes 2024.pdf"

    print(extract_text_from_pdf(pdf_path))

    # Replace these paths with your actual paths
    # model_path = "path_to_llama_model.gguf"  # Use appropriate Llama model
    output_path = "canvas_import.txt"

    # Process the PDF
    # questions, answers = process_pdf(pdf_path, model_path)

    # Export in Canvas format
    # export_to_canvas_format(questions, answers, output_path)

    # Print summary
    # print(f"Found {len(questions)} questions and {len(answers)} answers")
    # print(f"Results exported to {output_path}")


if __name__ == "__main__":
    main()

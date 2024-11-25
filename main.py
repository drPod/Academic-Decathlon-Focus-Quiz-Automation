import sort
import pdfToText
from CanvasClass import CanvasQuiz
import sys

# Check if a command line argument was provided
if len(sys.argv) < 2:
    print("Usage: python script.py <pdf_file>")
    sys.exit(1)

# Get the PDF filename from command line argument
quiz_import = sys.argv[1]

raw_text = pdfToText.extract_text_from_pdf(quiz_import)

# print(raw_text)

qBlocks = sort.split_questions(raw_text)

# Create a new quiz, don't hardcode the quiz name. Use the name of the pdf file.

quiz_id = 0
canvasQuizzes = []
for block in qBlocks:
    n, q, a = sort.sort_into_questions_and_answers(
        block
    )  # n = question number, q = question, a = answers
    if n == "1":
        quiz_id += 1
        quiz = CanvasQuiz(quiz_id, quiz_import.split(".")[0] + " Quiz " + str(quiz_id))
        quiz.add_question(q, a, 0)
        canvasQuizzes.append(quiz)
    else:
        quiz.add_question(q, a, 0)

# print([x.get_formatted() for x in canvasQuizzes])

import os
from dotenv import load_dotenv
from canvasapi import Canvas

# Load environment variables from .env file
load_dotenv()

# Initialize Canvas API
CANVAS_TOKEN = os.getenv("CANVAS_TOKEN")
CANVAS_DOMAIN = os.getenv("CANVAS_DOMAIN", "canvas.instructure.com")
COURSE_ID = int(os.getenv("COURSE_ID"))

canvas = Canvas(CANVAS_DOMAIN, CANVAS_TOKEN)
course = canvas.get_course(COURSE_ID)


def delete_all_quizzes(course):
    for quiz in course.get_quizzes():
        quiz.delete()
        print(f"Deleted quiz: {quiz.title}")


# delete_all_quizzes(course)

for quiz in canvasQuizzes:

    new_quiz = course.create_quiz(quiz.get_formatted())
    print(f"Created quiz: {new_quiz.title}")

    for q in quiz.questions:
        new_question = new_quiz.create_question(**q)
        # print(q)
        print(f"Created question: {new_question.question_name}")
    print("")

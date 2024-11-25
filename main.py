import sort
import pdfToText
from CanvasClass import CanvasQuiz

#! Testing
# raw_text = ""
# raw_text += "8. Find the variance for the probability distribution below.\n"
# raw_text += "Value  -6 -3 2 4\n"
# raw_text += "Probability  .2 .4 .1 .3\n"
# raw_text += "a. 11\n"
# raw_text += "b. 13\n"
# raw_text += "c. 15\n"
# raw_text += "d. 17\n"
# raw_text += "e. 19\n"

# n, q, a = sort.sort_into_questions_and_answers(raw_text)

quiz_import = "Math Focus Quizzes 2024.pdf"

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


delete_all_quizzes(course)

new_quiz = course.create_quiz(quiz.get_formatted())
for q in quiz.questions:
    print(q)
    new_question = new_quiz.create_question(**q)
    print(f"Created question: {new_question}")

# for quiz in canvasQuizzes:

#     new_quiz = course.create_quiz(quiz.get_formatted())
#     print(f"Created quiz: {new_quiz.title}")

#     for q in quiz.questions:
#         new_question = new_quiz.create_question(q)
#         print(q)
#         print(f"Created question: {new_question.question_name}")
#     print("")

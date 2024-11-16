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
print(quiz.get_formatted())

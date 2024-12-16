from canvasapi import Canvas
from dotenv import load_dotenv
import os
from time import sleep

# Load environment variables from .env file
load_dotenv()

# Initialize Canvas API
CANVAS_TOKEN = os.getenv("CANVAS_TOKEN")
CANVAS_DOMAIN = os.getenv("CANVAS_DOMAIN", "canvas.instructure.com")
COURSE_ID = int(os.getenv("COURSE_ID"))

canvas = Canvas(CANVAS_DOMAIN, CANVAS_TOKEN)
course = canvas.get_course(COURSE_ID)

# print(type(course.get_quizzes()))

# for quiz in course.get_quizzes():
#     print(quiz.title)
#     print(
#         quiz.quiz_type
#     )  # quiz_type is 'assignment' for quizzes that are assignments, 'practice_quiz' for quizzes that are not assignments
#     print(quiz.allowed_attempts)

sleep(3)
print(
    "According to documentation, quiz.allowed_attempts should be set to -1 for unlimited attempts."
)

for quiz in course.get_quizzes():
    quiz.edit(quiz={"allowed_attempts": -1})
    print("Updated quiz: " + quiz.title)

for quiz in course.get_quizzes():
    print(quiz.title)
    print("Allowed attempts: " + str(quiz.allowed_attempts))
    print("")

import pdfToText

# raw_text = pdfToText.extract_text_from_pdf("Math Focus Quizzes 2024.pdf")

# print(type(raw_text))
# print(raw_text)

# 8. Find the variance for the probability distribution below.
# Value  -6 -3 2 4
# Probability  .2 .4 .1 .3
# a. 11
# b. 13
# c. 15
# d. 17
# e. 19

# add the above text to the raw_text variable
raw_text = ""
raw_text += "8. Find the variance for the probability distribution below.\n"
raw_text += "Value  -6 -3 2 4\n"
raw_text += "Probability  .2 .4 .1 .3\n"
raw_text += "a. 11\n"
raw_text += "b. 13\n"
raw_text += "c. 15\n"
raw_text += "d. 17\n"
raw_text += "e. 19\n"

# print(raw_text)

# print(pdfToText.sort_into_questions_and_answers(raw_text))

q, a = pdfToText.sort_into_questions_and_answers(raw_text)

print(q)
print(a)

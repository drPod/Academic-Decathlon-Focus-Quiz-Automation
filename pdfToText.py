import PyPDF2


def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file."""
    text = []
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text.append(page.extract_text())
    return "\n".join(text)


# print(extract_text_from_pdf(pdf_path))


# def sort_into_questions_and_answers(text, qNumber):
#     """Sort text into questions and answers."""
#     question = ""
#     answers = []
#     for line in text.split("\n"):
#         # if line starts with an integer AND if the second character is a period
#         if line.isdigit() and line[1] == ".":
#             if line[0] == str(qNumber):
#                 question += line
#             else:
#                 answers.append(line)
#         # if the last line was a question AND this line starts with a character AND
#         # this line's second character isn't a period,
#         # append the current line to the question
#         elif question and line[0].isalpha() and line[1] != ".":
#             # concatenate the current line to the  question with a newline
#             question += "\n" + line
#         # if the line starts with a character and the second character is a period
#         elif line[0].isalpha() and line[1] == ".":
#             answers.append(line)


# def sort_into_questions_and_answers(text, qNumber):
#     """Sort text into questions and answers."""
#     question = ""
#     answers = []
#     for line in text.split("\n"):
#         # if line starts with an integer AND if the second character is a period
#         curr = line.split()
#         print(curr)
#         print(curr[0])
#         print(curr[0].split())

#         if curr[0].isdigit() and curr[1] == ".":
#             if curr[0] == str(qNumber):
#                 question += line
#             else:
#                 answers.append(line)
#         # if the last line was a question AND this line starts with a character AND
#         # this line's second character isn't a period,
#         # append the current line to the question
#         elif question and curr[0].split()[0].isalpha() and curr[0].split()[1] != ".":
#             # concatenate the current line to the  question with a newline
#             question += "\n" + line
#         # if the line starts with a character and the second character is a period
#         elif curr[0].split()[0].isalpha() and curr[0].split()[1] == ".":
#             answers.append(line)

# print(list(word[0]))


def sort_into_questions_and_answers(text):
    """Sort text into questions and answers."""
    question = ""
    answers = []
    for line in text.split("\n"):
        # if line starts with an integer AND if the second character is a period
        word = line.split(" ")
        try:
            if word[0][0].isdigit() and word[0][1] == ".":
                question += line
        except IndexError:
            # Ignore the index out of bounds error
            pass
        # if the last line was a question AND this line starts with a character AND
        # this line's second character isn't a period,
        # append the current line to the question
        try:
            if question and word[0].isalpha() and word[0][1] != ".":
                # concatenate the current line to the question with a newline
                question += "\n" + line
        except IndexError:
            # Ignore the index out of bounds error
            pass
        # if the line starts with a character and the second character is a period
        try:
            if word[0][0].isalpha() and word[0][1] == ".":
                answers.append(line)
        except IndexError:
            # Ignore the index out of bounds error
            pass
    return question, answers

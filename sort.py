def split_questions(text):
    """Split text by question"""
    # If the start of the line is "e.", then it's the last answer
    # This function will return just the block of text that contains the question and answers
    questions = []
    curr_question = []
    for line in text.split("\n"):
        curr_question.append(line)
        if line.startswith("e."):
            questions.append("\n".join(curr_question))
            curr_question = []

    return questions


def sort_into_questions_and_answers(text):
    """Sort text into questions and answers."""
    question = ""
    qNumber = 0
    answers = []
    for line in text.split("\n"):
        # if line starts with an integer AND if the second character is a period
        word = line.split(" ")
        try:
            if word[0][0].isdigit() and word[0][1] == ".":
                qNumber = word[0][0]
                question += line
        except IndexError:
            pass
        # if the line starts with two integers AND the third character is a period
        try:
            if word[0][0].isdigit() and word[0][1].isdigit() and word[0][2] == ".":
                qNumber = word[0][0] + word[0][1]  # concatenate the two integers
                question += line
        except IndexError:
            pass
        # if answers is empty AND the line starts with a character AND the second character is not a period
        try:
            if not answers and word[0][0].isalpha() and word[0][1] != ".":
                question += line
        except IndexError:
            pass
        # if answers is not empty AND the line starts with a character AND the second character is not a period
        try:
            if answers and word[0][0].isalpha() and word[0][1] != ".":
                answers.append(line)
        except IndexError:
            pass
        # if the line starts with a character and the second character is a period
        try:
            if word[0][0].isalpha() and word[0][1] == ".":
                answers.append(line)
        except IndexError:
            pass
    return qNumber, question, answers

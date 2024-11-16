class CanvasQuiz:
    """
    A parent class to represent a Canvas quiz that contains multiple questions.
    Only includes essential attributes needed for basic quiz functionality.
    """

    def __init__(self, quiz_id, title):
        self.quiz_data = {
            "id": quiz_id,
            "title": title,
            "quiz_type": "assignment",  # Default type
            "points_possible": 0,
            "question_count": 0,
            "published": False,
            "questions": [],
        }

    def add_question(self, question_text, answers, correct_index):
        """
        Creates and adds a new question to the quiz.

        Args:
            question_text (str): The text of the question
            answers (list): List of answer strings
            correct_index (int): Index of the correct answer (0-based)
        """
        position = len(self.quiz_data["questions"]) + 1
        question = CanvasQuestion(position, self)
        question.set_text(question_text)
        question.add_answers(answers, correct_index)
        self.quiz_data["questions"].append(question.get_formatted())
        self.quiz_data["question_count"] = len(self.quiz_data["questions"])
        self.quiz_data["points_possible"] = self.quiz_data["question_count"]
        return question

    def get_formatted(self):
        """Return the formatted quiz dictionary."""
        return self.quiz_data

    def publish(self):
        """Publish the quiz."""
        self.quiz_data["published"] = True
        return self


class CanvasQuestion:
    """
    A child class to represent a Canvas multiple choice question within a quiz.
    Each answer must be a dictionary with required fields as per Canvas API documentation.
    """

    def __init__(self, position, parent_quiz):
        self.parent_quiz = parent_quiz
        self.question_data = {
            "quiz_id": parent_quiz.quiz_data["id"],
            "position": position,
            "question_name": f"Question {position}",
            "question_type": "multiple_choice_question",
            "question_text": None,
            "points_possible": 1,
            "answers": [],
        }
        self.answer_id_counter = position * 1000  # To ensure unique answer IDs

    def set_text(self, text):
        """Set the question text."""
        self.question_data["question_text"] = text
        return self

    def add_answers(self, answers, correct_index):
        """
        Add answers as an array of properly formatted dictionaries.

        Args:
            answers (list): List of answer strings
            correct_index (int): Index of the correct answer (0-based)
        """
        answer_dicts = []
        for i, answer_text in enumerate(answers):
            answer_dict = {
                "id": self.answer_id_counter + i,
                "answer_text": answer_text.strip(),
                "answer_weight": 100 if i == correct_index else 0,
            }
            answer_dicts.append(answer_dict)

        self.question_data["answers"] = answer_dicts
        return self

    def get_formatted(self):
        """Return the formatted question dictionary."""
        if not self.question_data["question_text"] or not self.question_data["answers"]:
            raise ValueError(
                "Question must have both text and answers before formatting"
            )
        return self.question_data


# Example usage:
if __name__ == "__main__":
    # Create a new quiz
    quiz = CanvasQuiz(1, "Basic Math Quiz")

    # Add questions to the quiz
    quiz.add_question(
        "Which of the following is NOT a prime number?",
        ["15", "7", "11", "13"],
        correct_index=0,
    )

    quiz.add_question("What is 2 + 2?", ["3", "4", "5", "6"], correct_index=1)

    # Publish the quiz
    quiz.publish()

    # Get the formatted quiz - should match Canvas API format
    import json

    print(json.dumps(quiz.get_formatted(), indent=2))

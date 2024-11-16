import requests
from typing import Dict, Any


class CanvasAPI:
    """Handler for Canvas REST API interactions"""

    def __init__(self, access_token: str, domain: str):
        """
        Initialize the Canvas API handler

        Args:
            access_token (str): Your Canvas API access token
            domain (str): Your Canvas instance domain (e.g., 'canvas.instructure.com')
        """
        self.access_token = access_token
        self.base_url = f"https://{domain}/api/v1"
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

    def create_quiz(self, course_id: int, quiz_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new quiz in the specified course

        Args:
            course_id (int): The Canvas course ID
            quiz_data (dict): Formatted quiz data

        Returns:
            dict: The created quiz data from Canvas
        """
        endpoint = f"{self.base_url}/courses/{course_id}/quizzes"

        # Format the quiz data according to Canvas API requirements
        api_quiz_data = {
            "quiz": {
                "title": quiz_data["title"],
                "quiz_type": quiz_data["quiz_type"],
                "points_possible": quiz_data["points_possible"],
                "published": quiz_data["published"],
            }
        }

        response = requests.post(endpoint, headers=self.headers, json=api_quiz_data)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()

    def create_quiz_questions(
        self, course_id: int, quiz_id: int, questions: list
    ) -> list:
        """
        Create questions for a specific quiz

        Args:
            course_id (int): The Canvas course ID
            quiz_id (int): The Canvas quiz ID
            questions (list): List of formatted question dictionaries

        Returns:
            list: The created questions data from Canvas
        """
        endpoint = f"{self.base_url}/courses/{course_id}/quizzes/{quiz_id}/questions"
        created_questions = []

        for question in questions:
            response = requests.post(
                endpoint, headers=self.headers, json={"question": question}
            )
            response.raise_for_status()
            created_questions.append(response.json())

        return created_questions

    def get_courses(self) -> list:
        """
        Get a list of courses for the current user

        Returns:
            list: List of course dictionaries
        """
        endpoint = f"{self.base_url}/courses"
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()

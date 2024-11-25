# DemiDec Focus Quiz Automation

This project is intended for high school teachers importing DemiDec Focus Quizzes into the Canvas LMS. The project utilizes the [Canvas API Python wrapper](https://github.com/ucfopen/canvasapi) to automate the process of creating quizzes in Canvas. The project is designed to be run from the command line.

## Getting Started

You will need to first install Python 3.6 or later. You can download Python from the [official website](https://www.python.org/downloads/). You will also need to install the Canvas API Python wrapper and the pdfToText library. You can install these dependencies by running the following command in your terminal:

```bash
pip install canvasapi pdf2text PyPDF2 python-dotenv
```

Next, you will need to create a `.env` file in the root directory of the project. This file will store your Canvas API token, which you can obtain by clicking "Account" in the Canvas sidebar, then "Settings", then navigating to the "Approved Integrations" section. You can create a new token by clicking the "New Access Token" button. Once you have your token, run the following commands in your terminal:

```bash
touch .env
echo "CANVAS_TOKEN=<your-token-here>" > .env
echo "CANVAS_DOMAIN=<your-canvas-domain-here>" >> .env
echo "COURSE_ID=<your-course-id-here>" >> .env
```

You will need to replace `<your-token-here>`, `<your-canvas-domain-here>`, and `<your-course-id-here>` with your Canvas API token, your Canvas domain (e.g. `https://schoolname.instructure.com`), and the ID of the course you want to import quizzes into, respectively. You can find the course ID by navigating to the course in Canvas and looking at the URL. It will be the number at the end of the URL. For example, if the URL is `https://schoolname.instructure.com/courses/123456`, the course ID is `123456`.

## Usage

To run the script, navigate to the root directory of the project in your terminal and run the following command:

```bash
python main.py <path-to-quiz-pdf>
```

Replace `<path-to-quiz-pdf>` with the path to the PDF file containing the quiz you want to import. The script will automatically create multiple-choice questions in Canvas based on the questions in the PDF file. The questions will be added to a new quizzes in the specified course.

For example, if you have a PDF file named 'Math Focus Quizzes 2024.pdf' in the root directory of the project, you would run the following command:

```bash
python main.py "Math\ Focus\ Quizzes\ 2024.pdf"
```

The script will create a new quiz in the specified course with the questions from the PDF file. The quiz will be named based on the title of the PDF file.

At any point, you can use ctrl+c to stop the script.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

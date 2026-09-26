# Interactive Quiz Application

## Overview

Interactive Quiz Application is a command-line quiz tool written in Python. Users can choose a quiz topic, answer multiple-choice questions, see their score, and review saved quiz results.

## Features

- Choose from Python, Data Structures, and General CS quiz topics.
- Take multiple-choice quizzes with input validation and immediate feedback.
- Calculate scores and percentages.
- Save quiz results by username in `results.json`.
- View previous quiz results and an overall average percentage.

## Technologies and Tools

- Python 3.9 or later
- JSON for local result storage
- `unittest` for automated tests
- Git and GitHub

The project uses only Python's standard library; no additional packages are required.

## Install and Run

1. Clone the repository:

   ```bash
   git clone https://github.com/graciebagora/quiz_app.git

2. Change to the project directory:
   ```
   cd quiz_app
   ```
3. Run the application:
   ```
   python main.py
   ```
   On Windows, you can also use:
   ```
   py main.py
   ```
   The application creates results.json if it does not already exist.

## Testing
From the project root, run the unit tests with:
```
python -m unittest discover -s tests -p "test_*.py" -v
```
On Windows, you can use:
```
py -m unittest discover -s tests -p "test_*.py" -v
```
The current tests check correct-answer evaluation and quiz-result percentage calculation.


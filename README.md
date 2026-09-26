# Interactive Quiz Application

## Overview

Quiz Application is a python based command line quiz tool. The users can  select any topic of quiz, answer multiple option questions, view their result, saved quiz results.

## Features

- You can select any topic from the three i.e. Python, Data Structures, and General CS.
- Take quizzes with multiple options that checks input and gives feedback.
- Determine marks and percentage.
- Save quiz results by username in `results.json`.
- View previous quiz results and an overall average percentage.

## Technologies and Tools used

- Python 3.9 
- JSON for local result storage
- `unittest` for automated tests
- Git and GitHub

This project utilizes only the Standard Library of Python, and no packages.

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
   The app creates results.json if it does not already exist.

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


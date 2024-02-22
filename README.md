# Page Object Model with Selenium Sample Readme
This repository contains a sample of my work with Page Object Model (POM) with Selenium.

## Prerequisites
Before running the code, ensure that you have the following installed:

- Pytest
- Selenium

## Usage
1. Open Terminal
2. Navigate to the Project Directory
3. Run Tests with following command:
  
  ```
  pytest tests
  ```

If you want to generate a report using pytest-html, run the following command:
```
pytest --html=report.html
```

In this case, an HTML report will be generated.

## Running Specific Tests:

To run a specific test, use the following command:
```
pytest -k test_name tests/test_file.py
```

To run a specific file with the tests, use the following command:
```
pytest tests/test_file_name.py
```

## Notes
- Adjust paths and filenames as necessary according to your project structure.
- Ensure that you have the necessary permissions to install packages and execute commands.
- Replace `test_name` and `test_file_name` with the actual test name and file name, respectively.
  

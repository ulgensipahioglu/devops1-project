# RebTech AB - Internal Time-Reporting Application

This repository contains a simple Python application designed for RebTech AB to handle internal weekly time-reporting and hour calculations, alongside an automated testing and continuous integration setup.

## 1. What the Application Does
The core application (`app.py`) provides a robust calculation utility that takes the total hours worked by an employee in a week and automatically calculates:
* Standard working hours (up to 40 hours).
* Overtime hours (any hours worked beyond the standard 40-hour limit).

It includes automated unit tests written with `pytest` (`test_app.py`) to verify that the math behind the hour calculation works flawlessly under different scenarios.

## 2. How to Run the Application Locally
To set up and run this project on your local machine, follow these steps:

1. **Clone the repository:**

   git clone <https://github.com/ulgensipahioglu/devops1-project.git>
   cd devops1-project

2. **Install dependencies:**
Make sure you have Python installed, then install pytest for testing:

    pip install pytest

3. **Run the automated tests:**
Execute the test suite locally to verify everything works:

    pytest

## 3. How the CI Pipeline Works
This project implements a Continuous Integration (CI) pipeline powered by GitHub Actions, configured inside .github/workflows/main.yml.

Workflow Trigger Rules:
- Push: The pipeline automatically triggers whenever a developer pushes new code to the main or feature/time-calculator branches.

- Pull Request: It triggers automatically when a Pull Request is opened toward the main branch.

Pipeline Execution Steps:
When triggered, GitHub spins up a clean, isolated virtual environment running the latest Ubuntu Linux and performs the following automated steps:

1. Checkout Code: Downloads the repository code into the virtual environment.

2. Set up Python: Installs Python version 3.10 inside the container.

3. Install Dependencies: Upgrades pip and installs the required pytest library.

4. Run Tests: Executes the pytest command.

If all tests pass, the pipeline marks the build with a green checkmark, ensuring that new changes do not break existing features before they are merged into the main branch.
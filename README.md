# Python for DevOps: Mastering Real-World Automation

This repository contains all the code and materials for my Python for DevOps: Mastering Real-World Automation course. If you haven't enrolled yet, check the link below for a discount!

### ➡️ Course link (with a big discount 🙂): [https://www.lauromueller.com/courses/python-devops](https://www.lauromueller.com/courses/python-devops)

**Note:** You can find the code for the section about CI/CD for Python in the following repository: [https://github.com/lm-academy/python-devops-cicd-project](https://github.com/lm-academy/python-devops-cicd-project)

**Check my other courses:**

- 👉 [The Definitive Helm Course: From Beginner to Master](https://www.lauromueller.com/courses/definitive-helm-course)
- 👉 [Mastering Terraform: From Beginner to Expert](https://www.lauromueller.com/courses/mastering-terraform)
- 👉 [Mastering GitHub Actions: From Beginner to Expert](https://www.lauromueller.com/courses/mastering-github-actions)
- 👉 [The Complete Docker and Kubernetes Course: From Zero to Hero](https://www.lauromueller.com/courses/docker-kubernetes)
- 👉 [Write better code: 20 code smells and how to get rid of them](https://www.lauromueller.com/courses/writing-clean-code)

## Welcome!

I'm thrilled to have you here! This repository contains all the code, examples, and supplementary materials for my Python for DevOps course. My goal is to provide you with practical, real-world examples that will help you master Python for your automation and operational tasks.

## 🚀 Getting Started

To run the code examples locally, you'll need to set up your environment correctly. It is highly recommended to use a virtual environment to keep project dependencies isolated.

**IMPORTANT**: Make sure to have **Python 3.12.9** installed to follow along without running into any issues 😊 Up until the release of this course, Python 3.13.x presents a bug that prevents some native logging functionality from working correctly. Hopefully, this will be fixed in later Python releases soon, but to ensure a smooth experience, **Python 3.12.9** is recommended.

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/lm-academy/python-devops.git
    cd python-devops
    ```

2.  **Create and Activate a Virtual Environment**
    Create a new virtual environment (the conventional name is `.venv`):

    ```bash
    python3 -m venv .venv
    ```

    Activate it for your current shell session:

    ```bash
    # On macOS and Linux
    source .venv/bin/activate

    # On Windows
    .venv\Scripts\activate
    ```

    Your shell prompt should now be prefixed with `(.venv)`, indicating the environment is active.

3.  **Install Dependencies**
    The required packages for this course are listed in `requirements.txt`. Install them using pip:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Launch JupyterLab**
    Many of the initial lectures use Jupyter Notebooks (`.ipynb` files) for interactive demonstrations. You can launch the JupyterLab interface by running:
    ```bash
    jupyter lab
    ```
    This will open a new tab in your web browser, allowing you to navigate the project folders and open any `.ipynb` notebook files.

## 🧑‍💻 Following Along with the Course

This repository has two primary branches to support your learning:

- **`main` branch**: This branch contains the final, completed code for every lecture. Use it as a reference if you get stuck or want to see the finished solution.
- **`start` branch**: This branch is designed for you to follow along with the hands-on lectures. It contains the initial state for each lesson, including notebooks and markdown files, but with the code blocks often left for you to complete.

To switch to the `start` branch and code along with me, run:

```bash
git checkout start
```

## 📚 Course Structure

The repository is organized into modules, each corresponding to a section in the course. Here is an overview of what you will learn:

- **virtual-envs**: Learn why virtual environments are essential and how to use Python's built-in `venv` module to create and manage isolated project environments.

- **python-fundamentals**: Master the core building blocks of Python. This module covers variables, comments, data types (`str`, `int`, `list`, `dict`, `set`, `tuple`), conditionals, loops, functions, including `*args` and `**kwargs`, classes, among other topics

- **generators-decorators**: Explore advanced Python features that promote clean and efficient code. This section covers first-class functions, memory-efficient generators with `yield`, and powerful decorators for adding functionality like timing and retries.

- **error-handling**: Build resilient scripts by mastering error handling. This module covers the `try...except` block, raising built-in and custom exceptions, and using context managers for safe resource management.

- **logging**: Go beyond `print()` statements and learn to use Python's `logging` module. You'll explore logging levels, handlers, formatters, file-based logging with rotation, and modern structured logging with JSON.

- **files-regex-data-formats**: Dive into file I/O and data handling. You'll learn to work with filesystem paths using `pathlib`, process text with regular expressions (`re`), and handle common data serialization formats like **CSV**, **JSON**, and **YAML**.

- **interacting-with-os**: Write scripts that interact with the operating system. This module covers managing environment variables, executing external commands with `subprocess`, handling filesystem operations with `os` and `shutil`, and creating temporary files.

- **http-requests**: Learn to interact with web services and REST APIs using the powerful `requests` library. Topics include making GET/POST requests, passing parameters, handling authentication, and implementing robust error handling with retries and timeouts.

- **typing**: Improve code clarity and catch bugs early with Python's type hinting system. This module introduces basic and advanced types from the `typing` module, generics with `TypeVar`, and how to use static analysis tools like `mypy` to validate your code.

- **automated-testing**: Write professional, automated tests for your DevOps scripts using `pytest`. You will learn about assertions, fixtures for setup/teardown, markers for organizing tests, parametrization for DRY tests, and mocking external dependencies.

- **multi-file-projects**: Learn to structure larger Python applications. This module covers creating modules and packages (`__init__.py`), using absolute vs. relative imports, defining project metadata with `pyproject.toml`, and setting up a testable project layout.

I'm looking forward to seeing you in the course!

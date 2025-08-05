# Finance Learning Projects

This repository contains a collection of simple finance-related tools built as an exploration and learning journey into programming fundamentals. The goal was to understand basic concepts like user input, calculations, loops, and web development (HTML, CSS, JavaScript) through practical, business-oriented examples.

---

## Projects

### 1. Compound Interest Calculator (`calculator.py`)

* **Description:** This is the very first project, a simple Python script that calculates the future value of an investment based on an initial principal, an annual interest rate, and a number of years. It demonstrates basic Python input/output and a `for` loop for iterative calculations.

* **Key Learning Points:**

    * Getting user input (`input()`)

    * Type conversion (`float()`, `int()`)

    * Variables and basic arithmetic operations

    * Using `for` loops for iteration

    * Formatted output (`f-strings`)

### 2. Web-Based Compound Interest Calculator (`compound_interest.html`)

* **Description:** This project takes the concept of the compound interest calculator and brings it to the web. It's a single HTML file that uses **HTML** for structure, **Tailwind CSS** for styling, and **JavaScript** for the calculation logic.

* **Key Learning Points:**

    * Basic HTML structure (`<input>`, `<button>`, `<div>`, `<ul>`)

    * Integrating CSS frameworks (Tailwind CSS) for responsive and modern design

    * JavaScript DOM manipulation (getting element references, updating content)

    * Event listeners (`click` event)

    * Client-side calculation in JavaScript

### 3. Loan Amortization Schedule Calculator (`loan_amortization_calculator.html`)

* **Description:** This is a more advanced web-based calculator that generates a detailed amortization schedule for a loan. It calculates monthly payments, and then breaks down each payment into its interest and principal components, showing the remaining balance over the loan term. Like the compound interest web app, this is also a single HTML file leveraging HTML, Tailwind CSS, and JavaScript.

* **Key Learning Points:**

    * More complex financial formulas (loan payment calculation)

    * Generating structured data (tables) using JavaScript

    * Handling floating-point precision in financial calculations

    * Organizing and displaying tabular data on a web page

---

## How to Run

* **`calculator.py`**:

    * Ensure you have Python installed.

    * Open a terminal or command prompt.

    * Navigate to the directory where you saved `calculator.py`.

    * Run the script using: `python calculator.py`

    * Follow the prompts in the terminal.

* **`compound_interest.html` & `loan_amortization_calculator.html`**:

    * Open these `.html` files directly in any modern web browser. All the necessary code is within each file.

---

## Future Improvements

* **Add more input validation** (e.g. preventing negative interest rates for compound interest).

* **Implement additional features** (e.g. extra payments for loan amortization, different compounding frequencies).

* **Improve user interface** with more interactive elements or charts.

* **Refactor JavaScript** into separate functions for better organization.

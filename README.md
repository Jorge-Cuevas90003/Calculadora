# Calculator

A command-line calculator built in Python that uses prefix notation to perform calculations.

## Overview

Calculadora is a console-based application designed to perform mathematical computations. Its main feature is the use of **Prefix Notation (or Polish Notation)**, where the operator precedes its operands. The program includes a stylized welcome message and error handling for invalid inputs.

## Features

- **Supported Operations**:
  - Basic arithmetic: `+`, `-`, `*`, `/`, `%` (modulus), `div` (integer division)
  - Single-operand operations: `fact!` (factorial), `sqr` (square), `sqroot` (square root), `sen` (sine), `cos` (cosine), `tan` (tangent)
- **Input Format**: Expressions must follow Prefix Notation, be enclosed in parentheses, and have spaces between each element.
- **Error Handling**: Detects invalid expressions, division by zero, and incorrect parenthesis usage.
- **User Interface**: Displays a welcome animation and a user input prompt (`calculadora >>`).
- **Exit Command**: Type `quit` to exit the program.

## Installation

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/Jorge-Cuevas90003/Calculadora.git
    cd Calculadora
    ```

2.  **Requirements**:
    - Python 3.x
    - No external libraries required (uses standard libraries: `time`, `re`, `math`).

3.  **Run the Program**:
    ```bash
    python calculator.py
    ```

## Usage

1.  Run the program using the command above.
2.  At the `calculadora >>` prompt, enter a mathematical expression using **Prefix Notation**. The format is crucial: `(operator operand1 operand2)`.

    **Correct Format:**
    - `(+ 5 3)`
    - `(sqroot 16)`
    - `(+ 2 (* 3 4))`

    **Incorrect Format (will raise an error):**
    - `(5 + 3)`  *(Infix notation is not supported)*
    - `(+5 3)`  *(Missing spaces)*

3.  Type `quit` to exit.

## Examples

```
# Simple binary operation
calculadora >> (+ 5 3)
Resultado: 8

# Single-operand operation
calculadora >> (sqr 4)
Resultado: 16

# Simple nested operation (works correctly)
calculadora >> (+ 2 (* 3 4))
Resultado: 14

# Incorrectly formatted expression
calculadora >> 2 + 3
ERROR! Expresion no valida no tiene parentesis al inicio

# Exit the program
calculadora >> quit
Saliendo...
Adiós Usuario 🤙
```

## Limitations & Known Issues

It is important to note that the current evaluation logic has some limitations:

1.  **Incorrect Complex Calculations**: Expressions with multiple levels of nesting or parallel "branches" may produce incorrect results.
    - **Example**: The expression `(+ (* 2 3) (/ 8 4))` should yield `8`, but the program calculates **`18.0`**.
    - **Example**: The expression `(+ 2 (* 3 (- 10 4)))` should yield `20`, but the program calculates **`34`**.

2.  **Bug in `sqroot`**: The square root function (`sqroot`) is currently not working as intended. It tends to return the input number instead of the calculated result.
    - **Example**: `(sqroot 9)` returns `9` instead of `3`.

3.  **Strict Format Requirement**: The expression parser strictly requires a space between each operator and operand. `(+ 5 3)` works, but `(+5 3)` will not.

## Project Structure

- `calculator.py`: The main Python script containing the calculator logic.
- `README.md`: Project documentation.
- `.gitignore`: Excludes Python build artifacts and other unnecessary files.
- `LICENSE`: MIT License for open-source usage.

## Technologies Used

- **Python 3**: Core programming language.
- **Standard Libraries**:
  - `time`: For animation delays in the welcome message.
  - `re`: For parsing mathematical expressions using regular expressions.
  - `math`: For trigonometric and square root calculations.

## Author

- **Jorge Cuevas**  
  GitHub: [Jorge-Cuevas90003](https://github.com/Jorge-Cuevas90003)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

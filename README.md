# CLI Calculator 🧮

A simple command-line calculator built with Python. This project allows users to perform basic arithmetic operations directly in their terminal or command prompt.

It is designed to be easy to use and beginner-friendly. It is also a useful learning project for people who are getting started with Python and want to understand user input, variables, conditional statements, loops, exception handling, and functions of a command-line program.

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [How to Run the Calculator](#how-to-run-the-calculator)
- [How to Use the Calculator](#how-to-use-the-calculator)
- [Supported Operators](#supported-operators)
- [How to Quit](#how-to-quit)
- [Error Handling](#error-handling)
- [Example Session](#example-session)
- [How the Code Works](#how-the-code-works)
- [Possible Future Improvements](#possible-future-improvements)
- [Contributing](#contributing)
- [License](#license)

## About the Project

The CLI Calculator is a text-based application that runs in a terminal. Instead of using buttons and a graphical interface, the user follows prompts and types numbers and operators using the keyboard.

The calculator asks for a first number, an arithmetic operator, and a second number. It then calculates and displays the result. Users can perform another calculation or exit the program.

This project currently supports four basic arithmetic operations:

- Addition
- Subtraction
- Multiplication
- Division

The calculator also checks for invalid numeric input and prevents division by zero.

## Features

- **Simple interface:** Clear prompts guide the user through each calculation.
- **Basic arithmetic:** Supports addition, subtraction, multiplication, and division.
- **Decimal numbers:** Accepts whole numbers and decimal values, such as `8`, `3.5`, and `0.25`.
- **Division-by-zero protection:** Displays an error instead of attempting to divide by zero.
- **Input validation:** Handles values that cannot be converted into numbers.
- **Repeat calculations:** Allows users to perform multiple calculations without restarting the program.
- **Quit option:** Enter `q` at the operator prompt to exit the calculator.
- **Goodbye message:** Displays a farewell message when the user exits.

## Requirements

You need:

- **Python 3** installed on your computer.
- A code editor, such as [Visual Studio Code](https://code.visualstudio.com/) (optional but recommended).
- A terminal or command prompt.

The calculator uses Python's built-in features and does not require any third-party packages.

To check whether Python is installed, open a terminal and run:

```bash
python --version
```

On some systems, you may need to use:

```bash
python3 --version
```

If a Python version is displayed, Python is available through that command. If not, install Python 3 from the [official Python website](https://www.python.org/downloads/).

## Getting Started

1. Download or clone this project to your computer.
2. Open the project folder in your code editor or terminal.
3. Save the calculator code in a Python file, for example:

   ```text
   calculator.py
   ```

4. Open a terminal in the folder containing `calculator.py`.

If you are using Visual Studio Code, you can open the project folder and choose **Terminal → New Terminal** from the menu.

## How to Run the Calculator

In the terminal, run:

```bash
python calculator.py
```

If your system uses `python3`, run:

```bash
python3 calculator.py
```

You should see a welcome message similar to:

```text
Welcome to my CLI Calculator!
I can help you do calculations.
Enter your first number:
```

Follow the prompts and type your answers. Press **Enter** after each entry.

## How to Use the Calculator

Each calculation follows these steps.

### Step 1: Enter the first number

When prompted:

```text
Enter your first number:
```

Type the first number you want to calculate with.

Examples:

```text
8
12
4.5
```

Press **Enter** to continue.

### Step 2: Choose an operator

When prompted:

```text
Enter an operator (+, -, *, /, q):
```

Type one of the supported operators:

- `+` to add
- `-` to subtract
- `*` to multiply
- `/` to divide
- `q` to quit the calculator

Press **Enter** after entering your choice.

**Important:** Enter the operator symbol itself. For multiplication, use `*`, not the letter `x`.

If you enter `q`, the calculator displays the goodbye message and exits without asking for the second number.

### Step 3: Enter the second number

If you chose an arithmetic operator, the calculator asks:

```text
Enter your second number:
```

Type the second number and press **Enter**.

For example, if your first number is `8` and your operator is `+`, entering `3` as the second number produces the result `11`.

### Step 4: Read the result

The calculator displays the answer in this format:

```text
Result: 11
```

For decimal results, it displays the numeric result without unnecessary trailing zeros where applicable.

### Step 5: Choose whether to calculate again

After a calculation, the program asks:

```text
Do you want to calculate again? (yes/q):
```

- Type `yes` to start another calculation.
- Type anything other than `yes` to exit and display the goodbye message.

For clarity, enter `yes` if you want to continue. You can also quit at the operator prompt by entering `q`.

## Supported Operators

| Operator | Operation | Example | Result |
|---|---|---|---:|
| `+` | Addition | `8 + 3` | `11` |
| `-` | Subtraction | `8 - 3` | `5` |
| `*` | Multiplication | `8 * 3` | `24` |
| `/` | Division | `8 / 2` | `4` |

The calculator also accepts decimal numbers.

Examples:

| Calculation | Result |
|---|---:|
| `2.5 + 1.5` | `4` |
| `7.5 - 2` | `5.5` |
| `2.5 * 2` | `5` |
| `7 / 2` | `3.5` |

## How to Quit

There are two ways to leave the calculator:

1. **At the operator prompt:** Enter `q` when asked to choose an operator. The program displays the goodbye message and stops.
2. **After a calculation:** When asked whether you want to calculate again, enter anything other than `yes`. The program displays the goodbye message and stops.

Example:

```text
Enter an operator (+, -, *, /, q): q
Thank you for using my CLI Calculator!
```

## Error Handling

The calculator includes checks for common mistakes.

### 1. Invalid number input

The calculator expects numbers that Python can convert to a numeric value. If you type text such as `hello` when asked for a number, it displays:

```text
Error: Please enter valid numbers.
```

Enter a valid number when prompted.

Examples of valid input include `5`, `-2`, and `3.75`.

### 2. Division by zero

Dividing by zero is not allowed by this calculator. If you choose `/` and enter `0` as the second number, it displays:

```text
Error: Cannot divide by zero.
```

The calculator then returns to the beginning of the calculation loop.

### 3. Invalid operator

If you enter an operator other than `+`, `-`, `*`, `/`, or `q`, the calculator displays:

```text
Error: Invalid operator. Select either +, -, *, /
```

Choose one of the supported operators when prompted.

## Example Session

Here is an example of a complete calculation followed by another calculation and then exiting:

```text
Welcome to my CLI Calculator!
I can help you do calculations.
Enter your first number: 10
Enter an operator (+, -, *, /, q): *
Enter your second number: 3
Result: 30
Do you want to calculate again? (yes/q): yes
Enter your first number: 7
Enter an operator (+, -, *, /, q): /
Enter your second number: 2
Result: 3.5
Do you want to calculate again? (yes/q): no
Thank you for using my CLI Calculator!
```

## How the Code Works

The calculator uses several important Python concepts.

- **`print()`** displays messages and results in the terminal.
- **`input()`** asks the user to type a response.
- **Variables** such as `number1`, `number2`, `operator`, and `result` store information used by the program.
- **`float()`** converts numeric text into a number that can include decimal values.
- **`if`, `elif`, and `else`** select the calculation that matches the chosen operator.
- **`while True`** keeps the calculator running so users can perform repeated calculations.
- **`continue`** skips the rest of the current loop iteration and starts the next one.
- **`break`** exits the loop when the user chooses to quit.
- **`try` and `except ValueError`** handle invalid numeric input so the program can display an error message instead of stopping with an unhandled conversion error.
- **`.strip()`** removes spaces from the beginning and end of an input.
- **`.lower()`** converts the repeat response to lowercase, so entries such as `YES` are treated like `yes`.
- **An f-string with `:g`** formats the displayed result without unnecessary trailing decimal zeros.

## Possible Future Improvements

This is a beginner project, and it can be expanded over time. Possible additions include:

- Support for powers and remainders.
- A calculation history.
- More detailed input validation and clearer recovery after errors.
- Automated tests.
- A graphical user interface.
- More flexible quit commands.

These are ideas for future versions; they are not all included in the current calculator.

## Contributing

Suggestions and improvements are welcome. If you are learning Python, try adding one feature at a time, testing it, and documenting how it works.

A simple workflow is:

1. Make one small change.
2. Run the program.
3. Test both normal input and incorrect input.
4. Update this README if the user experience changes.

## License

Copyright and License
Copyright Notice & Educational Use License
Copyright © 2026. All rights reserved.

This CLI Calculator, including its source code, documentation, and associated materials, is the intellectual property of its owner.

Permitted Use

This project is made available for educational purposes only. Users may study the source code and learn from its implementation for personal learning, practice, and educational instruction.

Restrictions

Unless prior written permission is obtained from the owner, users may not:
- Use this project for commercial purposes.
- Redistribute, sell, or republish this project or modified versions of it.
- Claim ownership or authorship of the original work.
- Use this project in ways that infringe the owner's intellectual property rights.
- Use, reproduce, or adapt the project for purposes beyond the permitted educational use.
Permission for Other Uses

Anyone wishing to use, modify, distribute, publish, commercialize, or otherwise use this project beyond the permitted educational purposes must contact the owner and obtain permission in advance.

Anyone who becomes aware of suspected copyright infringement or unauthorized use is encouraged to contact the owner using the details below.

Contact the Owner
- Email: benedictonyeke29@gmail.com
- Phone: 07026345065
Disclaimer

This project is provided for educational purposes. Unauthorized use may violate the owner's rights and applicable laws. Nothing in this notice grants permission beyond the uses expressly stated above.

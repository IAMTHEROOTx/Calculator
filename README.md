# Calculator

This is a simple command-line calculator built in Python. It takes two numbers as input from the user and performs one of the four basic arithmetic operations: addition, subtraction, multiplication, or division.

## 📌 Features

- User-friendly text input
- Error handling for non-numeric input
- Supports the following operations: `+`, `-`, `*`, `/`
- Prevents division by zero
- Rounds the result of division to the nearest integer

## 💡 How It Works

1. The program prompts the user to input two numbers.
2. It checks whether both inputs are numeric.
3. The user selects an operation (`+`, `-`, `*`, `/`).
4. The program executes the operation and displays the result.

### Example usage:

```bash
Enter a number: 10
Enter a second number: 5
Choose an operation: You can do +, -, *, / *
The result of the operation * is 50
```

## 🚫 Error Handling

- If the user enters non-numeric input, the program prints an error message and exits.
- If the user tries to divide by 0, the program informs the user and exits gracefully.

### Example:

```bash
Enter a number: hello
Enter a second number: 3
Erreur: les deux nombres doivent être des nombres entiers
Fin du programme
```

## 🛠️ How to Run

Make sure you have Python installed. Then, simply run the script:

```bash
python calculator.py
```

## 📄 License

This project is open-source and provided for educational purposes. Feel free to use or modify it.

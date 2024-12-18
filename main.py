import streamlit as st

# Function definitions for operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Streamlit interface
def calculator():
    st.title("Simple Calculator")

    # Create input fields for numbers
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)

    # Create a radio button for selecting operation
    operation = st.radio("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))

    # Perform the calculation based on user choice
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)

    # Display the result
    st.write(f"Result: {result}")

# Run the calculator app
if __name__ == "__main__":
    calculator()

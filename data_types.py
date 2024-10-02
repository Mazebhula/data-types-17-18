def boolean():
    """
    Question 1 - Boolean

    Using the variable below, give it the value 'True', then print it.
    """
    staying_alive = False

    # enter your code here
    staying_alive = True
    print(staying_alive)

def integer():
    """
    Question 2 - Integer

    Create a program to accept two numbers from a user and multiply them, then print the product.
    """
    # enter your code here
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    total = num1 * num2
    print(f"The product is {total}")


def string():
    """
    Question 3 - String

    Assign your name to a variable below and print it.
    """

    # enter your code here
    name = "Evelyn"
    print(name)

def convert_to_float():
    """
    Question 4 - Float

    Convert the following integer to a float then print it.
    """
    int_num = 60
    # enter your code here
    print(float(int_num))

def all_data_types():
    """
    Question 5 - All Data Types

    Output the following sentence using the given variables.

    Welcome to the 2024 WeThinkCode_ where True learning costs R0.00
    """
    string_one = "Welcome to "
    string_two = " WeThinkCode_ where "
    string_3 = " learning costs R"
    bool_condition = True
    int_year = 2024
    float_cost = 0.00

    # enter your code here
    print(f"{string_one}{int_year}{string_two}{str(bool_condition)}{string_3}{float_cost:.2f}")


if __name__ == "__main__":
    """
    Run the entire program from here
    """
    boolean()
    integer()
    string()
    convert_to_float()
    all_data_types()
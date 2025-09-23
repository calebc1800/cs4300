"""
Task 2: Variables and Data Types
"""

def demonstrate_data_types():
    """
    Demonstrates various python data types (int, float, string, bool).

    Returns:
        dict: Dictionary containing each data type
    """

    # Values
    int_var = 18
    float_var = 18.189
    str_var = "Hello World"
    boolean_var = False

    # Print each var with type
    print(
        f" Integer: {int_var}\n",
        f"Float: {float_var}\n",
        f"String: {str_var}\n",
        f"Boolean: {boolean_var}"
    )

    return {
        'integer': int_var,
        'float': float_var,
        'string': str_var,
        'boolean': boolean_var
    }

if __name__ == "__main__":
    demonstrate_data_types()

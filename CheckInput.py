"""———————————————————————————————
    Check the inputs.
——————————————————————————————————"""

class CheckInput:

    # integer input (default)
    def readInt(inputMessage, errorMessage):
        """Verify that the entered data is an integer."""
        while True:
            try:
                value = int(input(inputMessage))
                break
            except:
                print(errorMessage)
        return value

    # integer input (default with default error message)
    def readIntDefaultErrorMessage(inputMessage):
        """Verifies that the data entered is an integer and if there is an error, it sends the error message by default (Enter an integer number)."""
        while True:
            try:
                value = int(input(inputMessage))
                break
            except:
                print('Error enter an integer number.')
        return value

    # integer input (range)
    def readIntRange(inputMessage, errorMessage, minValue, maxValue):
        """Verifies that the data entered is an integer within a range."""
        while True:
            try:
                value = int(input(inputMessage))
                if value < minValue or value > maxValue:
                    raise
                else:
                    break
            except:
                print(errorMessage)
        return value

    # integer input (range with default error message)
    def readIntRangeDefaultErrorMessage(inputMessage, minValue, maxValue):
        """Verifies that the data entered is an integer within a range, and if there is an error, it sends the default error message (Enter an integer within the range from the minimum value to the maximum value)."""
        while True:
            try:
                value = int(input(inputMessage))
                if value < minValue or value > maxValue:
                    raise
                else:
                    break
            except:
                print(f'Error enter an integer within the range of {minValue} to {maxValue}.')
        return value

    # float input (default)
    def readFloat(inputMessage, errorMessage):
        """Verify that the entered data is a float."""
        while True:
            try:
                value = float(input(inputMessage))
                break
            except:
                print(errorMessage)
        return value
    
    # float input (default with default error message)
    def readFloatDefaultErrorMessage(inputMessage):
        """Verifies that the data entered is a float and if there is an error, it sends the error message by default (Enter a float number)."""
        while True:
            try:
                value = float(input(inputMessage))
                break
            except:
                print('Error enter a float number.')
        return value
    
    # float input (range)
    def readFloatRange(inputMessage, errorMessage, minValue, maxValue):
        """Verifies that the data entered is a float within a range."""
        while True:
            try:
                value = float(input(inputMessage))
                if value < minValue or value > maxValue:
                    raise
                else:
                    break
            except:
                print(errorMessage)
        return value

    # float input (range with default error message)
    def readFloatRangeDefaultErrorMessage(inputMessage, minValue, maxValue):
        """Verifies that the data entered is a float within a range, and if there is an error, it sends the default error message (Enter a float within the range from the minimum value to the maximum value)."""
        while True:
            try:
                value = float(input(inputMessage))
                if value < minValue or value > maxValue:
                    raise
                else:
                    break
            except:
                print(f'Error enter a float within the range of {minValue} to {maxValue}.')
        return value

    # boolean input (default)
    def readBoolean(inputMessage, errorMessage):
        while True:
            try:
                value = str(input(inputMessage)).lower()
                if value.startswith('s') or value.startswith('y'):
                    value = True
                    break
                elif value.startswith('n'):
                    value = False
                    break
                else:
                    raise
            except:
                print(errorMessage)
        return value

    
    # boolean input (default with default error message)
    def readBooleanDefaultErrorMessage(inputMessage):
        while True:
            try:
                value = str(input(inputMessage)).lower()
                if value.startswith('s') or value.startswith('y'):
                    value = True
                    break
                elif value.startswith('n'):
                    value = False
                    break
                else:
                    raise
            except:
                print("Error enter yes or no.")
        return value


# created by dffr1903
# 05 / 13 / 2022

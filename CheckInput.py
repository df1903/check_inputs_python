"""———————————————————————————————
    Check the inputs.
——————————————————————————————————"""

class CheckInput:

    # integer input (default)
    def readInt(inputMessage, errorMessage):
        while True:
            try:
                value = int(input(inputMessage))
                break
            except:
                print(errorMessage)
        return value

    # integer input (default with default error message)
    def readIntDefaultErrorMessage(inputMessage):
        while True:
            try:
                value = int(input(inputMessage))
                break
            except:
                print('Enter an integer number.')
        return value

    # integer input (range)
    def readIntRange(inputMessage, errorMessage, minValue, maxValue):
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
        while True:
            try:
                value = int(input(inputMessage))
                if value < minValue or value > maxValue:
                    raise
                else:
                    break
            except:
                print(f'Enter an integer within the range of {minValue} to {maxValue}.')
        return value

    # boolean input
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

# created by dffr1903
# 05 / 13 / 2022

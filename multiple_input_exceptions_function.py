def process_input():
    try:
        numbers = [10, 20, 30]
        index = int(input("Enter list index: "))
        divisor = float(input("Enter divisor: "))
        return numbers[index] / divisor
    except ValueError:
        return "Error: Input must be numeric."
    except IndexError:
        return "Error: List index is invalid."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Incompatible input types."


print(f"Result: {process_input()}")

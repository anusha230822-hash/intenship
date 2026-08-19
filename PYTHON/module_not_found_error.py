try:
    import module_that_does_not_exist
except ModuleNotFoundError:
    print("Error: The requested module was not found.")

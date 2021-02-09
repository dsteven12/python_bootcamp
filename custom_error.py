class RuntimeErrorWithCode(TypeError): #If not a TypeError, can use a base error like 'Exception'
    """
    Exception raised when a specific error code is needed
    """
    def __init__(self, message, code):
        super().__init__(f"Error code {code}: {message}")
        self.code = code

err = RuntimeErrorWithCode("Ouch! An error happened.", 400)
print(f"Checking doc string of RuntimeErrorWithCode: {err.__doc__}")
raise err

class CustomError(TypeError):
    pass

raise CustomError("Ouch! An error happened.")
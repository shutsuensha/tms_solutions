class ValidationError(Exception):
    pass

class InvalidPageCountError(ValidationError):
    pass

class InvalidYearError(ValidationError):
    pass

class InvalidPriceError(ValidationError):
    pass
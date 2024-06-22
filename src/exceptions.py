class OptionsInterestError(Exception):
    pass

class ConnectionError(OptionsInterestError):
    pass

class DataRetrievalError(OptionsInterestError):
    pass

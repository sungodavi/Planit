from .api_error import APIError


class InputError(APIError):
    def __init__(self, message='Invalid Input'):
        super().__init__(422, message)

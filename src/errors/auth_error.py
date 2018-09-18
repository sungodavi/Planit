from .api_error import APIError


class AuthError(APIError):
    def __init__(self, message='Unauthorized'):
        super().__init__(status_code=403, message=message)

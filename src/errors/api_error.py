class APIError(Exception):
    def __init__(self, status_code=400, message='Error'):
        self.status_code = status_code
        self.message = message

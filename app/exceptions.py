from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler


class AppException(APIException):
    def __init__(self, message, status_code=500, caught=None, detail=None):
        super().__init__()
        self.message = message
        self.status_code = status_code
        self.caught = caught
        self.detail = detail

    @property
    def type(self):
        return __class__.__name__

    def __repr__(self):
        return f"{self.type}: {self.message} - {self.detail}"

    def __str__(self):
        return self.__repr__()


def handler(exception, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.

    if not isinstance(exception, APIException):
        print(exception)
        exception = AppException(
            "Unhandled Error", caught=exception, detail=str(exception)
        )

    response = exception_handler(exception, context)

    # Now add the HTTP status code to the response, and handle specific API errors
    if response is not None:
        if isinstance(response.data, list) and response.data:
            response.data = {"detail": response.data}

        response.data["status_code"] = response.status_code
        if isinstance(exception, AppException):
            del response.data["detail"]
            response.data["error"] = {}
            response.data["error"]["type"] = exception.type
            response.data["error"]["message"] = exception.detail

    return response

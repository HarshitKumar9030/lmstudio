class LMStudioAPIError(Exception):
    """Base class for exceptions related to the LM Studio API."""
    pass

class LMStudioInvalidResponseError(LMStudioAPIError):
    """Exception raised when the API response is invalid."""
    def __init__(self, message="The API response is invalid."):
        self.message = message
        super().__init__(self.message)

class LMStudioRequestError(LMStudioAPIError):
    """Exception raised for errors in API requests."""
    def __init__(self, message="An error occurred while making the API request."):
        self.message = message
        super().__init__(self.message)

class LMStudioAuthenticationError(LMStudioAPIError):
    """Exception raised for authentication errors."""
    def __init__(self, message="Authentication failed. Please check your API key."):
        self.message = message
        super().__init__(self.message)
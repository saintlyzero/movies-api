import datetime as d

class Constants:

    """
        This class contains all the constants used by Movie_api 
    """
    
    # Messages
    CREDENTIALS_MISSING = "Credentials Missing"
    CREDENTIALS_INVALID = "Invalid Credentials"
    CREDENTIALS_VALID = "Valid Credentials"
    RECORD_NEW = "Added new record"
    RECORD_DELETED = "Deleted record"
    RECORD_UPDATED = "Updated record"
    RECORD_UPDATE_FAIL = "Failed Updating record"
    RECORD_NOT_EXISTS = "Specified record does not exists"
    FORBIDDEN = "You don't have enough permissions"
    PARAMETERS_MISSING = "Missing required Parameters"
    DATA_VALID = "Valid Data"
    DATA_INVALID = "Invalid Data"
    MISSING_MOVIE_ID = "Missing Movie_Id"
    TITLE_ERROR = "Title should have length between 1 - 100"
    DESCRIPTION_ERROR = "Description should have length between 1 - 200"
    RATING_ERROR = "Rating value should be between 0 - 5"
    YEAR_ERROR = "Year value should be between 1980 - current year"
    INVALID_KEY = "Invalid Key"
    NOT_AUTHORIZED = "Not Authorized to perform this operation"
    MOVIE_DETAILS_SUCCESS = "Success fetching movie details"
    MOVIE_DETAILS_FAIL = "Error fetching movie details"
    EMPTY_RESULTSET = "Empty result-set"
    
    # Keys
    IS_ROOT = "is_root"
    MESSAGE = "message"
    DATA = "data"
    CREDENTIALS = "credentials"
    STATUS = "status"
    RESULT = "result"
    MOVIE_TITLE = "title"
    MOVIE_DESCRIPTION = "description"
    MOVIE_RATING = "rating"
    MOVIE_YEAR = "year"
    MOVIE_ID = "id"
    RECORD = "record"
    ERROR = "error"
    TOKEN = "token"
    
    # Status
    STATUS_OK = 200
    STATUS_FORBIDDEN = 403
    STATUS_UNAUTHORIZED = 401
    STATUS_BAD_REQUEST = 400

    # Values
    RATING_MIN_VALUE = 0
    RATING_MAX_VALUE = 5
    TITLE_MIN_LENGTH = 1
    TITLE_MAX_LENGTH = 100
    DESC_MIN_LENGTH = 1
    DESC_MAX_LENGTH = 200
    YEAR_MIN_VALUE = 1980
    YEAR_MAX_VALUE = int(d.datetime.now().year)
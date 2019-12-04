class Constants:
    
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
    TOKEN_INVALID = "Invalid Token, please login"
    
    # Keys
    IS_ROOT = "is_root"
    MESSAGE = "message"
    DATA = "data"
    CREDENTIALS = "credentials"
    EMAIL = "email"
    IS_ADMIN = "is_admin"
    STATUS = "status"
    RESULT = "result"
    RECORD = "record"
    ERROR = "error"
    USER_EMAIL = "email" 
    USER_ID = "user_id"
    USER_PASSWORD = "password"
    TOKEN_EXPIRY = "exp"
    TOKEN = "token"

    # Status
    STATUS_OK = 200
    STATUS_FORBIDDEN = 403
    STATUS_UNAUTHORIZED = 401
    STATUS_BAD_REQUEST = 400

    # Value
    TOKEN_EXPIRY_TIME = 3000
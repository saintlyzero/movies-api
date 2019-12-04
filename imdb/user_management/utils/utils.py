import jwt
import datetime

from django.conf import settings
from .constants import Constants
from ..models import Users


class Utils:
    
    """
        This class contains all the util methods required for user_management
    """
    
    @staticmethod
    def build_response(status, result, record=None):
        """
            Builds Response

            parameters:
            -------

            status: Result status code of the specified operation 
            result: Message signifying the result of the specified operation 
            record: <optional> Dictionary/List containing the affectd data

        """
        if record:
            return {
            Constants.STATUS: status,
            Constants.RESULT: result,
            Constants.RECORD: record
        }

        return {
            Constants.STATUS: status,
            Constants.RESULT: result
        }


    @staticmethod
    def generate_token(data):
        """
            Generates JWT Token 
            and sets expiry time in seconds

            parameters:
            -------

            data : {
                email: user_email,
                is_root: true/false,
                exp: 3000
            }
        """
        data[Constants.TOKEN_EXPIRY] = datetime.datetime.utcnow() + datetime.timedelta(seconds=Constants.TOKEN_EXPIRY_TIME)
        encoded_jwt = jwt.encode(data, settings.TOKEN_SALT, algorithm=settings.ENCRYPTION_ALGO)
        return encoded_jwt
    

    @staticmethod
    def decode_token(data):
        """
            Decodes JWT Token 
            

            parameters:
            -------

            data : encoded JWT token
        """
        decoded_jwt = jwt.decode(data, settings.TOKEN_SALT, algorithm=settings.ENCRYPTION_ALGO)
        return decoded_jwt

    
    @staticmethod
    def get_exisiting_token(user_email):
        """
            Checks whether a token 
            has already been generated 
            corresponding to the user
        

            parameters:
            -------

            user_email : user email address
        """

        # Fetch user
        user = Users.objects.get(email=user_email)

        # Get User Token
        existing_token = user.token
        if existing_token:
            try:
                Utils.decode_token(existing_token)
            except Exception as e:
                print("error checking exisiting token: ",e)
                return False
        return existing_token


    @staticmethod
    def update_user_token(user_email, new_token):
        """
            Updates the token in database
            corresponding to the user
        

            parameters:
            -------

            user_email : user email address
            new_token : New JWT Token
        """
        try:
            # fetch user
            user = Users.objects.filter(email=user_email)
            user.update(token = new_token.decode('utf-8'))
        except Exception as e:
            print("error updating token: ",e)
            return False
        return True






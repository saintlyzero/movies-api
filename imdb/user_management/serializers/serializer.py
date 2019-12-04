from django.contrib.auth.hashers import make_password
from django.conf import settings
from rest_framework import serializers

from ..models import Users
from ..utils.constants import Constants
from ..utils.utils import Utils


class AuthorizeUser():
    """
        Class contains methods for validation of user_management data
    """

    @staticmethod
    def validate_user(data):
        """
            Verifies user with supplied credentials
        """
        response = {}
        user_email = data.get(Constants.USER_EMAIL,None)
        user_password = data.get(Constants.USER_PASSWORD, None)
        user_token = data.get(Constants.TOKEN, None)
        token = None

        # if email and password is present
        if user_email and user_password:
            try:
                # generate hashed password 
                hashed_password = make_password(user_password, settings.PASSWORD_SALT)

                # Check is user exists
                user = Users.objects.get(email=user_email, password = hashed_password)
                
                # Generate token data
                token_data = {
                    Constants.USER_EMAIL : user_email,
                    Constants.IS_ROOT : user.is_admin
                }

                # Check if user already has a valid token
                existing_token = Utils.get_exisiting_token(user_email)
                if existing_token:
                    token = existing_token
                else:
                    # Generate new token
                    token = Utils.generate_token(token_data)
                    Utils.update_user_token(user_email, token)
                
                # Add token to the response
                response[Constants.MESSAGE] = Constants.CREDENTIALS_VALID
                response[Constants.DATA] = {Constants.IS_ROOT:user.is_admin}
                response[Constants.TOKEN] = token
            except Exception as e:
                print("** Exception: ",e)
                response[Constants.MESSAGE] = Constants.CREDENTIALS_INVALID
        
        # if token is present
        elif user_token:
                try:
                    # validate token
                    token = Utils.decode_token(user_token)
                    response[Constants.MESSAGE] = Constants.CREDENTIALS_VALID
                    response[Constants.DATA] = {Constants.IS_ROOT:token[Constants.IS_ROOT]}
                except Exception as e:
                    response[Constants.MESSAGE] = Constants.TOKEN_INVALID
        else:
            response[Constants.MESSAGE] = Constants.CREDENTIALS_MISSING
        return response



class AddUserSerializer(serializers.ModelSerializer):
    """
        User Serializer validates every field 
        from the Users model
    """
    class Meta:
        model = Users
        fields =("__all__")

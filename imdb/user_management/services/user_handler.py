from django.contrib.auth.hashers import make_password
from django.conf import settings

from ..utils.constants import Constants
from ..serializers.serializer import AddUserSerializer
from ..models import Users
from ..utils.utils import Utils

class UserHandler:
    """
        Class to manage all user_management activities 
    """

    @staticmethod
    def add_user(data):
        """
            Adds a new user

            parameters:
            -------

            data : {
                        "email":"admin123@gmail.com",
                        "password":"admin",
                        "is_admin":true
                    }
        """

        response = {}
        user_details = AddUserSerializer(data = data)

        # Validate input user data
        if user_details.is_valid():
            plain_password = data[Constants.USER_PASSWORD]

            # Generate hashed password
            data[Constants.USER_PASSWORD] = make_password(plain_password, settings.PASSWORD_SALT)
            
            # Add new record
            user = Users(**data)
            user.save()
            response = Utils.build_response(Constants.STATUS_OK, Constants.RECORD_NEW, record={
                Constants.EMAIL: user.email,
                Constants.IS_ADMIN: user.is_admin})
        else:
            response = Utils.build_response(Constants.STATUS_BAD_REQUEST, user_details.errors)
        return response


    @staticmethod
    def delete_user(user_email):

        """
            Deletes user

            parameters:
            -------

            user_email : "admin123@gmail.com"
        """
        response = {}
        try:

            # check if user exists
            user = Users.objects.get(email=user_email)

            # delete user record
            user.delete()
            response = Utils.build_response(Constants.STATUS_OK, Constants.RECORD_DELETED, record={
                Constants.USER_EMAIL: user_email})
        except Exception as e:
            response = Utils.build_response(Constants.STATUS_OK, Constants.RECORD_NOT_EXISTS)
        finally:
            return response
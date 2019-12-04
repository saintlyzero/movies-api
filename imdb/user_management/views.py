from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers.serializer import AddUserSerializer, AuthorizeUser
from .utils.constants import Constants
from .utils.utils import Utils
from .services.user_handler import UserHandler
from .models import Users


class UserController(APIView):
    """
        This View handles all User related operations

        path: http://127.0.0.1:8000/user
    """

    def post(self, request):
        """
            Adds new User Record

            REQUEST:
            -------
            {
                "email":"admin@gmail.com",
                "password":"admin",
                "data": {
                    "email":"admin123@gmail.com",
                    "password":"admin",
                    "is_admin":true
            }

            RESPONSE:
            -------
            {
                "status": 200,
                "result": "Added new record",
                "record": {
                    "email": "admin123@gmail.com",
                    "is_admin": true
                }
                "token" : "sample_token"
            }
        """
        response = {}

        # Validate User
        validation_response = AuthorizeUser.validate_user(request.data)
        if validation_response[Constants.MESSAGE] == Constants.CREDENTIALS_VALID:
            
            # Authorise User
            if validation_response[Constants.DATA][Constants.IS_ROOT]:

                # Add new user
                response = UserHandler.add_user(request.data.get(Constants.DATA, None))
            else:
                response = Utils.build_response(Constants.STATUS_FORBIDDEN, Constants.NOT_AUTHORIZED)
            
            # Return Token
            if validation_response.get(Constants.TOKEN, None):
                response[Constants.TOKEN] = validation_response[Constants.TOKEN]
        else:
            response = Utils.build_response(Constants.STATUS_UNAUTHORIZED, validation_response[Constants.MESSAGE])
        return Response(response)



    def delete(self, request):
        """
            Deletes User Record

            REQUEST:
            -------
            {
                "email":"admin@gmail.com",
                "password":"admin",
                "data": {
                    "email":"admin123@gmail.com",
                    "password":"admin",
                    "is_admin":true
            }

            RESPONSE:
            -------
            {
                "status": 200,
                "result": "Deleted record",
                "record": {
                    "email": "admin123@gmail.com"
                }
                "token" : "sample_token"
            }
        """
        response = {}

        # Validate user
        validation_response = AuthorizeUser.validate_user(request.data)
        if validation_response[Constants.MESSAGE] == Constants.CREDENTIALS_VALID:

            # Authorize user
            if validation_response[Constants.DATA][Constants.IS_ROOT]:
                data = request.data.get(Constants.DATA, None)
                if data:

                    # Delete user
                    user_email = data.get(Constants.USER_EMAIL, None)
                    response = UserHandler.delete_user(user_email)
                else:
                    response = Utils.build_response(Constants.STATUS_BAD_REQUEST, Constants.PARAMETERS_MISSING)
            else:
                response = Utils.build_response(Constants.STATUS_FORBIDDEN, Constants.NOT_AUTHORIZED)

            # Return Token
            if validation_response.get(Constants.TOKEN, None):
                response[Constants.TOKEN] = validation_response[Constants.TOKEN]
        else:
            response = Utils.build_response(Constants.STATUS_UNAUTHORIZED, validation_response[Constants.MESSAGE])
        return Response(response)


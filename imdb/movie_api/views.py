from django.shortcuts import render 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Movies
from .serializers.serilizers import AddMovieSerializer, UpdateMovieSerializer
from  .utils.constants import Constants
from  .utils.utils import Utils
from .services.movie_handler import MovieHandler

from  user_management.serializers.serializer import AuthorizeUser
from  user_management.models import Users


class MovieController(APIView):
    """
        This View handles all Movie related operations

        path : /movie
    """

    def post(self, request):
        """
            Adds new Movie Record

            REQUEST:
            -------
            {
                "email":"admin@gmail.com",
                "password":"admin",
                "data": {
                    "title": "Superman ",
                    "description": "Superhero Movie",
                    "rating": 4.7,
                    "year": 2015
            }

            RESPONSE:
            -------
            {
                "status": 200,
                "result": "Added new record",
                "record": {
                    "title": "Golmal 4",
                    "id": 19
                }
                "token" : "sample_token"
            }
        """
        response = {}

        # Validate Request
        validation_response = AuthorizeUser.validate_user(request.data)
        
        # Authorize user
        if validation_response[Constants.MESSAGE] == Constants.CREDENTIALS_VALID:
            
                # Add Movie Entry
            if validation_response[Constants.DATA][Constants.IS_ROOT]:
                response = MovieHandler.add_movie(request.data.get(Constants.DATA, None))
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
            Deletes Movie Record

            REQUEST:
            ------
            {
                "email":"admin@gmail.com",
                "password":"admin",
                "data": {
                    "id":"19"
                }
            }

            RESPONSE:
            ------
            {
                "status": 200,
                "result": "Deleted record",
                "record": {
                    "title": "Golmal 4",
                    "id": "19"
                },
                "token": "sample_token"
            }
        """
        response = {}

        # validate user
        validation_response = AuthorizeUser.validate_user(request.data)
        if validation_response[Constants.MESSAGE] == Constants.CREDENTIALS_VALID:

            # Authorize user
            if validation_response[Constants.DATA][Constants.IS_ROOT]:
                data = request.data.get(Constants.DATA, None)
                
                # delete movie entry
                if data:
                    movie_id = data.get(Constants.MOVIE_ID, None)
                    response = MovieHandler.delete_movie(movie_id)
                else:
                    response = Utils.build_response(Constants.STATUS_BAD_REQUEST, Constants.PARAMETERS_MISSING)
            else:
                response = Utils.build_response(Constants.STATUS_FORBIDDEN, Constants.NOT_AUTHORIZED)
            
            # return Token
            if validation_response.get(Constants.TOKEN, None):
                response[Constants.TOKEN] = validation_response[Constants.TOKEN]
        else:
            response = Utils.build_response(Constants.STATUS_UNAUTHORIZED, validation_response[Constants.MESSAGE])
        return Response(response)



    def put(self, request):
        """
            Update Movie Record

            REQUEST:
            ------
            {
                "email":"admin@gmail.com",
                "password":"admin",
                "data": {
                    "id":18,
                    "description":"New Description",
                    "rating": 3.6
                }
            }

            RESPONSE:
            ------
            {
                "status": 200,
                "result": "Updated record",
                "record":  {
                    "id": 18,
                    "description": "New Description",
                    "rating": 3.6
                },
                "token": "sample_token"
            }
        """
        response = {}

        # Validate User
        validation_response = AuthorizeUser.validate_user(request.data)
        if validation_response[Constants.MESSAGE] == Constants.CREDENTIALS_VALID:

            # Authorize user
            if validation_response[Constants.DATA][Constants.IS_ROOT]:
                movie_validation_response = UpdateMovieSerializer.validate(request.data.get(Constants.DATA, None))
                
                # Update Movie Record
                if movie_validation_response[Constants.MESSAGE] == Constants.DATA_VALID:
                    new_movie_data = request.data[Constants.DATA]
                    response = MovieHandler.update_movie(new_movie_data)
                else:
                    if movie_validation_response.get(Constants.ERROR):
                        response = Utils.build_response(Constants.STATUS_BAD_REQUEST, movie_validation_response[Constants.MESSAGE], 
                        record= movie_validation_response[Constants.ERROR])
                    else:
                        response = Utils.build_response(Constants.STATUS_BAD_REQUEST, movie_validation_response[Constants.MESSAGE])
            else:
                response = Utils.build_response(Constants.STATUS_FORBIDDEN, Constants.NOT_AUTHORIZED)
           
            # Return Token
            if validation_response.get(Constants.TOKEN, None):
                response[Constants.TOKEN] = validation_response[Constants.TOKEN]
        else:
            response = Utils.build_response(Constants.STATUS_UNAUTHORIZED, validation_response[Constants.MESSAGE])
        return Response(response)


    def get(self, request):
        """
            Fetch Movie Records

            REQUEST_PARAMETERS:
            ------
            
            "email":"admin@gmail.com",
            "password":"admin",
            "title": "avengers"

            RESPONSE:
            ------
            {
                "status": 200,
                "result": "Success fetching movie details",
                "record": [
                    {
                        "title": "The Avengers",
                        "description": "Nick Fury is compelled to launch the Avengers Initiative when Loki poses a threat to planet Earth. His squad of superheroes put their minds together to accomplish the task",
                        "rating": 4.5,
                        "year": 2012
                    },
                    {
                        "title": "Avengers: Age of Ultron",
                        "description": "DescriptionTony Stark builds an artificial intelligence system named Ultron with the help of Bruce Banner.",
                        "rating": 4.6,
                        "year": 2015
                    },
                    {
                        "title": "Avengers: Infinity War",
                        "description": "The Avengers must stop Thanos, a mad Titan, and his army from getting their hands on all the infinity stones. ",
                        "rating": 4.6,
                        "year": 2018
                    },
                    {
                        "title": "Avengers: Endgame",
                        "description": "After Thanos, an intergalactic warlord, disintegrates half of the universe, the Avengers must reunite and assemble again to reinvigorate their trounced allies and restore balance.",
                        "rating": 4.7,
                        "year": 2019
                    }
                ],
                "token": "sample_token"
            }
        """
        response = {}
        
        # Validate Response
        validation_response = AuthorizeUser.validate_user(request.query_params)
        if validation_response[Constants.MESSAGE] == Constants.CREDENTIALS_VALID:
            title = request.query_params.get(Constants.MOVIE_TITLE, None)
            
            # Fetch Movie Details
            response = MovieHandler.get_movies(title)
        
            # Return Token
            if validation_response.get(Constants.TOKEN, None):
                response[Constants.TOKEN] = validation_response[Constants.TOKEN]
        else:
            response = Utils.build_response(Constants.STATUS_UNAUTHORIZED, validation_response[Constants.MESSAGE])
        return Response(response)

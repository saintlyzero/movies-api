import datetime as d

from rest_framework import serializers
from ..models import Movies
from ..utils.constants import Constants

class AddMovieSerializer(serializers.ModelSerializer):
    """
        Serializer to validate every field of Movies Model
    """
    class Meta:
        model = Movies
        fields =("__all__")



class UpdateMovieSerializer():
    """
        Classs to validate movie data while 
        updating movie record
    """

    @staticmethod
    def validate(data):
        """
            Movie data validation wrapper

            parameters:
            ------

            data : new movie data
        """
        response = {}
        if data:
            # Finc movie_id to be updated
            if data.get(Constants.MOVIE_ID, None):

                # movie data validation
                errors = UpdateMovieSerializer.validate_data(data)

                # If errors present
                if errors:

                    # generate error messages corresponding to the error
                    errors = UpdateMovieSerializer.generate_error_message(errors)
                    response[Constants.MESSAGE] = Constants.DATA_INVALID
                    response[Constants.ERROR] = errors
                
                # If errros not present
                else:
                    response[Constants.MESSAGE] = Constants.DATA_VALID
            else:
                response[Constants.MESSAGE] = Constants.MISSING_MOVIE_ID
        else:
            response[Constants.MESSAGE] = Constants.PARAMETERS_MISSING
        return response
    


    @staticmethod
    def validate_data(data):
        """
            Actual data validator

            parameters:
            -------

            data : new movie data
        """

        def field_validator(key, value):
            """
                Closure function acting as a switch-case
                Validates specified field of the movie data

                Validations:

                0    <= rating           <= 5
                1980 <= year             <= current_year
                1    <= len(title)       <= 100
                1    <= len(decription)  <= 200

            """
            return {
                'rating': lambda : True if float(value) >= Constants.RATING_MIN_VALUE and float(value) <= Constants.RATING_MAX_VALUE else False,
                'year': lambda : True if int(value) >= Constants.YEAR_MIN_VALUE and int(value) <= Constants.YEAR_MAX_VALUE else False,
                'title': lambda : False if len(value) > Constants.TITLE_MAX_LENGTH or len(value) < Constants.TITLE_MIN_LENGTH else True,
                'description': lambda : False if len(value) > Constants.DESC_MAX_LENGTH or len(value) < Constants.TITLE_MIN_LENGTH else True
            }.get(key, lambda : False)()

        errors = []
        for key, value in data.items():
            try:
                if key == Constants.MOVIE_ID:
                    continue
                if not field_validator(key, value):
                    errors.append({key:value})
            except Exception as e:
                errors.append({key:value})
        return errors

    
    @staticmethod
    def generate_error_message(errors):
        """
            Maps errors with the corresponding error messages

            parameters:
            -------

            errors : keys containing errors
        """

        def map_error(key):
            """
                Closure function to map error messages

            """
            return {
                'rating': lambda : Constants.RATING_ERROR,
                'year': lambda : Constants.YEAR_ERROR,
                'title': lambda : Constants.TITLE_ERROR,
                'description': lambda: Constants.DESCRIPTION_ERROR
            }.get(key, lambda : Constants.INVALID_KEY)()
        error_messages = []
        for error in errors:
            for key in error:
                error_message = {
                    key: error[key],
                    Constants.MESSAGE : map_error(key)
                }
                error_messages.append(error_message)
        return error_messages


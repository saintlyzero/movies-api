from ..utils.constants import Constants
from ..utils.utils import Utils
from ..serializers.serilizers import AddMovieSerializer
from ..models import Movies

class MovieHandler:

    """
        Class to manage all movie activities 
    """
    
    @staticmethod
    def add_movie(data):
        """
            Adds a new movie record

            parameters:
            -------

            data : {
                        "title":"Golmal 4",
                        "description":" testing 1234.",
                        "rating":4.7,
                        "year":2019
                    }
        """
        response = {}

        # validate input movie data
        movie_details = AddMovieSerializer(data = data)
        if movie_details.is_valid():

            # Add new movie record
            movie = Movies(**data)
            movie.save()
            response = Utils.build_response(Constants.STATUS_OK, Constants.RECORD_NEW, record={
                Constants.MOVIE_TITLE: movie.title,
                Constants.MOVIE_ID: movie.id})
        else:
            response = Utils.build_response(Constants.STATUS_BAD_REQUEST, movie_details.errors)
        return response



    @staticmethod
    def delete_movie(movie_id):

        """
            Deletes movie record

            parameters:
            -------

            movie_id : 12
        """
        response = {}
        try:
            # check if movie exisits
            movie = Movies.objects.get(id=movie_id)
            movie_title = movie.title

            # delete movie record
            movie.delete()
            response = Utils.build_response(Constants.STATUS_OK, Constants.RECORD_DELETED, record={
                Constants.MOVIE_TITLE: movie_title,
                Constants.MOVIE_ID: movie_id})
        except Exception as e:
            response = Utils.build_response(Constants.STATUS_OK, Constants.RECORD_NOT_EXISTS)
        finally:
            return response

    @staticmethod
    def update_movie(new_movie_data):
        """
            Updates movie record

            parameters:
            -------

            new_movie_data : {
                                "id":18,
                                <title>: "New title"
                                <description>:"New Description",
                                <rating>: 3.6,
                                <year>: 2019
                            }
        """
        response = {}
        movie_id = new_movie_data.pop(Constants.MOVIE_ID)
        try:
            # Fetch movie record
            movie = Movies.objects.filter(id=movie_id)
            if movie.exists():

                # Update movie record
                movie.update(**new_movie_data)
                response = Utils.build_response(
                    Constants.STATUS_OK,
                    Constants.RECORD_UPDATED,
                    record={
                        Constants.MOVIE_ID: movie_id,
                        **new_movie_data})
            else:
                response = Utils.build_response(Constants.STATUS_OK, Constants.RECORD_NOT_EXISTS)
        except Exception as e:
            print('** Exception: ',e)
            response = Utils.build_response(Constants.STATUS_BAD_REQUEST, Constants.RECORD_UPDATE_FAIL)
        finally:
            return response


    @staticmethod
    def get_movies(title):
        """
            Fetches movie records

            parameters:
            -------

            title : "avengers"
        """
        response = {}
        movies = []
        if title: 

            # Find movies WHERE title matches pattern with the input title
            matching_movies = Movies.objects.filter(title__icontains=title)
            for movie_obj in matching_movies:
                movie = {
                    Constants.MOVIE_TITLE: movie_obj.title,
                    Constants.MOVIE_DESCRIPTION: movie_obj.description,
                    Constants.MOVIE_RATING: movie_obj.rating,
                    Constants.MOVIE_YEAR: movie_obj.year,
                }
                movies.append(movie)
            
            # Movies present
            if movies:
                response = Utils.build_response(Constants.STATUS_OK, Constants.MOVIE_DETAILS_SUCCESS, record=movies)
            
            # Movies not present
            else:
                response = Utils.build_response(Constants.STATUS_OK, Constants.EMPTY_RESULTSET)
        else:
            response = Utils.build_response(Constants.STATUS_BAD_REQUEST, Constants.PARAMETERS_MISSING)
        return response





from .constants import Constants

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

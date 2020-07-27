from flask import jsonify


class ApiResponseBuilder(object):

    @staticmethod
    def error(message, status_code):
        response = jsonify(message=message)
        response.status_code = status_code
        return response

    @staticmethod
    def success(message, result, status_code=200):
        response = jsonify(message=message, result=result)
        response.status_code = status_code
        return response

from flask import jsonify


class ApiResponseBuilder(object):

    def error(status_code, message):
        response = jsonify(status=status_code, message=message)
        response.status_code = status_code
        return response

    def success(status_code, message, result):
        response = jsonify(message=message, result=result, status=status_code)
        response.status_code = 201
        return response

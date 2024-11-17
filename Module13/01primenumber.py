from flask import Flask, request, Response
import json
from setuptools.unicode_utils import try_encode

app = Flask(__name__)
@app.route('/primenumber/<number>')
def primenumber(number):
    try:
        number = int(number)
        is_prime = True
        if number <= 0:
            is_prime = False
        else:
            for divider in range(2, number):
                if number % divider == 0:
                    is_prime = False
                    break
        status_code = 200
        response = {
                "Number": number,
                "isPrime": is_prime
        }
    except ValueError:
        status_code = 400
        response = {
            "status": status_code,
            "message": "Number must be an integer."
        }
    json_response = json.dumps(response)
    return Response(response = json_response, status = status_code, mimetype = 'application/json')

@app.errorhandler(400)
def page_not_found(error_code):
    response = {
        "status": 404,
        "message": "Bad Request"
    }
    json_response = json.dumps(response)
    return Response(response=json_response, status=error_code, mimetype='application/json')


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

# http://127.0.0.1:3000/alkuluku/31
# {"Number":31, "isPrime":true}
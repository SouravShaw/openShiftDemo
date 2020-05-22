
from flask import Flask, request, Response
from flask_cors import CORS
#from controller import *
import os, json, sys, logging



# ENV = os.getenv("ENV")
# if(ENV == None):
#     print("no ENV value given.. program terminated")
#     sys.exit(1)


# with open('config.json') as configfile :
#     urls = json.load(configfile)

# platform=urls[ENV]["SERVICENOW_PLATFORM"]
# servicenow_urls=urls[ENV][platform]
# import Logger and call the crate method
# Creates a logger singleton which will be called in the other script files
#logger = logging.getLogger("test_logger")
#logger.setLevel(logger.debug)

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def helloWorld():
    #logger.debug("test log")
    res = Response('{"message":"Hello World from MIB wrapper"}', 200, mimetype='application/json')
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.route('/test', methods=['GET'])
def testdata():
    #res = Response( 'Hello World from MIB wrapper', 200, mimetype='application/json')
    #res.headers['Access-Control-Allow-Origin'] = '*'
    #return res 
    err='error occured'
    return Response('{"ErrorMessage":"'+ str(err) +'"}', 500, mimetype='application/json')

# @app.route('/request', methods=['POST'])
# def route_request_item():
#     request_data=request.get_json()
#     res = create_request_item(request_data,servicenow_urls)
#     return res


# @app.route('/task', methods=['POST'])
# def route_task():
#     request_data=request.get_json()
#     res = create_task(request_data,servicenow_urls)
#     return res


if __name__ == '__main__':
#    pass

    # if(ENV == "LOCAL"):
    #     app.run(host='0.0.0.0', port=5000, debug=True) 
    # else:
        app.run(host='0.0.0.0', port=5000)

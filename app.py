
from flask import Flask, request, Response
from flask_cors import CORS


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
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

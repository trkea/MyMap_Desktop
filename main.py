from bottle import route, run,template,request


@route("/")
def index():
    return template('index')

if __name__ == '__main__':
	run(host='localhost', port=8080, debug=True)

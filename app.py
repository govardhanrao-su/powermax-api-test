from flask import Flask

import powermax

app = Flask(__name__)


@app.route('/')
def index():
    return """
    Hello!
    
    Available endpoints are
    - version
    - arrays
    - arrays/<array_id>
    - headroom/<array_id>
    """


@app.route('/version')
def show_ver():
    return str(powermax.get_uni_ver())


@app.route('/arrays')
def show_arrays():
    return str(powermax.list_arrays())


@app.route('/arrays/<sid>')
def show_array(sid):
    return str(powermax.get_array(sid))


@app.route('/arrays/<sid>/sgs')
def get_sgs(sid):
    return str(powermax.get_storage_groups(sid))


@app.route('/headroom/<sid>')
def show_capacity(sid):
    return str(powermax.get_headroom(sid))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)

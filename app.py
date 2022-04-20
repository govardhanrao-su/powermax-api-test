from flask import Flask

import powermax

app = Flask(__name__)


@app.route('/')
def index():
    '''index menu'''
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
    '''show version'''
    return str(powermax.get_uni_ver())


@app.route('/arrays')
def show_arrays():
    '''list storage arrays'''
    return str(powermax.list_arrays())


@app.route('/arrays/<sid>')
def show_array(sid):
    '''get detailed info of an array'''
    return str(powermax.get_array(sid))


@app.route('/arrays/<sid>/sgs')
def get_sgs(sid):
    '''get list of storage_groups'''
    return str(powermax.get_storage_groups(sid))


@app.route('/headroom/<sid>')
def show_capacity(sid):
    '''get free space from the given array'''
    return str(powermax.get_headroom(sid))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)

import json

import PyU4V

PyU4V.univmax_conn.file_path = 'PyU4V.conf'


# Connects to the PowerMAX storage system
def get_connection(sid=None):
    if sid:
        connection = PyU4V.U4VConn(array_id=sid)
    else:
        connection = PyU4V.U4VConn()

    return connection


# Closes the PowerMAX storage system connection
def close_connection(connection):
    pass


# get unisphere version
def get_uni_ver():
    connection = get_connection()
    result = connection.common.get_uni_version()
    connection.close_session()
    return result


# List storage arrays accessible via the unisphere IP
def list_arrays():
    connection = get_connection()
    result = connection.common.get_array_list()
    connection.close_session()
    return result


# get a storage array information
def get_array(sid):
    connection = get_connection(sid=sid)
    result = json.dumps(connection.common.get_array(array_id=sid), indent=4)
    connection.close_session()
    return result


# get headroom information from the storage array
def get_headroom(sid):
    array_info = json.loads(get_array(sid))
    if array_info.get('local', False):
        connection = get_connection()
        result = json.dumps(connection.common.get_headroom(array_id=sid), indent=4)
        connection.close_session()
        return result
    else:
        return "Symmetrix ID: {0} not managed locally".format(sid)


if __name__ == "__main__":
    print(list_arrays())
    print(get_headroom('000197902448'))

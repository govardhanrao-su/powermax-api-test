"""PowerMAX2000 storage systems"""

import json

import PyU4V

PyU4V.univmax_conn.file_path = 'PyU4V.conf'


def get_connection(sid=None):
    """# Connects to the PowerMAX storage system"""
    if sid:
        connection = PyU4V.U4VConn(array_id=sid)
    else:
        connection = PyU4V.U4VConn()

    return connection


def get_uni_ver():
    """# get unisphere version"""
    connection = get_connection()
    result = connection.common.get_uni_version()
    connection.close_session()
    return result


def list_arrays():
    """# List storage arrays accessible via the unisphere IP"""
    connection = get_connection()
    result = connection.common.get_array_list()
    connection.close_session()
    return result


def get_array(sid):
    """# get a storage array information"""
    connection = get_connection(sid=sid)
    result = json.dumps(connection.common.get_array(array_id=sid), indent=4)
    connection.close_session()
    return result


def get_headroom(sid):
    """# get headroom information from the storage array"""
    array_info = json.loads(get_array(sid))
    if array_info.get('local', False):
        connection = get_connection()
        result = json.dumps(connection.common.get_headroom(array_id=sid), indent=4)
        connection.close_session()
    else:
        result = f'Symmetrix ID: {sid} not managed locally'
    return result


def get_storage_groups(sid):
    """# get storage groups information from the storage array"""
    connection = get_connection(sid=sid)
    result = connection.provisioning.get_storage_group_list()
    connection.close_session()
    return result


if __name__ == "__main__":
    print(list_arrays())
    print(get_headroom('000197902448'))
    print(get_storage_groups('000197902448'))

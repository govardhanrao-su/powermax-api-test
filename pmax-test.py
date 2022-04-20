import PyU4V

PyU4V.univmax_conn.file_path = 'PyU4V.conf'
conn = PyU4V.U4VConn()
print(conn.common.get_uni_version())
conn.close_session()

import socket
from sqlite_wrapper import *
import json

HOST = '127.0.0.1'
PORT = 8123

#JSON SCHEMA
#request type
#arguments (rin, name)
def user_to_dict(user):
    labels = ['name','rin','good']
    return dict(zip(labels,user))


def parse_json(json_string):
    json_obj = json.loads(json_string);
    request_type = json_obj["request_type"];
    if request_type == "add_user":
        ret = add_user(json_obj["name"],json_obj["rin"])

    if request_type == "delete_user":
        ret = delete_user(json_obj["rin"])

    if request_type == "modify_privilege":
        ret = modify_privilege(json_obj["rin"], json_obj["privilege"])

    if request_type == "list_all":
        ret = list_user_privileges()
        new_obj= []
        for user in ret:
            new_obj.append(user_to_dict(user))
        return json.dumps(new_obj)

    if request_type == "list_entry":
        ret = get_user_privilege(json_obj["rin"])

        if not isinstance(ret,basestring):
            return json.dumps(user_to_dict(ret))



    if ret == None:
        return "{}"

    if isinstance(ret, basestring):
        return "{{'error': '{}' }}".format(ret)


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.listen(5)
        while(1):
            conn,addr = s.accept()
            with conn:
                print("Connection received from {}".format(addr))
                data = conn.recv(1024)
                ret = parse_json(data.decode("utf-8"))
                conn.send(ret.encode("utf-8"))

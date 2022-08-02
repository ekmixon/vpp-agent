import json


def create_interfaces_json_from_list(interfaces):
    ints_json = "".join(
        '{ "name": "' + interface + '", "bridged_virtual_interface": true },'
        if interface[:4] == 'bvi_'
        else '{ "name": "' + interface + '" },'
        for interface in interfaces
    )

    ints_json = ints_json[:-1]
    return ints_json


def remove_empty_lines(lines):
    return "".join(line for line in lines if line.strip())


def remove_keys(lines):
    return "".join(line + '\n' for line in lines if line[0] != '/')


# input - etcd dump
# output - etcd dump converted to json + key, node, name, type atributes
def convert_etcd_dump_to_json(dump):
    etcd_json = '['
    key = ''
    data = ''
    firstline = True
    for line in dump.splitlines():
        if line.strip() != '':
            if line[0] == '/':
                if not firstline:
                    etcd_json += '{"key":"'+key+'","node":"'+node+'","name":"'+name+'","type":"'+type+'","data":'+data+'},'
                key = line
                node = key.split('/')[2]
                name = key.split('/')[-1]
                type = key.split('/')[4]
                data = ''
                firstline = False
            else:
                if line == "null":
                    line = '{"error":"null"}'
                data += line
    if not firstline:
        etcd_json += '{"key":"'+key+'","node":"'+node+'","name":"'+name+'","type":"'+type+'","data":'+data+'}'
    etcd_json += ']'
    return etcd_json

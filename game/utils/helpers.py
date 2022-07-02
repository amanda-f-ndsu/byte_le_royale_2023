import json


def write_json_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


def cast(parent, child):
    for name, value in vars(parent).items():
        # print "setting child", name, ": ", value, "parent", name
        setattr(parent, name, value)

    return child

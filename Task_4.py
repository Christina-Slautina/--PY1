import json

INPUT_FILE = "input_1.csv"


def csv_to_list_dict(csv_file, delimiter=',', linefeed='\n') -> list[dict]:
    list_dict = []
    with open(csv_file) as f:
        header = f.readline()  # first line
        headers_list = header.replace(linefeed, "").split(delimiter)
        for line in f:
            list_dict.append(dict(zip(headers_list, line.replace(linefeed, "").split(delimiter))))
    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

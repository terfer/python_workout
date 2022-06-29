def passwd_to_dict(file_name: str) -> dict:
    dict_file = {}
    with open(file_name, 'r') as file:
        for i in file.readlines():
            if not i.startswith('#'):
                dict_file[i.strip().split(':')[0]] = i.strip().split(':')[3]
    return dict_file


print(passwd_to_dict("passwd.txt"))
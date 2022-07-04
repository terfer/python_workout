def reverse_lines(file_name: str):
    with open(file_name, 'r') as r_file:
        with open('output_file_24', 'w') as w_file:
            content = r_file.read().strip().split('\n')
            for i,j in enumerate(content):
                w_file.write(j[::-1])
                if i < (len(content) - 1):
                    w_file.write('\n')

reverse_lines('file_24')
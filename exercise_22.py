from csv import writer, reader


class passwd_to_csv:
    def __init__(self, file_input: str, file_output: str):
        self.file_input = file_input
        self.file_output = file_output
        self.file_content_in_rows = self.read_file()
        self.write_file()

    def read_file(self):
        file_content_in_rows = []
        with open(self.file_input, 'r') as r_file:
            content = reader(r_file, delimiter=':')
            for i in content:
                if not "".join(i).startswith('#'):
                    file_content_in_rows.append([i[0], i[2]])
        return file_content_in_rows

    def write_file(self):
        with open(self.file_output, 'w', newline='\n') as w_file:
            writer_f = writer(w_file, delimiter='\t')
            for i in self.file_content_in_rows:
                writer_f.writerow(i)


passwd_to_csv("exercise_22.csv", "output.csv")

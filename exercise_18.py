def get_final_line(filename: str) -> str:
    with open(filename, 'r') as f:
        return f.read()[-1]

print(get_final_line("exercise_18_file"))
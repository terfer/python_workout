PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

def format_sort_records(people_list: list) -> str:
    list_strings = []
    template = '{1:10} {0:10} {2:5.2f}'
    for i in people_list:
        list_strings.append(template.format(*i))
    list_strings = sorted(list_strings)
    for i in list_strings:
        print(i)

format_sort_records(PEOPLE)

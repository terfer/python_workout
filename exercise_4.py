def hex_output(hex):
    int_n = 0
    for i, j in enumerate(reversed(hex[2:])):
        if j not in 'abcdef':
            int_n += int(j) * 16**i
        else:
            if j == 'a':
                int_n += 10 * 16**i
            elif j == 'b':
                int_n += 11 * 16**i
            elif j == 'c':
                int_n += 12 * 16**i
            elif j == 'd':
                int_n += 13 * 16**i
            elif j == 'e':
                int_n += 14 * 16**i
            else:
                int_n += 15 * 16**i
    return int_n

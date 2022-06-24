MENU = {
    'sandwich': 10,
    'tea': 7
}


def restaurant(total_i):
    order = input("Order: ").strip()
    total = total_i
    if not order:
        return print(f"Your total is {total}")
    if order in MENU.keys():
        total += MENU[order]
        print(f"{order} costs {MENU[order]}, total is {total}")
        return restaurant(total)
    else:
        print(f"Sorry, we are fresh out of {order} today.")
        return restaurant(total)


restaurant(0)

def make_sandwich(*args):
    """
    Print the items in a sandwich order.

    Args:
        *args: The items the customer wants on the sandwich.
    """
    if args == ():
        print("\nAy Tony, this guy wants a sandwich with nuthin'!")
    else:
        print("\nAlright, one sandwich with:")
        for item in args:
            print(f" - {item.title()}")

make_sandwich("ham", "cheese")
make_sandwich("tuna", "onions", "olives")
make_sandwich()

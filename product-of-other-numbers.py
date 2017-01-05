# Write a function get_products_of_all_ints_except_at_index() that
# takes a list of integers and returns a list of the products.
# https://www.interviewcake.com/question/python/product-of-other-numbers

def get_products_of_all_ints_except_at_index(lst):
    """ Examples:
        >>> get_products_of_all_ints_except_at_index([1, 7, 3, 4])
        [84, 12, 28, 21]

        >>> get_products_of_all_ints_except_at_index([0, 1, 2, 3])
        [6, 0, 0, 0]

        >>> get_products_of_all_ints_except_at_index([5])
        The list needs at least two numbers.
    """

    if len(lst) <= 1:
        print("The list needs at least two numbers.")
        return

    product_list = []

    for i, item in enumerate(lst):
        temp_list = lst.copy()
        del temp_list[i]
        product = 1
        for j in temp_list:
            product = product * j
        product_list.append(product)

    print(product_list)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

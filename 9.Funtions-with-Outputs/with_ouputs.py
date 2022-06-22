def format_name(f_name, l_name):
    """"
    I can write anything
    :param f_name:
    :param l_name:
    :return:
    """
    if f_name == "" or l_name == "":
        return  "You dint provide valid names"
    return f"{f_name.title()} {l_name.title()}"


print(format_name(input("whats your first name?"), input("whats your last name?")))

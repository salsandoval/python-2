


import app

def print_app2():
    name = (__name__)
    return name



if __name__ == "__main__":
    # the following is calling code from within script
    print("I am running code from {}".format(print_app2()))

    # the following is calling code from the imported qpp.py
    print("I am running code from {}".format(app.print_app()))

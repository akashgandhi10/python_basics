# def hello():
#     return "hey Akash"
#
# def other(func):
#     print "other codes goes here!"
#     print func()
#
# other(hello)

def new_decorator(func):

    def wrap_func():
        print ("code here, execute before the func")

        func()

        print ("code here will execute after the func")

    return wrap_func

# def func_need_decorator():
#     print ("this func need a decorator")

# func_need_decorator()

# func_need_decorator = new_decorator(func_need_decorator)
#
# func_need_decorator()

@new_decorator # func_need_decorator = new_decorator(func_need_decorator)
def func_need_decorator():
    print ("this func need a decorator")

func_need_decorator()

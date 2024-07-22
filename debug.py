curr_func = 'main'

def d_set_func(func):
    global curr_func
    curr_func = func

def d_print(str):
    global curr_func
    print(f'(In {curr_func}) {str}')
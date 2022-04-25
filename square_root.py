
def square_root_update(x,a):
    return (x+a/x)/2

def improve(update,close,guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x,y,tolerance=1e-15):
    return abs(x-y) < tolerance

def square_root(a):
    return improve( lambda x:square_root_update(x,a),
                    lambda x:approx_eq(x*x,a))
# python if else one line statement for assign

from operator import sub,mul
age=20

isMan = True if age>18 else False

print(isMan)

fact = lambda n: 1 if n==1 else mul(n,fact(sub(n,1)))

# print(fact(5))



#

def make_anonymous_factorial():
    """
    1: no assignment,
    2: no def
    3: just condition assignment,lambda, call
    core function to finish
    1: how to implement recursive call  =>  f(f,v) learning to grasp the core point or abstract the most important part of the solution
    2: what is the most essential of the function: =>  f(f,v) can express the recursive logic
        2.1: at function level: function as param of function or function as the return value of the function.
        2.2 call function
        2.3 in the inner of the function: param, function body, and return value.

    fact = lambda n: 1 if n==1 else mul(n,fact(sub(n,1)))
    return lambda n: (lambda f,v: f(f,v)) (lambda f,v: 1 if v==1 else mul(v,f(f,sub(v,1))) ,n)
    """
    return lambda n: (lambda f,v: f(f,v)) (lambda ff,vv: 1 if vv==1 else mul(vv,ff(ff,sub(vv,1))) ,n)



test = make_anonymous_factorial()(5)

print(test)

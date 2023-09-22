x= int(input("Enter a number of repetitions"))
def repeats(fun):
    def wrapper():
      for i in range(x):
       fun()
    return wrapper
@repeats
def hello():
    print('hello')
hello()


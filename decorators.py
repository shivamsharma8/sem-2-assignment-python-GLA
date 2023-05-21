def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("thanks for using the function")
    return mfx

@greet
def hello():
    print("hey everyone")

hello()
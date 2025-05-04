class Logger:
    def __init__(self):
        print("Logger started")

    def __del__(self):
        print("Logger ended")

Log = Logger()
del Log
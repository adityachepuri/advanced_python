from threading import *
print(current_thread().getName)
print(current_thread().isDaemon())
current_thread().setDaemon(True)
print(current_thread().idaemon)

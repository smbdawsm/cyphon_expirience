import os

try:
        import win.module    
except (ImportError, NameError):
    if os.name == 'darwin':
        pass
    elif os.name == 'posix':
        import module
        print("yep")

  
print(module.cherta())
print(module.my_func())
print(module.cherta())

import os
import sys

try:
    if sys.argv[1] == 'compiled':
        print('This is compiled module')
        import c.module as mod
        
    elif sys.argv[1] == 'source':
        print('This is source code')
        #print(os.path.realpath(os.curdir))
        import py.module as mod       

except IndexError:

        try:
            import win.module as mod   
        except (ImportError):
            if os.name == 'darwin':
                pass
            elif os.name == 'posix':
                try:
                    import c.module as mod
                    print("compiled module")
                except ImportError:
                    import py.module as mod
                    print('source code')

print(mod.cherta())
print(mod.my_func())
print(mod.cherta())

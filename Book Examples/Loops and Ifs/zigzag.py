# Prints a zig-zag
import sys, time
indent = 0 # how many spaces to indent
indentIncreasing = True

#try:
while True: # Main program loop
    print(' ' * indent, end="")
    print('********')
    time.sleep(0.1)
        
    if indentIncreasing:
        indent = indent + 1
        if indent == 20:
            indentIncreasing = False
        
    else:
         indent = indent - 1
         if indent == 0:
             indentIncreasing = True
    
#except KeyboardInterrupt:
#    sys.exit()

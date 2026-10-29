
import gc

class Demo:
    def __init__(self, name):
        self.name = name
        self.ref = None

# Check whether garbage collection is enabled
print("Garbage collection enabled:", gc.isenabled())

# Create circular references
a = Demo("Object A")
b = Demo("Object B")

a.ref = b
b.ref = a

print("Objects created with circular references")

# Remove external references
del a
del b

# Check garbage collector statistics
print("Garbage collection counts:", gc.get_count())

# Perform manual garbage collection
collected = gc.collect()

print("Unreachable objects collected:", collected)

# Disable automatic garbage collection temporarily
gc.disable()
print("Automatic garbage collection disabled:", not gc.isenabled())

# Enable automatic garbage collection again
gc.enable()
print("Automatic garbage collection enabled:", gc.isenabled())

import argparse

# https://stackoverflow.com/questions/16712795/pass-arguments-from-cmd-to-python-script
# Define the parser
parser = argparse.ArgumentParser(description='Short sample app')

# Declare an argument (`--algo`), saying that the 
# corresponding value should be stored in the `algo` 
# field, and using a default value if the argument 
# isn't given
parser.add_argument('--keys', action="store", dest='keys', default="no keys")

# Now, parse the command line arguments and store the 
# values in the `args` variable
args = parser.parse_args()

# Individual arguments can be accessed as attributes...
# print args.algo
# raise ValueError(args.keys + ': Exiting program.')

print("reloading listen.py")
# destroy current process
# start new process of listen.py
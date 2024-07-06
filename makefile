 python -m unittest discover # This will search the current directory for any files named test*.py and attempt to test them.
 python -m unittest test

"""
Once you have multiple test files, as long as you follow the test*.py naming pattern,
you can provide the name of the directory instead by using the -s flag and the name of the directory:
"""
python -m unittest discover -s tests
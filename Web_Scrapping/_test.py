load_file_in_context("script.py")

try:
  # Attempt to access a variable identifier:
  turtles
  # Write more tests here:
  if type(turtles) != type({}):
    fail_tests("Expected `turtles` to be a dictionary!")
  
except NameError:
  fail_tests("Expected {} to be defined.".format("turtles"))

pass_tests()

#!/usr/bin/env python

list_example = [100,222,333,444,"string value"]
list_example_length = len(list_example)
for iteration in list_example:
    index_value = list_example.index(iteration)
    print("The length of list list_example is %s, the value at position %s is %s") % (str(list_example_length), str(index_value), str(iteration).
strip('[]'))

print("Script finished")

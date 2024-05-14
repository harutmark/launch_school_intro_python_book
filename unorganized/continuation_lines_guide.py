#Continuation Lines


#String literals can be continued over several lines, provided you enclose all the string content in a set of parentheses:
print("This is a long string. "
      "It's actually very long. "
      "It spans multiple lines. "
      "Are you getting tired of this? "
      "So am I.")
      
      
      
#Triple Quoting
def long_string():
    return """
        This is a long string.
        It's actually very long.
        It spans multiple lines.
        Are you getting tired of this?
        So am I.
    """
print(long_string())


#multi-value literals

my_list_nieces_nephews = [
    "Antonio",
    "Troy",
    "Emma", #python convention is to end every item w/ comma, including last item
]

my_tuple = (
    3.141592,
    2.718282,
    1.414213,
)

my_set = {
    "Dog",
    "Cat",
    "Pet",
}

print(my_list_nieces_nephews, my_tuple, my_set)


#delimit code
#def delimit_code():
#   return (obj.bar1 +
#           obj.bar2 +
#           obj.bar3)
            

#You can use a backslash to end any line you want to continue:
#result = value1 + \
#         value2 + \
#         value3

# Strip whitespaces from each string in a list
def striplist(in_list):
  return([x.strip() for x in in_list])

a_list = ["one","two   ","   three   "]
print (a_list)
print ("After strip")
print (striplist(a_list))

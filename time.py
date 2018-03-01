import time; # This is required to include time module.

ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks


def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print "Output is: "
   print "arg:",arg1
  
   for var in vartuple:
    
      print var
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )



localtime = time.localtime(time.time())
print "Local current time :", localtime
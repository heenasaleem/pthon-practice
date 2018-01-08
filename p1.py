
print("hello")
print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10)  # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end.  try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6)
print(end7 + end8 + end9 + end10 + end11 + end12)
print('#############new prog####################')



formatt = "{} {} {} {}"

print(formatt.format(1, 2, 3, 4, 5, 6, 7))
print(formatt.format("one", "two", "three", "four", "five"))
print(formatt.format(True, False, False, True))
print(formatt.format(formatt, formatt, formatt, formatt))
print(formatt.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

print("############333333333333333333333333333####################3")
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

    print "hello"


    tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]
print "tup2[1:5:2]: ", tup2[1:5:2]

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

import support;
support.print_func("heena")
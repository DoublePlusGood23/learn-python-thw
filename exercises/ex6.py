x = "There are %d types of people." % 10 # Declares the variable x with as string that also calls to '10'
binary = "binary" # Declares the variable to have a string
do_not = "don't" # do_not equals the string 'don't'
y = "Those who know %s and those who %s." % (binary, do_not) # has the varible y call two seperate variables

print x # prints the x string 
print y # prints the y string 

print "I said %r." % x # calls the x string in the string 
print "I also said: '%s'." % y # same with y 

hilarious = False # boolean variable 
joke_evaluation = "Isn't that joke so funny?! %r" # calls the last set variable with %r which is type agnostic

print joke_evaluation % hilarious # since joke_evaulation is a string is can cat it with hilarious using modulous 

w = "This is the left side of..." # declares a string  
e = "a string with a right side." # declares a second string

print w , e # detects two strings and cats them together 

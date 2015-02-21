from sys import argv

script, first, second, third = argv

print "The script is called:", script
script = raw_input("What is your name? ")
print "Your first variable is:", first
first = raw_input("What is your age? ")
print "Your second variable is:", second
second = raw_input("what is your eye color? ")
print "Your third variable is:", third
third = raw_input("Where do you live? ")

print "Your name is %s. You are %s years old. Your eyes are %s, and you live in %s." % (script, first, second, third)


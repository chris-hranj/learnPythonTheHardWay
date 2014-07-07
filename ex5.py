name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

heightCm = height * 2.54 # convert inches to centimeters
weightKilo = weight * 0.453592 # convert pounds to kilograms

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "His height in centimeters would be %d." % heightCm
print "He's %d pounds heavy." % weight
print "His weight in kilograms would be %d." % weightKilo
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the cofee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)

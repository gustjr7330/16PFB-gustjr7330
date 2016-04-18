name = 'Zed A. Shaw'
age = 21 # Maybe?
height_cm = 170 # cm
cm_to_inch = 1.0 / 2.54
height_inch = height_cm * cm_to_inch
weight_kg = 61 # kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height_inch
print "He's %d pounds heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height_cm, weight_kg, age + height_cm + weight_kg)

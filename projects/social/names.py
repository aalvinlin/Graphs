import random

boys = "Michael Christopher Matthew Joshua David James Daniel Robert John Joseph Jason Justin Andrew Ryan William Brian Brandon Jonathan Nicholas Anthony Eric Adam Kevin Thomas Steven Timothy Richard Jeremy Jeffrey Kyle Benjamin Aaron Charles Mark Jacob Stephen Patrick Scott Nathan Paul Sean Travis Zachary Dustin Gregory Kenneth Jose Tyler Jesse Alexander".split(" ")
girls = "Jessica Jennifer Amanda Ashley Sarah Stephanie Melissa Nicole Elizabeth Heather Tiffany Michelle Amber Megan Amy Rachel Kimberly Christina Lauren Crystal Brittany Rebecca Laura Danielle Emily Samantha Angela Erin Kelly Sara Lisa Katherine Andrea Jamie Mary Erica Courtney Kristen Shannon April Katie Lindsey Kristin Lindsay Christine Alicia Vanessa Maria Kathryn Allison".split(" ")
initials = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def create_random_name():
    
    if random.randrange(0, 2):
        name = random.choice(boys)
    else:
        name = random.choice(girls)
    
    return name + " " + random.choice(initials) + "."
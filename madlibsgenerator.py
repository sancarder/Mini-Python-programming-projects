#Mad Libs Generator


def get_input():
    adjective = raw_input("Write an adjective: ")
    subject = raw_input("Write a singular noun: ")
    verb = raw_input("Write a verb in third person: ")
    adverb = raw_input("Write an adverb: ")    
    theobject = raw_input("Write another singular noun: ")
    place = raw_input("Write a place: ")

    return adjective, subject, verb, adverb, theobject, place

def generate_story(adjective, subject, verb, adverb, theobject, place):

    story = get_article(subject).capitalize() + ' ' + adjective + ' ' + subject + ' ' + adverb + ' ' + verb + ' ' + get_article(theobject) + ' ' + theobject + ' in the ' + place

    return story

def get_article(noun):

    vowels = ['a', 'o', 'u', 'e', 'i', 'y']

    if noun[0] in vowels:
        article = 'an'
    else:
        article = 'a'

    return article


def main():

    write = 'y'
    
    print "Welcome to the Mad Libs Generator! Let's write some wacky stories!"

    while write == "y":
        write_story()
        write = raw_input("Do you want to write another story? y/n: ")

def write_story():
    adjective, subject, verb, adverb, theobject, place = get_input()
    story = generate_story(adjective, subject, verb, adverb, theobject, place)    
    print story
    

main()

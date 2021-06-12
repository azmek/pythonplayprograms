'''This is just a small program that creates a sentence of user input, checks if the sentence is a question or a statement, also ends with #end command'''

# create a function that takes a variable of the user input


def sentence_maker(phrase):
    # set the keywords in a tuple to distinguish a question or a statement
    keywords = ('how', 'what', 'when', 'why')
    # capitalise the first letter of the sentence
    capit = phrase.capitalize()
    # check if the input starts with any of the keywords
    # set either a question mark or a dot dpending on the input
    if phrase.startswith(keywords):
        return "{}?".format(capit)
    else:
        return "{}.".format(capit)


# an empty list to store our results
results = []
# A while loop is good fit here as the input continues
while True:
    user_input = input("Say something:")
    # command to end the program
    if user_input == "#end":
        break
    else:
        # if the the request is not to end the program, add the input to the list
        results.append(sentence_maker(user_input))

# join the results in a string with a space
print(" ".join(results))

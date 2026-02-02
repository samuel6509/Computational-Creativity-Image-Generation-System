# logic for breaking up the user's sentence description into tokens the system can understand

# TODO:
# 1. add more logic into the lematizer functions -- COMPLETE
# 2. add logic to test function so it mimics user_input -- COMPLETE

# uncomment the below to download nltk data needed for project ...
# import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer

#  testing that the above imports are working on my virtual enviroment
# also testing different way of word processing to get the best outcome
def test():
    # example user input
    text = "Blue sky with clear skies"
    # tokenize the input
    tokens = word_tokenize(text)
    #  remove punctuation
    tokens = [token for token in tokens if token.isalpha()]
    # converting all tokens to lower case
    tokens = [token.lower() for token in tokens]
    # tagging tokens
    tags = pos_tag(tokens)
    # lemmatizing tokens based on tags
    lemmatized_tokens = [lem_technique(token, tag) for token, tag in tags]
    # print(tags)
    print(lemmatized_tokens)
    return lemmatized_tokens

    # lemmatizing the tokens
    # lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    # adding the tag to each token
    # tags = pos_tag(lemmatized_tokens)
    # print(tags)

# function to use word processing and custom lemmatization technique on user input
def word_processing(input):
    # tokenize the input
    tokens = word_tokenize(input)
    #  remove punctuation
    tokens = [token for token in tokens if token.isalpha()]
    # all tokens to lowercase
    tokens = [token.lower() for token in tokens]
    # tagging the tokens
    token_tags = pos_tag(tokens)
    # lemmatize tokens based on the tags
    lemmatized_tokens = [lem_technique(token, tag) for token, tag in token_tags]

    print(lemmatized_tokens)
    return lemmatized_tokens

# function to test a lemmatization technique
def lem_technique(token, tag):
    # starting the lemmatizer
    lemmatizer = WordNetLemmatizer()
    #  lemmatizing token based on tag
    if tag.startswith('V'): # verb
        return lemmatizer.lemmatize(token, pos='v')
    elif tag.startswith('N'): # noun
        return lemmatizer.lemmatize(token, pos='n')
    elif tag.startswith('J'): # adjective
        return lemmatizer.lemmatize(token, pos='a')
    else:
        #  no tag worth lemmatizing
        return token

#  function to allow a user to input their sentence
def user_input():
    user_input = input('Please enter your setence description: ')
    # print('your input: ' + user_input)
    # make sure there is a user input
    while not user_input:
        user_input = input('Please enter your setence description: ')
    return word_processing(user_input)

# test()
# user_input()
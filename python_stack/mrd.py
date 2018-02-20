def print_dictionary_values(dic):
    for some_key, some_value in dic.iteritems():
        print "My" + " " + some_key + " " + "is" + " " + str(some_value)

print print_dictionary_values({
        "name": "Tom",
        "age": 30,
        "country of birth": "USA",
        "favorite language": "English"
    }
)

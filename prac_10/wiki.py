import wikipedia

def search_page(search_title):
    wikipedia.search(search_title)
    wikipedia.suggest(search_title)
    wikipedia.summary(search_title)
    wikipedia.title(search_title)
    wikipedia.url(search_title)

    try:
        search_title = wikipedia.summary(search_title)
    except wikipedia.exceptions.DisambiguationError as e:
        print e.options

title = input("Enter title of page: ")
while title != "":
    print(search_page(title))
    title = input("Enter title of page: ")
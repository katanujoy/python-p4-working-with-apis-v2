import requests
import json

class Search:
    def get_search_results(self):
        search_term = "the lord of the rings"
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
        response = requests.get(URL)
        return response.content

    def get_search_results_json(self):
        search_term = "the lord of the rings"
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
        response = requests.get(URL)
        return response.json()

    def get_user_search_results(self, search_term):
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
        response = requests.get(URL).json()
        
        # Handle cases where no results are found
        if not response['docs']:
            return "No results found"
            
        book = response['docs'][0]
        title = book.get('title', 'Unknown Title')
        author = book.get('author_name', ['Unknown Author'])[0]
        
        return f"Title: {title}\nAuthor: {author}"

# Uncomment to test different methods
# print(Search().get_search_results())
# print(json.dumps(Search().get_search_results_json(), indent=2))

# Interactive search
if __name__ == "__main__":
    search_term = input("Enter a book title: ")
    result = Search().get_user_search_results(search_term)
    print("\nSearch Result:")
    print(result)
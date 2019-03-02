
import urllib.request,json
from .models import Quote
 
base_url = None

def configure_request(app):
    global base_url   
    base_url = app.config['QUOTE_API_BASE_URL']

def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url.format()

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes_results = None

        if get_quotes_response['results']:
            quote_results_list = get_quotes_response['results']
            quote_results = process_results(quotes_results_list)


    return quotes_results

def process_results(quote_list):
    '''
    Function  that processes the quote result and transform them to a list of Objects

#     Args:
#         quote_list: A list of dictionaries that contain quote details

#     Returns :
#         quote_results: A list of quote objects
#     '''
    quote_results = []
    for quote_item in quote_list:

            author= onequote_response.get('author')
            id = onequote_response.get('id')
            quote = onequote_response.get('quote') 
      
            if author:
                quote_object = Quote(author,id.quote)
                quote_results.append(quote_object)

    return quote_results



def get_onequote(id):
    get_quotes_url = base_url.format(id)

with urllib.request.urlopen(get_quotes_url) as url:
        onequote = url.read()
        onequote_response = json.loads(onequote_data)

        quote_object = None
        if onequote_response:
            author= onequote_response.get('author')
            id = onequote_response.get('id')
            quote = onequote_response.get('quote')        

            quote_object = Quote(author,id,quote)

    return quote_object

# def search_movie(movie_name):
#     search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
#     with urllib.request.urlopen(search_movie_url) as url:
#         search_movie_data = url.read()
#         search_movie_response = json.loads(search_movie_data)

#         search_movie_results = None

#         if search_movie_response['results']:
#             search_movie_list = search_movie_response['results']
#             search_movie_results = process_results(search_movie_list)


#     return search_movie_results

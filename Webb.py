# Importing the 'web' module from the 'aiohttp' library. 
# 'aiohttp' is an asynchronous HTTP client/server framework in Python.
from aiohttp import web

# Defining an asynchronous request handler function 'handle'.
# This function will be executed whenever a GET request is made to the server.
# It takes 'request' as an argument, which contains the details of the HTTP request.
async def handle(request):
    # Extracting a 'name' parameter from the URL path using 'request.match_info.get'.
    # If no name is provided in the URL, it defaults to "Anonymous".
    name = request.match_info.get('name', "Anonymous")
    
    # Formatting the response text with the extracted 'name'.
    text = f"Hello, {name}"
    
    # Returning an HTTP response with the 'text' as the body of the response.
    return web.Response(text=text)

# Creating a new web application instance using aiohttp's web.Application().
app = web.Application()

# Adding routes to the application. The add_routes() function registers URL patterns.
# The first route is for the root URL ('/'), which will trigger the 'handle' function.
# The second route matches URLs with a variable name (e.g., '/John'), 
# which will also trigger the 'handle' function and greet the user by name.
app.add_routes([
    web.get('/', handle),  # Route for root URL
    web.get('/{name}', handle)  # Route with a 'name' parameter in the URL
])

# If the script is run directly (not imported as a module), this block will execute.
# It starts the web application by calling 'web.run_app()' and passing the 'app' instance.
if __name__ == '__main__':
    web.run_app(app)  # Running the application

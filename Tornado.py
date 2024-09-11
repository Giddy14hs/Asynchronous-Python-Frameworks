# Importing necessary modules from the Tornado framework.
# tornado.ioloop: Manages the I/O event loop that Tornado uses to handle requests asynchronously.
# tornado.web: Provides the web server capabilities like handling requests and responses.
import tornado.ioloop 
import tornado.web

# Defining a request handler class called 'MainHandler' that will process GET requests.
# The class inherits from tornado.web.RequestHandler, which provides methods for HTTP requests like GET, POST, etc.
class MainHandler(tornado.web.RequestHandler):  # Corrected to tornado.web.RequestHandler
    # The 'get' method is executed whenever a GET request is received at the corresponding route.
    def get(self):
        # Sends "Hello, World" as a response to the client when the root URL ("/") is accessed.
        self.write("Hello, World")

# Defining a function 'make_app' that creates and returns a Tornado web application instance.
# This application will map URL patterns to specific request handlers.
def make_app():
    return tornado.web.Application([
        # This route maps the root URL ("/") to the MainHandler, which handles requests to "/".
        (r"/", MainHandler),
    ])

# The main block ensures the application starts when the script is run directly.
if __name__ == "__main__":
    # Creating an application instance by calling the make_app() function.
    app = make_app()

    # Binding the application to port 8888, so it listens for HTTP requests on that port.
    app.listen(8888)

    # Starting the I/O loop, which will keep the server running and handle requests asynchronously.
    tornado.ioloop.IOLoop.current().start()

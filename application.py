def wsgi_app(environ, start_response):
    import sys
    output = str(sys.version)
    status = '200 OK'
    headers = [('Content-type', 'text/plain'),
               ('Content-Length', str(len(output)))]
    start_response(status, headers)
    yield output

application = wsgi_app
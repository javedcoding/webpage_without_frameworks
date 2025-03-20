#only used gunicorn for rendering operation no frameworks
def render_template(template_name="index.html", context={}):
    html_str = ""
    with open(template_name, 'r') as f: #here is the html files are read default is the index.html
        html_str = f.read()
        html_str = html_str.format(**context)
    return html_str

#this is the function to read Home Page html from the html file
def home(environ):
        data = render_template(template_name='index.html', context={})
        return data  

#this is the function to read Contact Page html from the html file
def contact_us(environ):
        data = render_template(template_name='contact.html', context={})
        return data  

#this is the main function called by the gunicorn as filename:app
def app(environ, start_response):
    path = environ.get("PATH_INFO") #this can be read from the request of browser

    #below portion determines what to do with which paths
    if path == "/":
        data = home(environ)
    elif path == "/contact":
        data = contact_us(environ)
    else:
        data = render_template(template_name='404.html', context={"path": path})
    data = data.encode("utf-8") #this is important for the decoding of data
    start_response(
        f"200, OK", [
            ("Content-Type", "text/html"), #this defines the content type can be plain html yaml jt etc.
            ("Content-Length", str(len(data))) #when its 200 this meta data will be given to browser
        ]
    ) #make the http responses here
    return iter([data])
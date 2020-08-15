class HtmlManager:

    def create_html(self):
        f = open('yourname.html','w')
        message = """<html>
        <head>Welp </head>
        <h1> Python</h1>
        <body><p>YEERRRRR</p>
        </body>
        </html>"""

        f.write(message)
        f.close()
    
    create_html()
class HtmlManager:
    def __init__(self):
        self.document = None
    def create_html(self):
        
        message = """<html>
        <head>YERRRRRRR</head>
        <h1>I hope this works </h1>
        <body><p>Howdy. ..</p>
        <p> Okay bye. </p>
        </body>
        </html>"""
        new_doc = HTMLDocument(message)
        self.document = new_doc
        print(new_doc)
    
    def save(self):
        f = open('yourname.html','w')
        f.write(self.document.information)
        f.close()
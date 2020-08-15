class HtmlDocument:
    def __init__(self,information):
        self.information = information

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
    
   

class AWSManager:
    pass
#s3 = boto3.client('s3')
  #define connections to boto3 and save file to s3
   # def save_to_s3():   
    #    boto3.client('s3').upload_file('helloworld.html', 'lmtd-class', 'heyclass.html')

    manager = HtmlManager()
    manager.create_html()
    manager.save_html_file()
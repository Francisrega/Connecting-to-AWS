import boto3

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
        
        new_doc = HtmlDocument(message)
        self.document = new_doc
    
    def save(self):
        f = open('Francis.html','w')
        f.write(self.document.information)
        f.close()
       

class AWSManager:
    def __init__(self):
        self.s3 = boto3.resource('s3')
  #define connections to boto3 and save file to s3
    def save_to_s3(self): 
        
        s3_client = boto3.client('s3')
        boto3.client('s3').upload_file('Francis.html', 'lmtd-class', 'Francis.html')

    def listBucketFile(self, bucketName):
        bucket = self.s3.Bucket(bucketName)
        files = bucket.objects.all()
        for file in files:
            print(file.key)

manager = HtmlManager()
manager.create_html()
manager.save()

aws = AWSManager()
aws.save_to_s3()
aws.listBucketFile("lmtd-class")
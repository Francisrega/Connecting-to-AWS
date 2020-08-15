import boto3
class AWSManager:
    pass
#s3 = boto3.client('s3')
  #define connections to boto3 and save file to s3
   # def save_to_s3():   
    #    boto3.client('s3').upload_file('helloworld.html', 'lmtd-class', 'heyclass.html')

    manager = HtmlManager()
    manager.create_html()
    manager.save()
import re
from unsec import Tools
from email import message_from_file
from email.header import decode_header, make_header 

class Email(object):
    def __init__(self, filename):
        file                = open(filename, "r")
        self.message        = message_from_file(file)


    def subject(self):
        ''' return raw subject ''' 
        return str(make_header(decode_header(self.message.get("Subject"))))

    def body(self):
        ''' return raw body ''' 
        return self.message.get_payload()

    def sender(self):
        ''' return raw sender '''
        return str(self.message.get("From"))

    def clean_body(self):
        ''' return clean body ''' 
        return Tools.clean(self.body())

    def clean_subject(self):
        ''' return clean subject ''' 
        return Tools.clean(self.subject())







    def __str__(self):
        return "mail de " + self.sender

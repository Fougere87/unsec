import re
from unsec import Tools
from email import message_from_file, message_from_bytes
from email.header import decode_header, make_header 
from langdetect import detect


class Email(object):
    def __init__(self, filename):
        file = open(filename, "r")
        self.message = message_from_bytes(open(filename, "rb").read())
        self.charset = self.message.get_charsets()

    def lang(self):
        return detect(self.body())


    def subject(self):
        ''' return raw subject ''' 
        sbj = self.message.get("Subject")
        if sbj is not None: 
            return str(make_header(decode_header(self.message.get("Subject"))))
        else: 
            return None

    def body(self):
        ''' return raw body ''' 
        result = self.message.get_payload()
        #remove empty line 
        result = result.replace('\n',' ')
        return result

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

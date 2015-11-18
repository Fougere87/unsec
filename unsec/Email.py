# coding: utf8
import re
from email import message_from_binary_file
from email.header import decode_header, make_header
from langdetect import detect



class Email(object):
    def __init__(self, filename):
        with open(filename, "rb") as file:
            self.filename  = filename
            self.message   = message_from_binary_file(file)
            self.charset   = self.message.get_charsets()[0]


    def get_subject(self):
        ''' return raw subject '''
        return str(make_header(decode_header(self.message.get("Subject"))))


    def get_body(self):
        ''' return raw body '''
        result = self.message.get_payload(decode=True).decode(self.charset)
        return result

    def get_sender(self):
        ''' return raw sender '''
        return str(self.message.get("From"))

    def get_lang(self):
        lang   = detect(self.get_body())
        return lang



    def __str__(self):
        return self.sender

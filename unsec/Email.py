# coding: utf8
import re
from unsec import Tools
from email import message_from_file, message_from_bytes, message_from_string,message_from_binary_file
from email.header import decode_header, make_header
from langdetect import detect
import base64
import chardet


class Email(object):
    def __init__(self, filename):
        file = open(filename, "r")
        self.message = message_from_binary_file(open(filename, "rb"))
        self.charset = self.message.get_charsets()[0]

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
        result = self.message.get_payload(decode=True)
        #print(result.decode(self.charset))
        print(result.decode(self.charset, "replace") )
        return ""
        #remove empty line
        result = result.replace('\n',' ')

        # if self.message.get("Content-Transfer-Encoding") == "base64":
        #     print("LALALALALA  ##### ")
        #     result = base64.decodestring(result)



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
        return self.sender

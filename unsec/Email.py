import re
from unsec import Tools
from email import message_from_file
from email.header import decode_header, make_header 

class Email(object):
    def __init__(self, filename):
        file                = open(filename, "r")
        self.message        = message_from_file(file)
        self.subject        = str(make_header(decode_header(self.message.get("Subject"))))
        self.body           = self.message.get_payload()
        # self.sender       = Email.extract_sender(raw)
        # self.clean_subject = Tools.clean(self.subject)
        self.clean_body      = Tools.clean(self.body)
        self.clean_subject   = Tools.clean(self.subject)






#====================================================================
    # @staticmethod
    # def extract_subject(raw):
    #     ''' extract subject '''
    #     match = re.search(r"Subject:\s(?P<subject>.+)", raw)
    #     return match.group("subject")
#====================================================================
    # @staticmethod
    # def extract_body(raw):
    #     ''' extract body '''
    #     subj = re.split("Subject:\s.+", raw)
    #     line = subj[1]
    #     return line
#====================================================================
    # @staticmethod
    # def extract_sender(raw):
    #     ''' extract email with a regexp '''
    #     return "truc@tete.fr"
    #     # try:
    #     #     match = re.search(r"From:.*(?P<email>.+@)\s", raw)
    #     #     return match.group("email")
    #     # except:
    #     #     return None

#====================================================================
    def __str__(self):
        return "mail de " + self.sender

import re


class Email(object):
    def __init__(self, filename):
        file = open(filename, "r")
        raw = "".join(file.readlines())

        self.subject = Email.extract_subject(raw)
        self.body    = Email.extract_body(raw)
        self.sender  = Email.extract_sender(raw)


    @staticmethod
    def extract_subject(raw):
        ''' extract subject '''
        return "je suis je subject"

    @staticmethod
    def extract_body(raw):
        ''' extract body '''
        return "body"

    @staticmethod
    def extract_sender(raw):
        ''' extract email with a regexp '''
        line = re.findall(r'Sender: \w+@\w+\.\w{2,3}',raw)[0]
        line = line.replace("Sender: ", "")
        return line

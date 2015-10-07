import re


class Email(object):
    def __init__(self, filename):
        file = open(filename, "r")
        raw = "".join(file.readlines())
        # dec = re.match("(.*) (From:\s.+\n) (Subject:\s.+\n) (.*)", raw, re.DOTALL)
        self.subject = Email.extract_subject(raw)
        self.body    = Email.extract_body(raw)
        self.sender  = Email.extract_sender(raw)


    @staticmethod
    def extract_subject(raw):
        ''' extract subject '''
        match = re.search(r"Subject:\s(?P<subject>.+)", raw)
        return match.group("subject")

    @staticmethod
    def extract_body(raw):
        ''' extract body '''
        subj = re.split("Subject:\s.+", raw)
        line = subj[1]
        return line

    @staticmethod
    def extract_sender(raw):
        ''' extract email with a regexp '''
        match = re.search(r"From:\s\".*\"\s<(?P<email>.+@.+)>", raw)
        return match.group("email")



    def __str__(self):
        return "mail de " + self.sender

import re


class Email(object):
    def __init__(self, filename):
        file = open(filename, "r")
        raw = "".join(file.readlines())
        # dec = re.match("(.*) (From:\s.+\n) (Subject:\s.+\n) (.*)", raw, re.DOTALL)
        self.subject = Email.extract_subject(raw)
        self.body    = Email.extract_body(raw)
        self.sender  = Email.extract_sender(raw)

    def salut(self):
        print(self.nom)




    @staticmethod
    def extract_subject(raw):
        ''' extract subject '''
        # line = re.search("Subject:\s.+", raw)
        # dec = re.search("(.*) (From:\s.+\n) (Subject:\s.+\n) (.*)", raw, re.DOTALL)
        dec = re.search("(From:\s.+)(\n.*)(Subject:\s.+\n)", raw, re.DOTALL)
        return dec.group(1)

    # def extract_subject(dec):
    #     ''' extract subject '''
    #     # line = re.search("Subject:\s.+", raw)
    #     return dec.group(3)


    @staticmethod
    def extract_body(raw):
        ''' extract body '''
        subj = re.split("Subject:\s.+", raw)
        line = subj[1]
        return line

    @staticmethod
    def extract_sender(raw):
        ''' extract email with a regexp '''
        line = re.search("From:\s.+",raw)
        return line.group(0)


    def __str__(self):
        return "mail de " + self.sender

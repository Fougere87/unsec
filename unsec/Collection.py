import glob
from unsec import Email


class Collection(object):
    def __init__(self, directory):
        self.emails = list()
        for email in self.get_email(directory):
            self.emails.append(Email(email))
        self.all_subjects = Collection.get_subject(self, email)
        self.all_bodies   = Collection.get_body(self, email)
        self.all_senders  = Collection.get_sender(self, email)

    def get_email(self, directory):
        '''
        Returns the emails' paths from the dataset
        '''
        for email in glob.glob(directory+"/bioinfo_2014-0?/*"):
            if email.endswith("recoded"):
                yield email

    def get_subject(self, email):
        '''
        Returns a list containing all the emails' subjects
        '''
        return [email.subject for email in self.emails]

    def get_body(self, email):
        '''
        Returns a list containing all the emails' bodies
        '''
        return [email.body for email in self.emails]

    def get_sender(self, email):
        '''
        Returns a list containing all the emails' senders
        '''
        return [email.sender for email in self.emails]

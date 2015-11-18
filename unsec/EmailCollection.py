import glob
from unsec import Tools
from unsec import Email


class EmailCollection(object):
    def __init__(self):
        self.paths  = []


    def add_file(self, filename):
        self.paths.append(filename)

    def get_subjects(self):
        ''' return a generator of all email subjects '''
        for filename in self.paths:
            email = Email(filename)
            yield email.get_subject()


    def get_bodies(self):
        ''' return aa generator of all email bodies '''
        for filename in self.paths:
            email = Email(filename)
            yield email.get_body()


    def get_senders(self):
        ''' return aa generator of all email bodies '''
        for filename in self.paths:
            email = Email(filename)
            yield email.get_sender()


    def count(self):
        ''' return file list count '''
        return len(self.paths)

    def at(self, index):
        ''' return mail from index '''
        return Email(self.paths[index])



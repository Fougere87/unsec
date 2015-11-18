import glob
from unsec import Tools
from unsec import Email


class EmailCollection(object):
    def __init__(self):
        self.paths  = []

    def get_emails(self, lang_filter = None):
        ''' return a generator of all email '''
        for filename in self.paths:
            email = Email(filename)
            if lang_filter is None:
                yield email
            elif lang_filter in ("fr","en"):
                if email.get_lang() == lang_filter:
                    yield email



    def add_file(self, filename):
        ''' add filename '''
        if filename not in self.paths:
            self.paths.append(filename)

    def add_from_directory(self, directory):
        ''' add filenames from the directory '''
        for f in glob.glob(directory+"/*"):
            self.add_file(f)


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

    def __str__(self):
        return "Collection of {} emails".format(self.count())



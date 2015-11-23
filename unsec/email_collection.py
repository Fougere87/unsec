# coding: utf8

"""email_collection.py: EmailCollection is a container for Email class """

__author__      = "Sacha Schutz - Hugo Mayer"
__copyright__   = "Copyright 2015, labsquare"
__license__     = "GPL3"
__email__       = "sacha@labsquare.org"

import re
import glob
from unsec import Email
import logging

class EmailCollection(object):
    def __init__(self):
        self.paths  = []


    def get_emails(self, lang_filter = None):
        """
        emails accessors
        @param string lang
        @return generator emails    emails in the collection
        """

        for filename in self.paths:
            email = Email(filename)
            if lang_filter is None:
                yield email
            elif lang_filter in ("fr","en"):
                if email.get_lang() == lang_filter:
                    yield email

    def add_file(self, filename):
        """
        add email from filename
        @param string filename
        """
        log = logging.getLogger(__name__)

        if filename not in self.paths:
            self.paths.append(filename)
            log.debug("add {}".format(filename))


    def add_from_directory(self, directory):
        """
        add email from a directory
        @param string directory     path of directory
        """
        for f in glob.glob(directory+"/*"):
            self.add_file(f)


    def get_subjects(self):
        """
        return all subjects from collection's emails
        @return generator subjects
        """
        for filename in self.paths:
            email = Email(filename)
            yield email.get_subject()


    def get_bodies(self):
        """
        return all bodies from collection's emails
        @return generator bodies
        """
        for filename in self.paths:
            email = Email(filename)
            yield email.get_body()


    def get_senders(self):
        """
        return all subjects from collection's emails
        @return generator senders
        """
        for filename in self.paths:
            email = Email(filename)
            yield email.get_sender()


    def count(self):
        """
        return size of collection
        @return int count
        """
        return len(self.paths)

    def at(self, index):
        """
        return email from index
        @return Email email
        """
        return Email(self.paths[index])


    def keep_lang(self, lang="fr", debug=True):

        log = logging.getLogger(__name__)
        log.info("Fitering language : {}".format(lang))
        paths_to_keeps = []
        for email in self.get_emails():
            if email.get_lang() == lang:
                paths_to_keeps.append(email.filename)
                log.debug("keep file {}".format(email.filename))


        self.paths = paths_to_keeps

    def __getitem__(self, index):
        return self.at(index)

    def __iter__(self):
        return self.get_emails()



    def __str__(self):
        return "Collection of {} emails".format(self.count())



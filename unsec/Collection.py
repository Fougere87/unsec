import glob
from unsec import Tools
from unsec import Email


class Email_Collection(object):
    def __init__(self, directory):
        self.emails = list()
        self.files_list =list() #can be used to retrive the email number in the directory
        mails = glob.glob(directory)
        print("creating collection...")
        for email in mails :
            e=Email(email)
            # if (e.clean_body() == None or e.clean_subject()== None) :
            #         print(email," is invalid, ignoring it.")
            # else :
            self.emails.append(e)
            self.files_list.append(email)

        self.all_cleaned_subjects = Email_Collection.get_cleaned_subjects(self, self.emails)
        self.all_cleaned_bodies   = Email_Collection.get_cleaned_bodies(self, self.emails)
        self.all_senders  = Email_Collection.get_senders(self, self.emails)
        
        print("collection créée...")


    # def get_email(self, directory):
    #     '''
    #     Returns the emails' paths from the dataset
    #     '''
    #     for email in glob.glob(directory): # bof..
    #         print(email)
    #         yield email

    def get_cleaned_subjects(self, emails):
        '''
        Returns a list containing all the emails' subjects
        '''
        return [email.clean_subject() for email in emails]

    def get_cleaned_bodies(self, emails):
        '''
        Returns a list containing all the emails' bodies
        '''
        return [email.clean_body() for email in emails]

    def get_senders(self, emails):
        '''
        Returns a list containing all the emails' senders
        '''
        return [email.sender() for email in emails]

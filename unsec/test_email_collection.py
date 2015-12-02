from unsec import EmailCollection, Email
from unsec import LARGE_DATASET_PATH
import glob
import re
import os

class TestEmailCollection(EmailCollection):
    def __init__(self, label = None, dataset = LARGE_DATASET_PATH ):
        super(TestEmailCollection, self).__init__(label)
        self.dataset = dataset

        for filename in glob.glob(self.dataset+"/*.email"):
            basename = os.path.basename(filename)
            cat      = re.sub("[1-9]+.+\.email","", basename)

            self.add_email(Email(filename, cat))






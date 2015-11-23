from unsec import EmailCollection, Email
from unsec import DATASET_PATH

import glob
from email.message import EmailMessage


class SmallEmailCollection(EmailCollection):
    def __init__(self):
        super(SmallEmailCollection,self).__init__()

        for path in glob.glob(DATASET_PATH+"/*.txt"):
            with open(path,"r") as file:
                raws = file.read().split("\n")
                subject = raws[0]
                body = "\n".join(raws[1:])

                message = EmailMessage()
                message["Subject"] = subject
                message.set_payload(body, "utf8")

                email = Email()
                email.from_bytes(message.as_bytes())







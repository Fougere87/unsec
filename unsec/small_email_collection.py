from unsec import EmailCollection
from unsec import DATASET_PATH
import glob

class SmallEmailCollection(EmailCollection):
    def __init__(self):
        super(SmallEmailCollection,self).__init__()

        for path in glob.glob(DATASET_PATH+"/*.txt"):
            with open(path,"r") as file:
                raws = file.read().split("\n")
                subject = raws[0]
                body = "\n".join(raws[1:])
                print(body)
                input()



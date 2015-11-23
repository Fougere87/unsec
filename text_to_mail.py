from email.message import EmailMessage
import glob

def convert(filename):
    with open(filename, "r") as file:
        raws    = file.read().split("\n")
        subject = raws[0]
        body    = "\n".join(raws[1:])

        email = EmailMessage()
        email.set_payload(body,"utf8")
        email["Subject"] = subject

        return email





for filename in glob.glob("unsec/dataset/large/*.txt"):

    with open(filename+".email","wb") as file:
        email = convert(filename)
        file.write(email.as_bytes())







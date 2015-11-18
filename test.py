import os
import glob
from email.header import decode_header, make_header
from email import message_from_binary_file
from email.header import decode_header, make_header



for f in glob.glob("data/bioinfo_2014-01/*"):
    email   = message_from_binary_file(open(f,"rb"))
    subject = str(make_header(decode_header(email.get("Subject"))))
    charset = email.get_charsets()[0]
    body    = email.get_payload(decode=True).decode(charset)
    print(f)
    print(body)
    input("press .. ")

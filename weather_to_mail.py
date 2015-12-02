from email.message import EmailMessage
import glob


with open("weather.txt") as file:
    lines = file.readlines()
    index = 0
    for line in lines:
        data = line.rstrip().split(",")
        category = data[0]
        body     = ",".join(data[1:])

        email = EmailMessage()
        email.set_payload(body,"utf8")
        email["Subject"] = category

        with open("unsec/dataset/small/"+category+str(index)+".email","wb") as file2:
            file2.write(email.as_bytes())


        index+=1

import dropbox
import dropbox.files
import os

#App: Bgremove on dropbox
TOKEN = "sl.BlpxLvFMFhJ-NjZ0ejffFyHyJyognaTU9tqSCAqTknTtVXbbGu1IQCRbzq98TW2ejiPW2STGwHqIjD4ibnE8sf-z9dCDyprjfIVQqxeQtraunPOU3w-nA3Bwly04McPQedbnsxp1MVrl03-yQRYn2kk"
dbx = dropbox.Dropbox(TOKEN)

def upload_files():
    for file in os.listdir("media/2023/09"):
        with open(os.path.join("media/2023/09",file),"rb") as f:
            data = f.read()
            dbx.files_upload(data,f"/{file}")

upload_files()
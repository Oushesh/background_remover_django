import dropbox
import os

def upload_to_dropbox(image_path, destination_path, access_token):
    with open(image_path, "rb") as image_file:
        dbx = dropbox.Dropbox(access_token)
        try:
            dbx.files_upload(image_file.read(), destination_path, mode=dropbox.files.WriteMode("overwrite"))
            print(f"Uploaded {image_path} to {destination_path} in Dropbox")
        except dropbox.exceptions.ApiError as err:
            print(f"API error: {err}")

if __name__ == "__main__":
    #Dropbox app name:
    ACCESS_TOKEN = "sl.BlqmRHlhTgNa9kl6u2AzuLxKBU5IkybUFB517IywH_ - jhrBwzZ5A3QWQvBKhu_qkIMAyOTj0lrNIXI8DFhEmIlnYfSWFKk1 - mQigD8NLRxXCoErzspbqt_0JRX8gqvaotknRPs - UVWFU"

    # Local image path and the path where you want to save the image in Dropbox
    IMAGE_PATH = "media/2023/09/20230905_122716.jpeg"
    DESTINATION_PATH = "https://www.dropbox.com/scl/fo/jf97szegrp01chpg6lsk8/h?rlkey=waoojc609zf7nq4ifji7g4u1e&dl=0"
    upload_to_dropbox(IMAGE_PATH, DESTINATION_PATH, ACCESS_TOKEN)

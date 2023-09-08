import dropbox
import os


def upload_to_dropbox(image_path, destination_path, access_token):
    """
    Upload an image to Dropbox.

    :param image_path: local path to the image you want to upload
    :param destination_path: path in Dropbox where you want the image to be saved
    :param access_token: your Dropbox OAuth2 access token
    """
    with open(image_path, "rb") as image_file:
        dbx = dropbox.Dropbox(access_token)
        try:
            dbx.files_upload(image_file.read(), destination_path, mode=dropbox.files.WriteMode("overwrite"))
            print(f"Uploaded {image_path} to {destination_path} in Dropbox")
        except dropbox.exceptions.ApiError as err:
            print(f"API error: {err}")


if __name__ == "__main__":
    # Load your access token from an environment variable or hardcoded string

    ACCESS_TOKEN = "qckrh0b36gaarzm"

    # Local image path and the path where you want to save the image in Dropbox
    IMAGE_PATH = "media/2023/09/20230905_122716.jpeg"
    DESTINATION_PATH = "/path_in_dropbox.jpg"

    upload_to_dropbox(IMAGE_PATH, DESTINATION_PATH, ACCESS_TOKEN)

## dropbox: view check

import dropbox
from PIL import Image
from io import BytesIO

# Initialize the Dropbox client
DROPBOX_OAUTH2_TOKEN = "sl.BlpxLvFMFhJ-NjZ0ejffFyHyJyognaTU9tqSCAqTknTtVXbbGu1IQCRbzq98TW2ejiPW2STGwHqIjD4ibnE8sf-z9dCDyprjfIVQqxeQtraunPOU3w-nA3Bwly04McPQedbnsxp1MVrl03-yQRYn2kk"
dbx = dropbox.Dropbox(DROPBOX_OAUTH2_TOKEN)

# Define the shared link
shared_link = "https://replay.dropbox.com/share/VB2Z22hReJPnxti7"

# Download the image
metadata, res = dbx.sharing_get_shared_link_file(shared_link)

# Read the image bytes and open it using PIL
image_bytes = res.content
image = Image.open(BytesIO(image_bytes))
image.show()

#need to test the image.

from io import BytesIO
import os

from django.core.files import File
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from rembg import remove
import requests
from requests.adapters import Retry, HTTPAdapter

from .models import UserActivity

session = requests.Session()  # to retry failed requests (3 times)
retries = Retry(total=3, backoff_factor=1)
session.mount("http://", HTTPAdapter(max_retries=retries))
session.mount("https://", HTTPAdapter(max_retries=retries))


@receiver(post_save, sender=UserActivity)
def process_image(sender, instance, *args, **kwargs):
    """Process user uploaded image and remove its background."""
    if instance.result:
        return

    environment = os.getenv("DJANGO_SETTINGS_MODULE")
    print ("environment")
    """
    if "production" in environment:
        # get image from Dropbox when in production
        # change to get image from local

        #Hard coded instance image url from dropbox link.
        image_link = "https://www.dropbox.com/scl/fi/kvfpkl5rvpf0qsoo44sga/20230905_122716.jpeg?rlkey=z0g7tdb8gcq2gm53o85ze8fz2&dl=0"
        response = session.get(image_link)
        #response = session.get(instance.image.url)

        if response.status_code != 200:
            return
        #else open the Image
        image_file = Image.open(BytesIO(response.content))
        response = None
    else:
    """
    # get image from disk when in local
    image_link = "https://www.facebook.com/BeautifulBusinMauritius/photos/a.324200598457987/870665687144806/?__cft__[0]=AZU9u8DcmfeRnLUTFRy3O0qc4lLwB0KFH2D88lRFZU_RAXsh5JFkO3ufNcE-M2qjSsYUH_CDgnORClCJm0ao0v8Fj5jyxNSlXi-NZhCfD8Xp9s-7RzDWrlIdB0I9YqixkQM&__tn__=EH-R"
    response = requests.get(image_link)
    image_file = Image.open(BytesIO(response.content))


        #image_file = Image.open(instance.image.path)
    
    path, ext = instance.image.name.split(".")
    filename = path.split("/")[-1]
    result_path = f"{filename}_output.{ext}"



    output = remove(image_file)  #remove background using rembg
    image_file = None

    output.convert("RGB")
    output.save(result_path, "PNG")
    output = None

    instance.result.save(result_path, File(open(result_path, "rb")))
    os.remove(result_path)

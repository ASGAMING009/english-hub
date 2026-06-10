import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.core.files.storage import Storage
from django.core.files.base import ContentFile
import urllib.request


class CloudinaryMediaStorage(Storage):
    def _save(self, name, content):
        result = cloudinary.uploader.upload(
            content,
            public_id=name.split('.')[0],
            resource_type='auto'
        )
        return result['public_id']

    def _open(self, name, mode='rb'):
        url = self.url(name)
        response = urllib.request.urlopen(url)
        return ContentFile(response.read())

    def url(self, name):
        return cloudinary.CloudinaryImage(name).build_url()

    def exists(self, name):
        try:
            cloudinary.api.resource(name)
            return True
        except:
            return False

    def delete(self, name):
        cloudinary.uploader.destroy(name)
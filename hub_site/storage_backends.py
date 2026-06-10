import cloudinary.uploader
import cloudinary.api
from django.core.files.storage import Storage
from django.conf import settings
import cloudinary


class CloudinaryMediaStorage(Storage):
    def _save(self, name, content):
        result = cloudinary.uploader.upload(
            content,
            public_id=name.split('.')[0],
            resource_type='auto'
        )
        return result['public_id']

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
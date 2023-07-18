import boto3
from botocore.exceptions import ClientError
from django.conf import settings

from django.db import models
from django.utils import timezone
from django.urls import reverse
from django_resized import ResizedImageField
from django_quill.fields import QuillField


class Ebook(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    description_long = QuillField(blank=True, null=True, default='')
    description_short = QuillField(blank=True, null=True, default='')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = ResizedImageField(force_format="WEBP", quality=75, upload_to='images')
    small_image = ResizedImageField(size=[390, 285], force_format="WEBP", quality=75, upload_to='images_small', default = '')
    upload = models.FileField(upload_to="ebook/")
    object = models.Manager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
         return reverse('ebook:ebook_detail',
                         args=[self.slug])

    def get_presigned_url(self):
        s3_client = boto3.client('s3',
                                 aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                                 region_name=settings.AWS_S3_REGION_NAME)
        try:
            response = s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                        'Key': 'static/' + self.upload.name,
                        'ResponseContentDisposition': 'attachment; filename="{}"'.format(
                            'static/' + self.upload.name.split('/')[-1])
                        },
                ExpiresIn=3600  # URL expiration time in seconds
            )
        except ClientError as e:
            # Handle any errors here
            return None
        return response


class EbookEmails(models.Model):
    email = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    time = models.DateTimeField(default=timezone.now)
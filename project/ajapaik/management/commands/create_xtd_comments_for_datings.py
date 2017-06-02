from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from django.conf import settings
from project.ajapaik.models import Dating, MyXtdComment


class Command(BaseCommand):
    help = "Get all the Datings, create django-comments-xtd comments"

    def handle(self, *args, **options):
        content_type_id = ContentType.objects.filter(app_label='ajapaik', model='photo').first().pk

        # Get datings which have no MyXtdComment
        datings = Dating.objects.filter(comment_obj=None)

        for dating in datings:
            ajapaik_user = dating.profile
            if ajapaik_user:
                comment = MyXtdComment.objects.create(
                    user=ajapaik_user.user,
                    level=0,
                    followup=False,
                    is_public=True,
                    is_removed=False,
                    site_id=settings.SITE_ID,
                    content_type_id=content_type_id,
                    comment=dating.comment,
                    object_pk=dating.photo.id,
                    submit_date=dating.created,
                    comment_type=MyXtdComment.DATING_TYPE
                )

                dating.comment_obj = comment
                dating.save()

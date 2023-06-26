from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(
            name='sourjo13',
            email = 'sourjo13@hotmail.com',
            is_staff = True,
            is_superuser = True,
            phone = '7767953248',
            gender = 'Male'
        )

        user.set_password("12345")
        user.save()
    dependencies=[]
    operations=[migrations.RunPython(seed_data),]
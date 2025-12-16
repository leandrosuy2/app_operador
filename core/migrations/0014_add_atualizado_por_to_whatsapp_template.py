# Generated manually to fix OperationalError

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0013_anexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='whatsapptemplate',
            name='atualizado_por',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='whatsapp_templates',
                to=settings.AUTH_USER_MODEL
            ),
        ),
    ]


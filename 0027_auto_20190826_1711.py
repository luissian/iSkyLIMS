# Generated by Django 2.2 on 2019-08-26 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('iSkyLIMS_core', '0012_auto_20190826_1620'),
        ('iSkyLIMS_wetlab', '0026_auto_20190811_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='libraryPreparation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('singlePairedEnd', models.CharField(max_length=20)),
                ('lengthRead', models.CharField(max_length=5)),
                ('indexValues_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='iSkyLIMS_wetlab.IndexLibraryValues')),
                ('molecule_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iSkyLIMS_core.MoleculePreparation')),
            ],
        ),
        migrations.CreateModel(
            name='ProtocolLibrary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protocolName', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=160, null=True)),
                ('generated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReagentsUserCommercialKits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickName', models.CharField(max_length=60)),
                ('numberOfUses', models.IntegerField(default=0, null=True)),
                ('latestUsedDate', models.DateTimeField(null=True)),
                ('chipLot', models.CharField(max_length=100)),
                ('expirationDate', models.DateField()),
                ('generatedat', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Laboratory',
        ),
        migrations.RemoveField(
            model_name='naprotparamdata',
            name='NA_Parameter_id',
        ),
        migrations.RemoveField(
            model_name='naprotparamdata',
            name='sample_id',
        ),
        migrations.RemoveField(
            model_name='nucleotidescomercialkits',
            name='protocol_id',
        ),
        migrations.RemoveField(
            model_name='nucleotidescomercialkits',
            name='registerUser',
        ),
        migrations.RemoveField(
            model_name='samplesinproject',
            name='project_id',
        ),
        migrations.DeleteModel(
            name='SampleType',
        ),
        migrations.DeleteModel(
            name='Species',
        ),
        migrations.DeleteModel(
            name='StatesForSample',
        ),
        migrations.RemoveField(
            model_name='reagentscommercialkits',
            name='chipLot',
        ),
        migrations.RemoveField(
            model_name='reagentscommercialkits',
            name='cuantityUsed',
        ),
        migrations.RemoveField(
            model_name='reagentscommercialkits',
            name='expirationDate',
        ),
        migrations.RemoveField(
            model_name='reagentscommercialkits',
            name='usedDate',
        ),
        migrations.AddField(
            model_name='reagentscommercialkits',
            name='maximunUses',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='protocollibraryparameters',
            name='protocol_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iSkyLIMS_wetlab.ProtocolLibrary'),
        ),
        migrations.AlterField(
            model_name='reagentscommercialkits',
            name='protocol_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='iSkyLIMS_wetlab.ProtocolLibrary'),
        ),
        migrations.RenameModel(
            old_name='NAProtocolParameters',
            new_name='ProtocolLibraryParameters',
        ),
        migrations.DeleteModel(
            name='NAProtParamData',
        ),
        migrations.DeleteModel(
            name='NucleotidesComercialKits',
        ),
        migrations.DeleteModel(
            name='ProtocolInLab',
        ),
        migrations.DeleteModel(
            name='SamplesInProject',
        ),
        migrations.AddField(
            model_name='reagentsusercommercialkits',
            name='reagentUserKit_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='iSkyLIMS_wetlab.ReagentsCommercialKits'),
        ),
        migrations.AddField(
            model_name='reagentsusercommercialkits',
            name='registerUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='librarypreparation',
            name='protocol_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='iSkyLIMS_wetlab.ProtocolLibrary'),
        ),
        migrations.AddField(
            model_name='librarypreparation',
            name='reagent_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='iSkyLIMS_wetlab.ReagentsUserCommercialKits'),
        ),
        migrations.AddField(
            model_name='librarypreparation',
            name='registerUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Premio.foto'
        db.delete_column('website_premio', 'foto')

        # Adding field 'Premio.thumbnail'
        db.add_column('website_premio', 'thumbnail',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=300, blank=True),
                      keep_default=False)

        # Adding field 'Premio.quantidade_de_fotos'
        db.add_column('website_premio', 'quantidade_de_fotos',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

    def backwards(self, orm):
        # Adding field 'Premio.foto'
        db.add_column('website_premio', 'foto',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=300, blank=True),
                      keep_default=False)

        # Deleting field 'Premio.thumbnail'
        db.delete_column('website_premio', 'thumbnail')

        # Deleting field 'Premio.quantidade_de_fotos'
        db.delete_column('website_premio', 'quantidade_de_fotos')

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'website.conta': {
            'Meta': {'object_name': 'Conta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'default': '0', 'unique': 'True'}),
            'premios_recuperados': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['website.Premio']", 'symmetrical': 'False'}),
            'saldo': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'website.premio': {
            'Meta': {'object_name': 'Premio'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mais_informacoes': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '120'}),
            'prazo_de_entrega': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'quantidade_de_fotos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'thumbnail': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'valor': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['website']
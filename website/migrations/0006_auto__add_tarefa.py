# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tarefa'
        db.create_table('website_tarefa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('valor', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('tempo_para_execucao', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('bonus_voluntario', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('tempo_para_bonus', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('bonus_de_tempo', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('tempo_para_desconto', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('desconto_por_tempo', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('tempo_limite', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('website', ['Tarefa'])

    def backwards(self, orm):
        # Deleting model 'Tarefa'
        db.delete_table('website_tarefa')

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
        'website.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '120'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
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
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Categoria']", 'null': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mais_informacoes': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '120'}),
            'prazo_de_entrega': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'quantidade_de_fotos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'thumbnail': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'valor': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'website.tarefa': {
            'Meta': {'object_name': 'Tarefa'},
            'bonus_de_tempo': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'bonus_voluntario': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'desconto_por_tempo': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'tempo_limite': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'tempo_para_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'tempo_para_desconto': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'tempo_para_execucao': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'valor': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['website']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field sabores on 'Premio'
        db.create_table('website_premio_sabores', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('premio', models.ForeignKey(orm['website.premio'], null=False)),
            ('sabor', models.ForeignKey(orm['website.sabor'], null=False))
        ))
        db.create_unique('website_premio_sabores', ['premio_id', 'sabor_id'])

        # Adding M2M table for field cores on 'Premio'
        db.create_table('website_premio_cores', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('premio', models.ForeignKey(orm['website.premio'], null=False)),
            ('cor', models.ForeignKey(orm['website.cor'], null=False))
        ))
        db.create_unique('website_premio_cores', ['premio_id', 'cor_id'])

        # Adding M2M table for field tamanhos on 'Premio'
        db.create_table('website_premio_tamanhos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('premio', models.ForeignKey(orm['website.premio'], null=False)),
            ('tamanho', models.ForeignKey(orm['website.tamanho'], null=False))
        ))
        db.create_unique('website_premio_tamanhos', ['premio_id', 'tamanho_id'])

    def backwards(self, orm):
        # Removing M2M table for field sabores on 'Premio'
        db.delete_table('website_premio_sabores')

        # Removing M2M table for field cores on 'Premio'
        db.delete_table('website_premio_cores')

        # Removing M2M table for field tamanhos on 'Premio'
        db.delete_table('website_premio_tamanhos')

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
        'website.cor': {
            'Meta': {'object_name': 'Cor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '120'})
        },
        'website.grupodetarefas': {
            'Meta': {'object_name': 'GrupoDeTarefas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '120'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        'website.premio': {
            'Meta': {'object_name': 'Premio'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Categoria']", 'null': 'True'}),
            'cores': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['website.Cor']", 'symmetrical': 'False'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mais_informacoes': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '120'}),
            'prazo_de_entrega': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'quantidade_de_fotos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sabores': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['website.Sabor']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'tamanhos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['website.Tamanho']", 'symmetrical': 'False'}),
            'thumbnail': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'valor': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'website.sabor': {
            'Meta': {'object_name': 'Sabor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '120'})
        },
        'website.tamanho': {
            'Meta': {'object_name': 'Tamanho'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '120'})
        },
        'website.tarefa': {
            'Meta': {'object_name': 'Tarefa'},
            'bonus_de_tempo': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'bonus_voluntario': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'desconto_por_tempo': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.GrupoDeTarefas']", 'null': 'True'}),
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
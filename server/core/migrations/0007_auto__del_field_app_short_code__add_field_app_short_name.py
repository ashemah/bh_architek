# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'App.short_code'
        db.delete_column(u'core_app', 'short_code')

        # Adding field 'App.short_name'
        db.add_column(u'core_app', 'short_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'App.short_code'
        db.add_column(u'core_app', 'short_code',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)

        # Deleting field 'App.short_name'
        db.delete_column(u'core_app', 'short_name')


    models = {
        u'core.app': {
            'Meta': {'object_name': 'App'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'core.appbinding': {
            'Meta': {'object_name': 'AppBinding'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.service': {
            'Meta': {'object_name': 'Service'},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'services'", 'to': u"orm['core.App']"}),
            'container_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'container_name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'templates'", 'to': u"orm['core.ServiceTemplate']"})
        },
        u'core.servicelink': {
            'Meta': {'object_name': 'ServiceLink'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'from_service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'links_to'", 'to': u"orm['core.Service']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'links_from'", 'to': u"orm['core.Service']"})
        },
        u'core.servicetemplate': {
            'Meta': {'object_name': 'ServiceTemplate'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'core.volume': {
            'Meta': {'object_name': 'Volume'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['core']
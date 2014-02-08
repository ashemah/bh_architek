# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'App'
        db.create_table(u'core_app', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'core', ['App'])

        # Adding model 'Volume'
        db.create_table(u'core_volume', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'core', ['Volume'])

        # Adding model 'ServiceTemplate'
        db.create_table(u'core_servicetemplate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('image_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'core', ['ServiceTemplate'])

        # Adding model 'Service'
        db.create_table(u'core_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(related_name='services', to=orm['core.App'])),
            ('state', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(related_name='templates', to=orm['core.ServiceTemplate'])),
            ('instance_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'core', ['Service'])

        # Adding model 'ServiceLink'
        db.create_table(u'core_servicelink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('from_service', self.gf('django.db.models.fields.related.ForeignKey')(related_name='links_to', to=orm['core.Service'])),
            ('to_service', self.gf('django.db.models.fields.related.ForeignKey')(related_name='links_from', to=orm['core.Service'])),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'core', ['ServiceLink'])

        # Adding model 'AppBinding'
        db.create_table(u'core_appbinding', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'core', ['AppBinding'])


    def backwards(self, orm):
        # Deleting model 'App'
        db.delete_table(u'core_app')

        # Deleting model 'Volume'
        db.delete_table(u'core_volume')

        # Deleting model 'ServiceTemplate'
        db.delete_table(u'core_servicetemplate')

        # Deleting model 'Service'
        db.delete_table(u'core_service')

        # Deleting model 'ServiceLink'
        db.delete_table(u'core_servicelink')

        # Deleting model 'AppBinding'
        db.delete_table(u'core_appbinding')


    models = {
        u'core.app': {
            'Meta': {'object_name': 'App'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.appbinding': {
            'Meta': {'object_name': 'AppBinding'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.service': {
            'Meta': {'object_name': 'Service'},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'services'", 'to': u"orm['core.App']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
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
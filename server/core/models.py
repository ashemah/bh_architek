from django.db import models
from builder.server import BuilderServer


class App(models.Model):
    display_name = models.CharField(max_length=40)
    short_name = models.CharField(max_length=20)

    def service_list(self):
        res = []
        for service in self.services.all():
            res.append({
                'image_name': service.template.image_name,
                'container_name': service.container_name
            })

        return res

    def __unicode__(self):
        return self.display_name


class Volume(models.Model):
    display_name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.display_name


class ServiceTemplate(models.Model):
    display_name = models.CharField(max_length=40)
    image_name = models.CharField(max_length=40)
    short_name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.display_name


class Service(models.Model):

    STATE_CHOICES = (
        (BuilderServer.STATE_NOTFOUND, "Not found"),
        (BuilderServer.STATE_STOPPED, "Stopped"),
        (BuilderServer.STATE_STARTING, "Starting"),
        (BuilderServer.STATE_RUNNING, "Running"),
        (BuilderServer.STATE_STOPPING, "Stopping"),
    )

    app = models.ForeignKey(App, related_name='services')
    state = models.IntegerField(default=BuilderServer.STATE_NOTFOUND, choices=STATE_CHOICES)
    template = models.ForeignKey(ServiceTemplate, related_name='templates')

    container_name = models.CharField(max_length=40, blank=True, null=True)
    container_id = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.app.display_name + "::" + self.template.display_name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        self.container_name = self.app.short_name + '-' + self.template.short_name
        super(Service, self).save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    @classmethod
    def update_from_info(self, info):

        for service_info in info:

            print service_info

            service = Service.objects.get(container_name=service_info['container_name'])

            if 'container_status' in service_info:
                service.state = service_info['container_status']

            if 'container_id' in service_info:
                service.container_id = service_info['container_id']

            service.save()



class ServiceLink(models.Model):
    display_name = models.CharField(max_length=40)
    from_service = models.ForeignKey(Service, related_name='links_to')
    to_service = models.ForeignKey(Service, related_name='links_from')
    alias = models.CharField(max_length=20)

    def __unicode__(self):
        return self.display_name


class ServiceEnvironmentValue(models.Model):
    service = models.ForeignKey(Service, related_name='env')
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s -> %s=%s" % (self.service.display, self.name, self.value)


class AppBinding(models.Model):
    pass
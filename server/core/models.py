from django.db import models


class App(models.Model):
    display_name = models.CharField(max_length=40)


class Volume(models.Model):
    display_name = models.CharField(max_length=40)


class ServiceTemplate(models.Model):
    display_name = models.CharField(max_length=40)
    image_name = models.CharField(max_length=40)
    short_name = models.CharField(max_length=20)


class Service(models.Model):

    STATE_UNKNOWN = 0
    STATE_NOTFOUND = 1
    STATE_STARTING = 2
    STATE_RUNNING = 3
    STATE_STOPPING = 4
    STATE_STOPPED = 5

    STATE_CHOICES = (
        (STATE_UNKNOWN, "Unknown"),
        (STATE_NOTFOUND, "Not Found"),
        (STATE_STARTING, "Starting"),
        (STATE_RUNNING, "Running"),
        (STATE_STOPPING, "Stopping"),
        (STATE_STOPPED, "Stopped")
    )

    app = models.ForeignKey(App, related_name='services')
    state = models.IntegerField(default=STATE_UNKNOWN, choices=STATE_CHOICES)
    template = models.ForeignKey(ServiceTemplate, related_name='templates')
    instance_name = models.CharField(max_length=40)


class ServiceLink(models.Model):
    display_name = models.CharField(max_length=40)
    from_service = models.ForeignKey(Service, related_name='links_to')
    to_service = models.ForeignKey(Service, related_name='links_from')
    alias = models.CharField(max_length=20)


class AppBinding(models.Model):
    pass
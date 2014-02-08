import zerorpc


class BuilderClient(object):

    def __init__(self, host, port):

        self.host = host
        self.port = port

        self.conn = zerorpc.Client()
        self.conn.connect("tcp://%s:%d" % (self.host, self.port))

    def status(self, info):
        return self.conn.status(info)

    def start(self, app_id, service_list):
        return self.conn.start(app_id, service_list)

    def stop(self, app_id, service_list):
        return self.conn.stop(app_id, service_list)

    def build(self, app_id, service_list):
        return self.conn.build(app_id, service_list)

    def remove(self, app_id, service_list):
        return self.conn.remove(app_id, service_list)

    def kill(self, app_id, service_list):
        return self.conn.kill(app_id, service_list)

if __name__ == '__main__':

    import sys

    host = sys.argv[1]
    port = int(sys.argv[2])

    c = BuilderClient(host, port)

    info = [
        {
            'image_name': 'bh_redis',
            'container_name': ''
        }
    ]

    print c.status(info)

    service_list = [
        {
            'image_name': 'bh_redis',
            'container_name': 'safe_d-redis_stats'
        }
    ]

    print c.build('safe_d', service_list)
    print c.start('safe_d', service_list)
    print c.stop('safe_d', service_list)
    print c.remove('safe_d', service_list)
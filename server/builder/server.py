import zerorpc
import docker


class BuilderServer(object):

    class ContainerExists(Exception):
        pass

    class ContainerInfoFailed(Exception):
        pass

    IMAGE_NOTFOUND = 0
    IMAGE_FOUND = 1

    STATE_NOTFOUND = 0
    STATE_STARTING = 1
    STATE_RUNNING = 2
    STATE_STOPPING = 3
    STATE_STOPPED = 4

    def __init__(self):
        self.docker = docker.Client(base_url='unix://var/run/docker.sock', version='1.7', timeout=10)

    def build(self, app_id, service_list):
        print "build: %s" % service_list

        res = []

        for item in service_list:
            image_name = item['image_name']
            container_name = item['container_name']

            container_info = self.container_info(container_name)
            container_status = container_info['state']

            print container_info

            if container_status != BuilderServer.STATE_NOTFOUND:
                raise BuilderServer.ContainerExists("Container '%s' exists. Build aborted." % container_name)

            build_res = self.docker.create_container(image_name, name=container_name)
            container_id = build_res['Id']

            container_info = self.container_info(container_name)
            container_status = container_info['state']

            item_res = {
                'container_name': container_name,
                'container_id': container_id,
                'container_status': container_status
            }

            res.append(item_res)

        return res

    def start(self, app_id, info):
        print "start: %s" % info

        res = []

        for item in info:
            container_name = item['container_name']
            self.docker.start(container_name, publish_all_ports=True)

            container_info = self.container_info(container_name)
            container_status = container_info['state']

            item_res = {
                'container_name': container_name,
                'container_status': container_status
            }

            res.append(item_res)

        return res

    def stop(self, app_id, info):
        print "stop: %s" % info

        res = []

        for item in info:
            container_name = item['container_name']
            self.docker.stop(container_name)

            container_info = self.container_info(container_name)
            container_status = container_info['state']

            item_res = {
                'container_name': container_name,
                'container_status': container_status
            }

            res.append(item_res)

        return res

    def kill(self, app_id, info):
        print "kill: %s" % info

        res = []

        for item in info:
            container_name = item['container_name']
            self.docker.kill(container_name)

            container_info = self.container_info(container_name)
            container_status = container_info['state']

            item_res = {
                'container_name': container_name,
                'container_status': container_status
            }

            res.append(item_res)

        return res

    def remove(self, app_id, info):
        print "remove: %s" % info

        res = []

        for item in info:
            container_name = item['container_name']
            self.docker.remove_container(container_name)

            container_info = self.container_info(container_name)
            container_status = container_info['state']

            item_res = {
                'container_name': container_name,
                'container_status': container_status
            }

            res.append(item_res)

        return res

    def status(self, info):
        print "status: %s" % info

        res = []

        for item in info:

            item_res = {}

            if 'container_name' in item:
                container_name = item['container_name']
                container_info = self.container_info(container_name)
                container_status = container_info['state']

                item_res['container_name'] = container_name
                item_res['container_status'] = container_status

            if 'image_name' in item:
                image_name = item['image_name']
                image_status = self.image_status(image_name)

                item_res['image_name'] = image_name
                item_res['image_status'] = image_status

            res.append(item_res)

        return res

    def image_status(self, image_name):
        try:
            info = self.docker.inspect_image(image_name)
            return BuilderServer.IMAGE_FOUND
        except docker.APIError, e:
            return BuilderServer.IMAGE_NOTFOUND

    def container_info(self, container_name):

        state = BuilderServer.STATE_NOTFOUND
        ports = []

        try:
            info = self.docker.inspect_container(container_name)
            state_info = info['State']
            if state_info['Running'] is True:
                state = BuilderServer.STATE_RUNNING
            else:
                state = BuilderServer.STATE_STOPPED

        except docker.APIError, e:
            pass

        return {
            'ports': ports,
            'state': state
        }
        # raise Builder.ContainerInfoFailed("Unable to get container info")


    @staticmethod
    def run(hostname):

        s = zerorpc.Server(BuilderServer())
        s.bind("tcp://%s" % hostname)

        print "Builder Server listening on %s" % hostname

        s.run()


if __name__ == '__main__':

    import sys
    hostname = sys.argv[1]
    BuilderServer.run(hostname)


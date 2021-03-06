import docker
import argparse
from kazoo.client import KazooClient
from kazoo.client import KazooState


class DataSpoutContainers:
    def __init__(self):
        self.client = docker.from_env()
        self.dockerfile_path = './'
        self.image_tag = 'dataspout'
        self.image = None

    def build_image(self):
        print('Start building image....')
        self.image = self.client.images.build(path=self.dockerfile_path, tag=self.image_tag)

    def run_container(self, name, hostname, command):
        container = self.client.containers.run(image='dataspout',
                                               detach=True,
                                               name=name,
                                               hostname=hostname,
                                               tty=True,
                                               stdin_open=True,
                                               command=command)
        return container

    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-a', '--address', type=str, default='127.0.0.1', help='The address of destination.')
        parser.add_argument('-p', '--port', type=str, default='2341', help='The port number of destination.')
        args = parser.parse_args()
        address = args.address
        port = args.port
        for i in range(5):
            container_name = 'DataSpout' + str(i+1)
            print('Start running container DataSpout %s' % str(i+1))
            command = 'python /home/SpoutingData.py -s ' + str(i+1) + ' -a ' + address + ' -p ' + port
            self.run_container(container_name, container_name, command)


if __name__ == '__main__':
    spout = DataSpoutContainers()
    spout.build_image()
    spout.main()









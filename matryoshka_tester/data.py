containers = dict()
containers["go"] = {
    "1.16": "registry.opensuse.org/home/fcrozat/matryoshka/containerfile/opensuse/golang:1.16",
    "1.15": "registry.opensuse.org/home/fcrozat/matryoshka/containerfile/opensuse/golang:1.15",
}
containers["node"] = {
    "15": "registry.opensuse.org/home/fcrozat/matryoshka/containers_node15/node15:latest",
    "14": "registry.opensuse.org/home/fcrozat/matryoshka/containers_node14/node14:latest",
    "12": "registry.opensuse.org/home/fcrozat/matryoshka/containers_node12/node12:latest",
}
containers["openjdk"] = {
    "16": "registry.opensuse.org/home/fcrozat/matryoshka/containerfile/opensuse/openjdk:16",
    "11": "registry.opensuse.org/home/fcrozat/matryoshka/containerfile/opensuse/openjdk:11",
}
containers["python"] = {
    "3.9": "registry.opensuse.org/home/fcrozat/matryoshka/containers_python39/python39:latest",
    "3.8": "registry.opensuse.org/home/fcrozat/matryoshka/containers_python38/python38:latest",
    "3.6": "registry.opensuse.org/home/fcrozat/matryoshka/containers_python36/python36:latest",
}
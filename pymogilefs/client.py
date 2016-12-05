from pymogilefs.backend import Backend
from pymogilefs.request import Request


class Client:
    def __init__(self, trackers):
        self._backend = Backend(trackers)

    def _do_request(self, config, **kwargs):
        return self._backend.do_request(Request(config, **kwargs)).items

    def get_hosts(self):
        return self._do_request(GetHostsConfig)

    def create_host(self, host, ip, port):
        return self._do_request(CreateHostConfig, host=host, ip=ip, port=port)

    def update_host(self, host, ip, port):
        return self._do_request(UpdateHostConfig, host=host, ip=ip, port=port)

    def delete_host(self, host):
        return self._do_request(DeleteHostConfig, host=host)

    def get_domains(self):
        return self._do_request(GetDomainsConfig)

    def create_domain(self, domain):
        return self._do_request(CreateDomainConfig, domain=domain)

    def delete_domain(self, domain):
        return self._do_request(DeleteDomainConfig, domain=domain)

    def get_classes(self):
        raise NotImplementedError

    def create_class(self, domain, _class, mindevcount):
        return self._do_request(CreateClassConfig,
                                domain=domain,
                                _class=_class,
                                mindevcount=mindevcount)

    def update_class(self, domain, _class, mindevcount):
        return self._do_request(UpdateClassConfig,
                                domain=domain,
                                _class=_class,
                                mindevcount=mindevcount)

    def delete_class(self, domain, _class):
        return self._do_request(DeleteClassConfig,
                                domain=domain,
                                _class=_class)

    def get_devices(self):
        return self._do_request(GetDevicesConfig)

    def create_device(self, hostname, devid, hostip, state):
        return self._do_request(CreateClassConfig,
                                hostname=hostname,
                                devid=devid,
                                hostip=hostip,
                                state=state)

    def set_state(self, host, device, state):
        return self._do_request(SetStateConfig,
                                host=host,
                                device=device,
                                state=state)

    def set_weight(self, host, device, weight):
        return self._do_request(SetWeightConfig,
                                host=host,
                                device=device,
                                weight=weight)


class GetHostsConfig:
    COMMAND = 'get_hosts'
    PREFIX_RE = r'^host[0-9]+_'


class CreateHostConfig:
    COMMAND = 'create_host'
    PREFIX_RE = r'^host'


class UpdateHostConfig:
    COMMAND = 'update_host'
    PREFIX_RE = r'^host'


class DeleteHostConfig:
    COMMAND = 'delete_host'
    PREFIX_RE = r'^host'


class GetDomainsConfig:
    COMMAND = 'get_domains'
    PREFIX_RE = r'^domain[0-9]+'


class GetDevicesConfig:
    COMMAND = 'get_devices'
    PREFIX_RE = r'^dev[0-9]+_'

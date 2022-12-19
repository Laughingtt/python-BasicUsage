#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/12/5 11:12 AM 
# ide： PyCharm
from pynginxconfig import NginxConfig


class TransmitNginxConfig(NginxConfig):
    def __init__(self):
        super(TransmitNginxConfig, self).__init__(offset_char=' ')

    def add_upstream_block(self, origin_server_name, server_ip_port):
        """
        增加upstream
        """
        http_block = self.get_value(self.get([('http',)]))

        sub_upstream = {'name': 'upstream', 'param': origin_server_name, 'value': [('server', server_ip_port)]}
        for sub_block in http_block:
            if isinstance(sub_block, dict):
                if (sub_upstream['name'], sub_upstream['param']) == (sub_block['name'], sub_block['param']):
                    raise KeyError("key already in this block")
        http_block.append(sub_upstream)

    def add_location_transmit(self, origin_server_name, header_key):
        """
        增加本地转发逻辑
        """
        server_block = self.get_value(self.get([('http',), ('server',)]))
        value_list = None
        for sub_block in server_block:
            if isinstance(sub_block, dict) and sub_block.get("name", None) == "location":
                value_list = sub_block.get("value")
                break

        transmit_rule = {'name': 'if',
                         'param': '($http_x_app = "{}")'.format(header_key),
                         'value': [('proxy_pass', 'http://{}'.format(origin_server_name))]}
        for sub_old_rule in value_list:
            param = sub_old_rule.get("param")
            if param == transmit_rule["param"]:
                raise KeyError("key already in this block")
        value_list.append(transmit_rule)


class ModifyNginxConfig:
    def __init__(self, conf_path):
        self.conf_path = conf_path
        self.nc = None
        self.init_nc()

    def init_nc(self):
        self.nc = TransmitNginxConfig()
        self.nc.loadf(path)

    def add_transmit_rule(self, origin_server_name, server_ip_port, header_key):

        try:
            self.nc.add_upstream_block(origin_server_name=origin_server_name, server_ip_port=server_ip_port)
            self.nc.add_location_transmit(origin_server_name=origin_server_name, header_key=header_key)
            print(self.nc.data)
            self.nc.savef(path)
        except Exception as e:
            print(e)

    @staticmethod
    def reload_nginx(root_pwd):
        import subprocess
        cmd = "echo '{}' | sudo -S nginx -s reload".format(root_pwd)
        subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    path = "/usr/local/etc/nginx/nginx.conf"

    mn = ModifyNginxConfig(conf_path=path)
    mn.add_transmit_rule(origin_server_name="test5005", server_ip_port="127.0.0.1:5005", header_key="5005")
    mn.reload_nginx("tianjian321")

#!/usr/bin/env python

import argparse
import os
import sys
import yaml
from jinja2 import Environment, PackageLoader, select_autoescape

class AnsibleManager:
    def __init__(self, entrypoint, hosts, datastore, manager):
        self.entrypoint = entrypoint
        self.hosts = hosts.split(',')
        self.roles = [
            datastore,
            manager
        ]
        self.conf = None
        self.jinja_env = Environment(
            loader=PackageLoader(),
            autoescape=select_autoescape(['yaml'])
        )

    def load(self):
        template = self.env.get_template(self.entrypoint)
        data = template.render(host=self.hosts, roles=self.roles)
        self.conf = yaml.load(data)


def main():
    pwd = os.path.dirname(os.path.realpath(__file__))
    
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--hosts', type=str, help='a comma separated list of hosts to provision')
    parser.add_argument('--datastore', type=str, help='the datastore to setup for maestro use')
    parser.add_argument('--manager', type=str, help='the manager runtime for maestro use')
    parser.add_argument('--entrypoint', type=str, default="{}/main.yml".format(pwd), help='path to ansible entrypoint')
    args = parser.parse_args(sys.argv[1:])

    mgr = AnsibleManager(args.entrypoint, args.hosts, args.datastore, args.manager)
    mgr.load()

if __name__ == '__main__':
    main()

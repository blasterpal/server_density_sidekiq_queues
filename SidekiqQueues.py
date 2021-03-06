#!/usr/bin/env python

import re
import commands

REDIS_AVAIL = int(commands.getoutput("type redis-cli > /dev/null 2>&1 ; echo $?")) == 0

class SidekiqQueues:
    def __init__(self, agent_config, checks_logger, raw_config):
        self.agent_config = agent_config
        self.checks_logger = checks_logger
        self.raw_config = raw_config

        if self.agent_config is None:
            self.set_default_config()

        if ('Sidekiq' not in self.agent_config):
            self.set_default_config()

    def set_default_config(self):
        self.agent_config = {}
        self.agent_config['Sidekiq'] = {'namespace': 'sidekiq'}

    def run(self):
        stats = {}
        #only run redis-cli commands on servers that have it.
        if REDIS_AVAIL:
            namespace = self.agent_config['Sidekiq']['namespace']
            command = "redis-cli --raw llen %(namespace)s:queue:" % locals()
            for queue in commands.getoutput(command).splitlines():
                stats[queue] = int(commands.getoutput(command+queue))
        return stats

if __name__ == '__main__':
    sidekiq = SidekiqQueues(None, None, None)
    print sidekiq.run()


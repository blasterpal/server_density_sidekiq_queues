SidekiqQueues
=============================

[Sidekiq](https://github.com/mperham/sidekiq) plugin for ServerDensity to show queue sizes. 

#Metrics

The plugin will report one metric per queue in Sidekiq.

##Assumptions

* Requires redis-cli in PATH.
* Presumes installation on the primary Redis server.
* Only tested for Linux.

##Installation

Copy `SidekiqQueues.py` plugin to your `sd-agent` plugins folder (`/usr/bin/sd-agent/plugins`). Create the plugins folder if it doesn't exist.


#Thanks
Drew configuration inspiration from https://github.com/justincase/sd-beanstalkd/blob/master/Beanstalkd.py.

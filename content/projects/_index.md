---
title: Projects
layout: single
---

A selection of things I've built, maintained, contributed to, or helped bring
into the world.

## Open source

### [NAPALM](https://github.com/napalm-automation/napalm)

**Network Automation and Programmability Abstraction Layer with Multivendor
support**

NAPALM is a Python library that provides a unified API for interacting with
network devices from different vendors. I was one of the early contributors and
maintainers, alongside David Barroso, Kirk Byers, Elisa Jasinska, and many
others.

[GitHub →](https://github.com/napalm-automation/napalm)

### [napalm-logs](https://github.com/napalm-automation/napalm-logs)

A Python library for turning network syslog messages into structured data using
OpenConfig and IETF YANG models. I worked on the project as part of the
NAPALM community, with the goal of making network events useful to automation
systems rather than just something humans read in a terminal.

[GitHub →](https://github.com/napalm-automation/napalm-logs)

### [salt-sproxy](https://github.com/mirceaulinic/salt-sproxy)

A Salt plugin for managing network devices and other programmable systems at
scale without running a Proxy Minion for every device.

It grew out of a fairly practical problem: Salt was a powerful automation
engine, but running thousands of long-lived Proxy Minion processes was not
particularly attractive. `salt-sproxy` kept the Salt model while changing how
those devices were managed.

[GitHub →](https://github.com/mirceaulinic/salt-sproxy) · [Documentation →](https://salt-sproxy.readthedocs.io/)

### [ISalt](https://github.com/mirceaulinic/isalt)

An IPython-style interactive console for debugging and developing Salt code. It
makes Salt's otherwise contextual dunder variables available interactively,
which makes it much easier to experiment with execution modules, runners,
grains, pillars, proxy devices, and other Salt internals.

[GitHub →](https://github.com/mirceaulinic/isalt) · [Documentation →](https://isalt.readthedocs.io/)

### [latency-monitor](https://github.com/mirceaulinic/latency-monitor)

A lightweight TCP and UDP latency monitoring tool with pluggable metrics
backends.

It measures one-way and round-trip latency, supports high-frequency probing,
and can publish measurements to systems such as Datadog, ClickHouse, ZeroMQ,
and Pushgateway. This is one of my more recent projects and a good example of
the kind of small tool I like building when existing monitoring systems don't
quite fit the problem.

[GitHub →](https://github.com/mirceaulinic/latency-monitor)

### NAPALM-Salt

I also contributed to the Salt integration around NAPALM, including modules for
using NAPALM within Salt for event-driven network automation and orchestration.
The Salt modules for NAPALM were eventually fully integrated beginning with Salt
release [2016.11.0 Codename 
Carbon](https://docs.saltproject.io/en/3008/topics/releases/2016.11.0.html#network-automation-napalm).

[GitHub →](https://github.com/napalm-automation/napalm-salt)

## Books & publications

### [Network Automation at Scale](https://www.oreilly.com/library/view/network-automation-at/9781491992524/)

A short O'Reilly book I co-authored with Seth House in 2017. It covers using
Salt and NAPALM for network automation, including Salt architecture, Proxy
Minions, Jinja and YAML, configuration management, event-driven automation,
orchestration, and more.

The book is intentionally practical and still available
[online](https://www.cloudflare.com/resources/assets/slt3lc6tev37/2UixizjqVh3v7L9yhcJWMT/87c1175735d490221147e1ad5866d909/network-automation-at-scale.pdf)

### [Network Programmability and Automation](https://www.oreilly.com/library/view/network-programmability-and/9781491931240/)

I contributed the **SaltStack section** to the first edition of this O'Reilly
book, covering Salt's architecture, network configuration management, remote
execution, and its event-driven capabilities.

This was one of the earlier opportunities I had to help document network
automation for a broader audience, and it was a fun book to be involved with.

## Training

### [APNIC Network Automation Course](https://mirceaulinic.net/2024-04-11-apnic-network-automation/)

I worked with APNIC on the development of its network automation course, from
the early discussions and course design through building the training
environment and preparing the material.

The course eventually became a hands-on, multi-day workshop covering much more
than configuration management: NAPALM, `napalm-logs`, Salt, Prometheus,
Alertmanager, Grafana, Elasticsearch/Kibana, NetBox, TextFSM, and
event-driven automation. The training environment itself was a fairly
substantial virtualised multi-vendor lab.

The first delivery was at APRICOT 2024 in Bangkok, after several years of
preparation.

[About the course →](https://mirceaulinic.net/2024-04-11-apnic-network-automation/) · [APNIC Academy →](https://academy.apnic.net/en/catalog/network-automation-5days)

## More

There are plenty of smaller experiments, prototypes, talks, and contributions
that don't deserve their own entry here. My
[GitHub profile](https://github.com/mirceaulinic) is probably the best place to
find those.

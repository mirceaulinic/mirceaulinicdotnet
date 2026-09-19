---
title: Talks
layout: single
---

A selection of talks, tutorials, panels, and workshops I've given over the years.
Where a recording or slide deck is publicly available, I've included it.

## 2024

### AutoCon 2 — Closing Keynote
**Network Automation Forum · Denver, US · 22 November 2024**

I closed AutoCon 2 with a keynote covering DigitalOcean's approach to network
automation, including the tooling and architecture used around NetBox, Peering
Manager, IRRd, Salt, Prometheus, and event-driven orchestration.

The tooling was only part of the story I wanted to tell. The bigger point was
how dramatically the network is changing as infrastructure becomes more dynamic
and deployments happen at an entirely different scale. With GPU deployments
ramping up and new infrastructure being built and rebuilt so frequently, the old
model of manually configuring and operating networks simply doesn't work anymore.

We have reached a point where automation isn't just about making engineers more
efficient or eliminating repetitive work: it's fundamental to being able to
operate the network at all. The way we used to do networking is changing, and
there's really no going back. I was very sick, but I hope I managed to convey
this message.

[Video →](https://www.youtube.com/watch?v=Jf2-_2n8yDI) · [Conference →](https://networkautomation.forum/autocon2)

## 2020

### Managing Networks and Applications Using Salt, Without Minions
**SaltConf20 · 29 October 2020**

A practical look at Salt SProxy and using Salt to manage network infrastructure
without running a Proxy Minion for every device.

[Slides →](https://speakerdeck.com/mirceaulinic/saltconf20-managing-networks-and-applications-using-salt-without-minions)

### Automating Networks Using Salt, Without Running Proxy Minions
**iNOG::14v · Dublin / online · 17 April 2020**

One of the first fully virtual iNOG events, during which I gave a talk about
Salt SProxy and managing network infrastructure without running Proxy Minions.

[Event →](https://inog.net/)

## 2019

### A (Proxy) Minion-less Approach to Network Automation using Salt
**RIPE 79 · Rotterdam, Netherlands · October 2019**

A deeper look at `salt-sproxy`: why traditional Proxy Minions can become
operationally expensive at scale, and how the Super Proxy approach changes the
model.

[Video →](https://ripe79.ripe.net/archives/video/231) · [Related article →](https://mirceaulinic.net/2019-06-17-minionless-salt-automation/)

### Extending Salt's Capabilities for Event-Driven Network Automation and Orchestration
**NANOG 76 · Washington, DC · June 2019**

A tutorial on extending Salt with custom execution modules and using those
extensions for network automation and event-driven orchestration.

[Slides →](https://pc.nanog.org/static/published/meetings/NANOG76/1982/20190612_Ulinic_Extending_Salt_S_Capabilities_v1.pdf) · [Speaker Deck →](https://speakerdeck.com/mirceaulinic/nanog-76-extending-salts-capabilities-for-event-driven-network-automation-and-orchestration)

### Technical Debt: an Anycast Story
**APRICOT 2019 · Daejeon, South Korea · February 2019**

A case study of Cloudflare's anycast network and the process of removing old
routing configuration safely across a large global network.

[Slides →](https://www.slideshare.net/slideshow/technical-debt-an-anycast-story/134791020)

### Event-driven Network Automation and Orchestration
**APRICOT 2019 · Daejeon, South Korea · February 2019**

A hands-on tutorial covering Salt, NAPALM, YANG, `napalm-logs`, and event-driven
automation. The accompanying lab was published as a GitHub repository so
participants could reproduce the setup themselves.

[Slides →](https://2019.apricot.net/assets/files/APKS756/event-driven-network-automation-and-orchestration.pdf) · [SlideShare →](https://www.slideshare.net/slideshow/eventdriven-network-automation-and-orchestration/133629821) · [Lab →](https://github.com/mirceaulinic/apricot2019-tutorial)

### Three Years of Automating Large Scale Networks Using Salt
**Config Management Camp 2019 · Gent, Belgium · 5 February 2019**

A look back at Cloudflare's first three years of using Salt for network
automation, the open-source components that came out of the work, and where the
platform was heading.

[Event →](https://cfgmgmtcamp.org/ghent2019/schedule/tuesday/saltscaling/)

## 2018

### Three Years of Automating Large Scale Networks Using Salt
**RIPE 77 · Amsterdam, Netherlands · 18 October 2018**

The RIPE Open Source Working Group presentation covering the evolution of
Cloudflare's Salt-based automation and the wider ecosystem around NAPALM,
NetBox, `napalm-logs`, and other tools.

[Slides →](https://ripe77.ripe.net/wp-content/uploads/presentations/113-RIPE77_Three_years_of_automating_large-scale_networks_using_Salt-Mircea_Ulinic.pdf) · [RIPE archive →](https://ripe77.ripe.net/archives/)

### Event-driven Network Automation and Orchestration
**RIPE 76 · Marseille, France · 14 May 2018**

A hands-on tutorial on using Salt and NAPALM for cross-platform configuration
management and event-driven network automation.

[Slides →](https://ripe76.ripe.net/presentations/17-RIPE76_-Event-driven-network-automation-and-orchestration.pdf) · [Tutorial →](https://ripe76.ripe.net/programme/meeting-plan/tutorials/)

### Event-driven Network Automation and Orchestration
**UKNOF 40 · Manchester, UK · 27 April 2018**

A joint presentation with Tom Strickx on combining Salt Proxy Minions and NAPALM
for vendor-agnostic automation and reacting to network events.

[Video →](https://youtu.be/axwgvcU-N5A) · [Event & slides →](https://indico.uknof.org.uk/event/42/contributions/549/)

### Event-driven Network Configuration Management Using Salt
**Config Management Camp 2018 · Gent, Belgium · 5 February 2018**

A talk about using Salt and NAPALM to bring configuration management and
event-driven automation to network devices.

[Slides →](https://speakerdeck.com/mirceaulinic/event-driven-network-configuration-management-using-salt) · [Event →](https://cfgmgmtcamp.org/ghent2018/schedule/salt/network)

## 2017

### Orchestration with Network Devices: Challenges and Solutions
**SaltConf17 · Salt Lake City, US · 2 November 2017**

A look at the challenges of orchestrating network devices and combining Salt
with NAPALM for cross-vendor network automation.

[Slides →](https://speakerdeck.com/mirceaulinic/saltconf-2017-orchestration-with-network-devices-challenges-and-solutions) · [PDF →](https://eventmobi.com/api/events/20058/documents/download/70dfc2fa-2215-468c-b3b4-882b63e76679.pdf/as/Saltconf_2017_Orchestration_with_network_devices_challenges_and_solutions_Mircea_Ulinic_Cloudflare.pdf)

### NetDevOps: DevOps in Networking: Challenges and Solutions
**Hackference 2017 · Birmingham, UK · 20 October 2017**

An introduction to the practical side of NetDevOps, including NAPALM, Salt, and
a real-world network orchestration example.

[Slides →](https://speakerdeck.com/mirceaulinic/netdevops-devops-in-networking-challenges-and-solutions)

### Network Automation Panel: Past, Present and Future
**NANOG 71 · San Jose, US · October 2017**

A panel with Kirk Byers, David Barroso, Jeremy Stretch and Jathan McCollum,
covering the evolution of network automation, NAPALM, IPAM/source-of-truth
systems, and event-driven automation.

[Slides →](https://speakerdeck.com/mirceaulinic/network-automation-panel-past-present-and-future)

### Managing Network Devices Like Servers
**NANOG 71 · San Jose, US · 4 October 2017**

A lightning talk about managing network platforms that can run custom software
(e.g., Arista EOS, Cumulus OS, etc.) using approaches traditionally associated
with server automation.

[Slides →](https://speakerdeck.com/mirceaulinic/managing-network-devices-like-servers)

### Event-driven Network Automation and Orchestration
**London Network Automation Meetup · London, UK · 21 September 2017**

A practical introduction to designing network automation systems, choosing the
right tools, and using Salt for event-driven orchestration.

[Slides →](https://speakerdeck.com/mirceaulinic/event-driven-network-automation-and-orchestration)

### Network Automation at Scale: Up and Running in 60 Minutes
**RIPE 74 · Budapest, Hungary · 8 May 2017**

A step-by-step tutorial covering the tooling and workflow needed to get started
with large-scale network automation.

[Slides →](https://ripe74.ripe.net/presentations/18-RIPE-74-Network-automation-at-scale-up-and-running-in-60-minutes.pdf) · [Speaker Deck →](https://speakerdeck.com/mirceaulinic/network-automation-at-scale-up-and-running-in-60-minutes-2)

### Network Automation at Scale: Up and Running in 60 Minutes
**NANOG 69 · Washington, DC · February 2017**

An introductory tutorial based on the automation stack used at Cloudflare at
the time.

[Video →](https://www.youtube.com/watch?v=99jHvkVM0Dk) · [Slides →](https://www.nanog.org/sites/default/files/1_Ulinic_Network_Automation_At_v1.pdf) · [Speaker Deck →](https://speakerdeck.com/mirceaulinic/network-automation-at-scale-up-and-running-in-60-minutes-1)

## 2016

### Network Automation with Salt and NAPALM
**NANOG 68 · Dallas, US · 17 October 2016**

A talk about using Salt and NAPALM to automate network operations at scale,
including configuration management and orchestration.

[Video →](https://www.youtube.com/watch?v=gV2918bH5_c) · [Recorded demo →](https://www.youtube.com/watch?v=AqBk5fM7qZ0) · [Slides →](https://www.nanog.org/sites/default/files/NANOG68%20Network%20Automation%20with%20Salt%20and%20NAPALM%20Mircea%20Ulinic%20Cloudflare%20(1).pdf) · [Speaker Deck →](https://speakerdeck.com/mirceaulinic/network-automation-with-salt-and-napalm)

### Network Automation with Salt and NAPALM
**RIPE 72 · Copenhagen, Denmark · 24 May 2016**

One of my earlier public talks about NAPALM and Salt, covering vendor-agnostic
network automation and the motivation for bringing DevOps-style approaches to
networking.

[Video →](https://ripe72.ripe.net/archives/video/121/) · [Slides →](https://ripe72.ripe.net/wp-content/uploads/presentations/58-RIPE72-Network-Automation-with-Salt-and-NAPALM-Mircea-Ulinic-CloudFlare.pdf)

# OWASP IoT Top 10 – 2018

* **I01:2018 - Weak, Guessable, or Hardcoded Passwords**\
    Use of easily brute forced, publicly available, or unchangeable credentials, 
    including backdoors in firmware or client software that grants unauthorized 
    access to deployed systems.

* **I02:2018 - Insecure Network Services**\
    Unneeded or insecure network services running on the device itself, especially 
    those exposed to the internet, that compromise the confidentiality,
    integrity/authenticity, or availability of information or allow unauthorized
    remote control.

* **I03:2018 - Insecure Ecosystem Interfaces**\
    Insecure web, backend API, cloud, or mobile interfaces in the ecosystem
    outside of the device that allows compromise of the device or its related
    components. Common issues include a lack of authentication/authorization, 
    lacking or weak encryption, and a lack of input and output filtering.

* **I04:2018 - Lack of Secure Update Mechanism**\
    Lack of ability to securely update the device. This includes lack of firmware 
    validation on device, lack of secure delivery (un-encrypted in transit), 
    lack of anti-rollback mechanisms, and lack of notifications of security 
    changes due to updates.

* **I05:2018 - Use of Insecure or Outdated Components**\
    Use of deprecated or insecure software components/libraries that could allow 
    the device to be compromised. This includes insecure customization of
    operating system platforms, and the use of third-party software or hardware 
    components from a compromised supply chain.

* **I06:2018 - Insufficient Privacy Protection**\
    User’s personal information stored on the device or in the ecosystem that is 
    used insecurely, improperly, or without permission.

* **I07:2018 - Insecure Data Transfer and Storage**\
    Lack of encryption or access control of sensitive data anywhere within the 
    ecosystem, including at rest, in transit, or during processing.

* **I08:2018 - Lack of Device Management**\
    Lack of security support on devices deployed in production, including asset 
    management, update management, secure decommissioning, systems monitoring, 
    and response capabilities.

* **I09:2018 - Insecure Default Settings**\
    Devices or systems shipped with insecure default settings or lack the ability 
    to make the system more secure by restricting operators from modifying
    configurations.

* **I10:2018 Lack of Physical Hardening**\
    Lack of physical hardening measures, allowing potential attackers to gain 
    sensitive information that can help in a future remote attack or take local 
    control of the device.


## References

* [OWASP Internet of Things Project](https://wiki.owasp.org/index.php/OWASP_Internet_of_Things_Project#tab=IoT_Top_10)

*Egon Teiniker, 2020-2023, GPL v3.0*	
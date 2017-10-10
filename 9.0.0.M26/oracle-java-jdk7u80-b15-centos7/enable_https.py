#!/usr/bin/env python2

import os, sys
import xml.etree.ElementTree as ET

CATALINA_HOME = os.environ.get('CATALINA_HOME')

SSL_HOSTNAME = os.environ.get('SSL_HOSTNAME')
HTTPS_PORT = os.environ.get('HTTPS_PORT', '8443')
HTTPS_KEYSTORE_PATH = os.environ.get('HTTPS_KEYSTORE_PATH')
HTTPS_KEYSTORE_PASS = os.environ.get('HTTPS_KEYSTORE_PASS')
HTTPS_KEYSTORE_ALIAS = os.environ.get('HTTPS_KEYSTORE_ALIAS')
HTTPS_TRUSTSTORE_PATH = os.environ.get('HTTPS_TRUSTSTORE_PATH')
HTTPS_TRUSTSTORE_PASS = os.environ.get('HTTPS_TRUSTSTORE_PASS')
HTTPS_CRT_PATH = os.environ.get('HTTPS_CRT_PATH')
HTTPS_KEY_PATH = os.environ.get('HTTPS_KEY_PATH')
HTTPS_KEY_PASS = os.environ.get('HTTPS_KEY_PASS')
HTTPS_CA_CRT_PATH = os.environ.get('HTTPS_CA_CRT_PATH')
USE_APR = os.environ.get('USE_APR')


if CATALINA_HOME is None or CATALINA_HOME == '':
    print("CATALINA_HOME is not defined")
    sys.exit(1)

server_xml_path = os.path.join(CATALINA_HOME, 'conf/server.xml')
server_xml_doc = ET.parse(server_xml_path)

catalina_service_elem = server_xml_doc.findall(".//Service[@name='Catalina']")

if USE_APR:
    protocol = 'org.apache.coyote.http11.Http11AprProtocol'
else:
    protocol = 'org.apache.coyote.http11.Http11NioProtocol'

https_connector_attributes = {'port': HTTPS_PORT,
                              'protocol': protocol,
                              'maxThreads': '150',
                              'SSLEnabled': 'true',
                              'scheme': 'https',
                              'secure': 'true'}

https_connector_elem = ET.Element('Connector', attrib=https_connector_attributes)

if HTTPS_TRUSTSTORE_PATH is not None:
    ssl_host_config_attributes = {
        'hostName': SSL_HOSTNAME,
        'truststoreFile': HTTPS_TRUSTSTORE_PATH,
        'truststorePassword': HTTPS_TRUSTSTORE_PASS
    }
    ssl_host_config_attributes = {k: v for k, v in ssl_host_config_attributes.items() if v}
else:
    ssl_host_config_attributes = None

ssl_host_config_elem = ET.SubElement(https_connector_elem, 'SSLHostConfig', attrib=ssl_host_config_attributes)

certificate_elem_attributes = {'certificateFile': HTTPS_CRT_PATH,
                               'certificateChainFile': HTTPS_CA_CRT_PATH,
                               'certificateKeyAlias': HTTPS_KEYSTORE_ALIAS,
                               'certificateKeyFile': HTTPS_KEY_PATH,
                               'certificateKeyPassword': HTTPS_KEY_PASS,
                               'certificateKeystoreFile': HTTPS_KEYSTORE_PATH,
                               'certificateKeystorePassword': HTTPS_KEYSTORE_PASS,
                               'type': 'RSA'}

certificate_elem_attributes = {k: v for k, v in certificate_elem_attributes.items() if v}

certificate_elem = ET.SubElement(ssl_host_config_elem, 'Certificate',
                                 attrib=certificate_elem_attributes)

catalina_service_elem.insert(1, https_connector_elem)
server_xml_doc.write()

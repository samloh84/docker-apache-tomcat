FROM samloh84/oracle-java-jdk:8u144-b01-centos7
ARG VENDOR=apache
ARG PRODUCT=tomcat
ARG PRODUCT_VERSION=9.0.0.M26
ARG TEMP_DIR_ROOT=/tmp/${VENDOR}-${PRODUCT}
ARG TEMP_DIR=/${TEMP_DIR_ROOT}/${PRODUCT_VERSION}
ARG INSTALL_DIR_ROOT=/opt/${VENDOR}-${PRODUCT}
ARG INSTALL_DIR=${INSTALL_DIR_ROOT}/${PRODUCT_VERSION}

ARG APACHE_TOMCAT_BINARIES_URL="http://www-eu.apache.org/dist/tomcat/tomcat-9/v9.0.0.M26/bin/apache-tomcat-9.0.0.M26.tar.gz"
ARG APACHE_TOMCAT_BINARIES="apache-tomcat-9.0.0.M26.tar.gz"
ARG APACHE_TOMCAT_GPG_KEYS_URL=http://www-eu.apache.org/dist/tomcat/tomcat-9/v9.0.0.M26/KEYS
ARG APACHE_TOMCAT_GPG_KEYS=KEYS
ARG APACHE_TOMCAT_SIGNATURE_URL="http://www-eu.apache.org/dist/tomcat/tomcat-9/v9.0.0.M26/bin/apache-tomcat-9.0.0.M26.tar.gz.asc"
ARG APACHE_TOMCAT_SIGNATURE="apache-tomcat-9.0.0.M26.tar.gz.asc"

USER ${ROOT_UID}

RUN \
mkdir -p ${TEMP_DIR} ${INSTALL_DIR} && \
cd ${TEMP_DIR} && \
curl -LjSs ${APACHE_TOMCAT_BINARIES_URL} -o ${APACHE_TOMCAT_BINARIES} && \
curl -LjSs ${APACHE_TOMCAT_GPG_KEYS_URL} -o ${APACHE_TOMCAT_GPG_KEYS} && \
curl -LjSs ${APACHE_TOMCAT_SIGNATURE_URL} -o ${APACHE_TOMCAT_SIGNATURE} && \
gpg --import ${APACHE_TOMCAT_GPG_KEYS} && \
curl -LjSs ${APACHE_TOMCAT_SIGNATURE_URL} -o ${APACHE_TOMCAT_SIGNATURE} && \
gpg --verify ${APACHE_TOMCAT_SIGNATURE} && \
tar -xf ${APACHE_TOMCAT_BINARIES} --strip-components=1 -C ${INSTALL_DIR} && \
fix-ownership ${INSTALL_DIR} && \
fix-permissions ${INSTALL_DIR} && \
rm -rf ${TEMP_DIR_ROOT}

ENV CATALINA_HOME ${INSTALL_DIR}
ENV PATH ${CATALINA_HOME}/bin:${PATH}

USER ${APP_UID}

WORKDIR ${CATALINA_HOME}

EXPOSE 8080
EXPOSE 8443

CMD ${CATALINA_HOME}/bin/catalina.sh run
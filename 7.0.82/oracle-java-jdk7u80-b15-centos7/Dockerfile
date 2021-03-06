FROM samloh84/oracle-java-jdk:7u80-b15-centos7
ARG VENDOR=apache
ARG PRODUCT=tomcat
ARG PRODUCT_VERSION=7.0.82
ARG TEMP_DIR_ROOT=/tmp/${VENDOR}-${PRODUCT}
ARG TEMP_DIR=/${TEMP_DIR_ROOT}/${PRODUCT_VERSION}
ARG INSTALL_DIR_ROOT=/opt/${VENDOR}-${PRODUCT}
ARG INSTALL_DIR=${INSTALL_DIR_ROOT}/${PRODUCT_VERSION}

ARG APACHE_TOMCAT_BINARIES_URL="http://www.apache.org/dist/tomcat/tomcat-7/v7.0.82/bin/apache-tomcat-7.0.82.tar.gz"
ARG APACHE_TOMCAT_BINARIES="apache-tomcat-7.0.82.tar.gz"
ARG APACHE_TOMCAT_GPG_KEYS_URL=http://www.apache.org/dist/tomcat/tomcat-7/v7.0.82/KEYS
ARG APACHE_TOMCAT_GPG_KEYS=KEYS
ARG APACHE_TOMCAT_SIGNATURE_URL="http://www.apache.org/dist/tomcat/tomcat-7/v7.0.82/bin/apache-tomcat-7.0.82.tar.gz.asc"
ARG APACHE_TOMCAT_SIGNATURE="apache-tomcat-7.0.82.tar.gz.asc"


ARG APACHE_PORTABLE_RUNTIME_URL="http://www-eu.apache.org/dist/apr/apr-1.6.3.tar.gz"
ARG APACHE_PORTABLE_RUNTIME="apr-1.6.3.tar.gz"
ARG APACHE_PORTABLE_RUNTIME_GPG_KEYS_URL="https://people.apache.org/keys/group/apr.asc"
ARG APACHE_PORTABLE_RUNTIME_GPG_KEYS=apr.asc
ARG APACHE_PORTABLE_RUNTIME_SIGNATURE_URL="http://www.apache.org/dist/apr/apr-1.6.3.tar.gz.asc"
ARG APACHE_PORTABLE_RUNTIME_SIGNATURE="apr-1.6.3.tar.gz.asc"

USER ${ROOT_UID}

RUN \
mkdir -p ${TEMP_DIR} ${INSTALL_DIR} && \
cd ${TEMP_DIR} && \
curl -LjSs ${APACHE_PORTABLE_RUNTIME_URL} -o ${APACHE_PORTABLE_RUNTIME} && \
curl -LjSs ${APACHE_PORTABLE_RUNTIME_GPG_KEYS_URL} -o ${APACHE_PORTABLE_RUNTIME_GPG_KEYS} && \
gpg --import ${APACHE_PORTABLE_RUNTIME_GPG_KEYS} && \
curl -LjSs ${APACHE_PORTABLE_RUNTIME_SIGNATURE_URL} -o ${APACHE_PORTABLE_RUNTIME_SIGNATURE} && \
gpg --verify ${APACHE_PORTABLE_RUNTIME_SIGNATURE} && \
mkdir -p ${TEMP_DIR}/apr && \
tar -xf ${APACHE_PORTABLE_RUNTIME} --strip-components=1 -C ${TEMP_DIR}/apr && \
pushd ${TEMP_DIR}/apr && \
yum install -y autoconf libtool gcc-c++ make && \
./configure && \
make && \
make install && \
yum remove -y autoconf libtool gcc-c++ make && \
yum clean all && \
popd && \
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
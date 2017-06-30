FROM samloh84/oracle-jre:8u131-centos7

ARG VENDOR=apache
ARG PRODUCT=tomcat
ARG PRODUCT_VERSION=8.5.15
ARG TEMP_DIR_ROOT=/tmp/${VENDOR}-${PRODUCT}
ARG TEMP_DIR=${TEMP_DIR_ROOT}/${PRODUCT_VERSION}
ARG INSTALL_DIR_ROOT=/opt/${VENDOR}-${PRODUCT}
ARG INSTALL_DIR=${INSTALL_DIR_ROOT}/${PRODUCT_VERSION}

ARG TOMCAT_INSTALL_TAR_GZ_URL="http://www-eu.apache.org/dist/tomcat/tomcat-8/v8.5.15/bin/apache-tomcat-8.5.15.tar.gz"
ARG TOMCAT_INSTALL_TAR_GZ=apache-tomcat-8.5.15.tar.gz
ARG TOMCAT_INSTALL_TAR_GZ_SHA1SUM=67650d6deda0c0ba9e8c7db7fe4006c35d6dc7db

ARG TOMCAT_KEYS_URL="https://www.apache.org/dist/tomcat/tomcat-8/KEYS"
ARG TOMCAT_INSTALL_TAR_GZ_ASC_URL="https://www.apache.org/dist/tomcat/tomcat-8/v8.5.15/bin/apache-tomcat-8.5.15.tar.gz.asc"
ARG TOMCAT_INSTALL_TAR_GZ_ASC=apache-tomcat-8.5.15.tar.gz.asc

USER ${ROOT_UID}

RUN \
mkdir -p ${TEMP_DIR} && \
mkdir -p ${INSTALL_DIR} && \
pushd ${TEMP_DIR} && \
curl -LjSs ${TOMCAT_KEYS_URL} -o KEYS && \
curl -LjSs ${TOMCAT_INSTALL_TAR_GZ_ASC_URL} -o ${TOMCAT_INSTALL_TAR_GZ_ASC} && \
curl -LjSs ${TOMCAT_INSTALL_TAR_GZ_URL} -o ${TOMCAT_INSTALL_TAR_GZ} && \
gpg --import ./KEYS && \
gpg --verify ${TOMCAT_INSTALL_TAR_GZ_ASC} ${TOMCAT_INSTALL_TAR_GZ} && \
echo "${TOMCAT_INSTALL_TAR_GZ_SHA1SUM}  ${TOMCAT_INSTALL_TAR_GZ}" | sha1sum -c - && \
tar -xzf ${TEMP_DIR}/${TOMCAT_INSTALL_TAR_GZ} --strip-components=1 -C ${INSTALL_DIR} && \
fix-ownership ${INSTALL_DIR} && \
fix-permissions ${INSTALL_DIR} && \
popd && \
rm -rf ${TEMP_DIR_ROOT}


ENV CATALINA_HOME ${INSTALL_DIR}
ENV PATH ${CATALINA_HOME}/bin:${PATH}

USER ${APP_UID}

EXPOSE 8080
EXPOSE 8443

WORKDIR ${CATALINA_HOME}

CMD ${CATALINA_HOME}/bin/catalina.sh start

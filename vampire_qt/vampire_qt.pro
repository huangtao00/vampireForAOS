TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle
CONFIG -= qt

SOURCES +=
INCLUDEPATH += $$PWD/../vampire/hdr
INCLUDEPATH += $$PWD/../vampire/src/ltmp
INCLUDEPATH += $$PWD/../vampire/src/qvoronoi

include(deployment.pri)
qtcAddDeployment()


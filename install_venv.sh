#! /bin/bash
#
# install_venv.sh
#
# Copyright © 2014 Mathieu Gaborit (matael) <mathieu@matael.org>
#
#
# Distributed under WTFPL terms
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.
#

CORE_2_USE=2

PYTHON278_URL=https://www.python.org/ftp/python/2.7.8/Python-2.7.8.tgz
LOCALPYTHON=.localpython
PYTHON_DIRNAME=Python-2.7.8

VENV_DIR=.venv_pelican
INIT_PATH="$PWD"

echo "==> Testing for virtualenv..."
# test for virtualenv disponibility
virtualenv /tmp/test_venv_$PPID || ( echo "Please install virtualenv (sudo apt-get install python-virtualenv on Debian-based Linux)" ; exit )
rm -rf /tmp/test_venv_$PPID

echo "==> Creating dir $LOCALPYTHON to setup a new python install..."
mkdir $LOCALPYTHON

echo "==> Downloading and unpacking python_2.7.8..."
mkdir /tmp/python_$PPID && cd /tmp/python_$PPID
wget $PYTHON278_URL --quiet -O - | tar zx
cd $PYTHON_DIRNAME
echo "... Done."

echo "==> Running ./configure..."
./configure --prefix $INIT_PATH/$LOCALPYTHON

echo "==> Running make..."
make -j $CORE_2_USE PREFIX=$INIT_PATH/$LOCALPYTHON
make install

cd $INIT_PATH
echo "==> Creating bare virtualenv in $VENV_DIR ..."
virtualenv --python=$LOCALPYTHON/bin/python $VENV_DIR

echo "==> Activating venv..."
source $VENV_DIR/bin/activate

echo "==> Installing requirements..."
pip install  -r requirements.txt

echo "==> Deactivating venv..."
deactivate

#!/bin/bash

# set -x

which pip &> /dev/null
if [[ $? -ne 0 ]]; then
  sudo apt install -y python-pip -q
fi

which virtualenv &> /dev/null
if [[ $? -ne 0 ]]; then
  sudo pip install virtualenv
fi

virtualenv ./
source bin/activate
pip install -r requirements.txt

echo
echo '------------------------------------------------------------'
echo "Now run"
echo "  > source bin/activate"

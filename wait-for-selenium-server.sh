#!/bin/bash
until [[ $(docker logs testchrome 2>/dev/null | grep -c "Selenium Server is up and running") -ge 1 ]]; do
  if [[ ${COUNTER} -gt 10 ]]; then
    echo
    echo "Took too long to start Selenium server."
    break
  fi
  echo -n "."
  sleep 1
  let COUNTER=COUNTER+1
done

#!/usr/bin/env bash
session_engines=(
"django.contrib.sessions.backends.db"
"django.contrib.sessions.backends.file"
"django.contrib.sessions.backends.cache"
"django.contrib.sessions.backends.cached_db"
"django.contrib.sessions.backends.signed_cookies"
)

for session in "${session_engines[@]}"
do
    export SESSION_ENGINE=$session
    tox -- --driver=Chrome
    tox -- --driver=Firefox --liveserver=127.0.0.1
done

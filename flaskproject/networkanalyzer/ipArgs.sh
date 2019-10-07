#!/bin/sh
ifconfig en0 | grep netmask | tee IPinfo.txt

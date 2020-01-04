#!/bin/bash

wg genkey | tee privatekey | wg pubkey > publickey \
       && chmod 600 privatekey


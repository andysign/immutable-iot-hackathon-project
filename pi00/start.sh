#!/bin/bash
pinum=00
datadir=data${pinum}/
networkid=20200727
pwd=123
GETH=""
if [ "$(uname)" == "Darwin" ]; then
GETH="geth-darwin";
elif [ "$(uname)" == "Linux" ]; then
    if [ "$(uname -m)" == "armv7l" ]; then
        GETH="geth"
    else
        GETH="geth-linux"
    fi;
fi
./$GETH version
./$GETH --datadir ${datadir} --nodiscover --networkid ${networkid} \
    --unlock 0 --password <(echo ${pwd}) --allow-insecure-unlock \
    --rpc --rpcapi eth,net,web3 --identity $(uname -n) \
    --syncmode full  --rpccorsdomain "*" console

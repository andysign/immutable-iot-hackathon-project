#!/bin/bash
pinum=02
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
rm ../log
./$GETH --datadir ${datadir} --nodiscover --networkid ${networkid} \
    --unlock 0 --password <(echo ${pwd}) --allow-insecure-unlock \
    --rpc --rpcaddr 0.0.0.0 --rpcapi eth,net,web3 --mine \
    --rpccorsdomain "*" --identity $(uname -n) --syncmode full \
    --lightkdf $1 2>&1 | tee -a $HOME/log

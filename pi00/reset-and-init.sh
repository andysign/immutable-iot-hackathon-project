#!/bin/bash
pinum=00
datadir=data${pinum}/
privkey=6b256f8f0dfbe6a57d41a68d135eb3db348df035679f6c6c10d8b87f73cf59c0 # 0x010394e95E108465E438fd0af870f44ca47B87dF
nodekey=d4c84815715e96ce2cd168292f5f4ac9936b7c9a87216e2d21e7fed8386e7f98 # 010516a6e3acd95b9cf69c39d1d799d3e9fb8bef76e4c53bc1b92753a73b03e2e1222119365508dbb2faf18b365d2d42c86a4d748b6a8a7d1fa11592afb55ac5
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
# Reset everything
rm -rf data${pinum}/*
# Init Chain
./$GETH --datadir ${datadir} init genesis_clique.json
# Build account
./$GETH --datadir ${datadir} --password <(echo $pwd) account \
    import <(echo $privkey)
# Build nodekey
echo "$nodekey" > ${datadir}/geth/nodekey
# Build staticnodes
echo "[]" > ${datadir}/static-nodes.json
# End
echo DONE

#!/bin/bash
pinum=02
datadir=data${pinum}/
privkey=d9f2eaa9794455a3d1c8adc7d5717f58db768dc8ae3430f4473b30b1f5fdaa24 # 0x030F23b9F8b5adba8c0FdB58e79b398420cb9B89
nodekey=989fc61967c868f52de2e693bf7233b0afe62aeadaaa3479d1983734fe31c912 # 03a46d5f0b7a5de1c7b2d4233693dbf5991d949ff789fb108081f57d796988f7788e23100f33ed82b1360ffa975c989aa7e76a4bebcc8aa8e427893ce43dd1f6
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

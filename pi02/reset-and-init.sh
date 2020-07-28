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
echo '[' >  ${datadir}/static-nodes.json
echo '"enode://010516a6e3acd95b9cf69c39d1d799d3e9fb8bef76e4c53bc1b92753a73b03e2e1222119365508dbb2faf18b365d2d42c86a4d748b6a8a7d1fa11592afb55ac5@192.168.0.100:30303",' >> ${datadir}/static-nodes.json
echo '"enode://021e339379c1115da274bbd80f8014789c10682aa8b9e97a5a50d8c4127423fb628c8ab5e6bbc9d8e0ffbf1c7204d95f955ef17dcd06237eb5118820b8045cd0@192.168.0.101:30303",' >> ${datadir}/static-nodes.json
echo '"enode://03a46d5f0b7a5de1c7b2d4233693dbf5991d949ff789fb108081f57d796988f7788e23100f33ed82b1360ffa975c989aa7e76a4bebcc8aa8e427893ce43dd1f6@192.168.0.102:30303"'  >> ${datadir}/static-nodes.json
echo ']' >>  ${datadir}/static-nodes.json
# End
echo DONE

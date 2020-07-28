#!/bin/bash
pinum=01
datadir=data${pinum}/
privkey=
privkey=7b98417687d193e2176e967d4f49e3ca1da48d5c75d72602626e6447fed29899 # 0x02090F81fb8c98017472f13cD334ddbD2448DD73
nodekey=ae73adda58cc379cf5d0c6c772c8ca828c50b974b45d1d2057a38d58317baa64 # 021e339379c1115da274bbd80f8014789c10682aa8b9e97a5a50d8c4127423fb628c8ab5e6bbc9d8e0ffbf1c7204d95f955ef17dcd06237eb5118820b8045cd0
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

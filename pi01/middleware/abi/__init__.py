import json

abi = '[{"constant":true,"inputs":[],"name":"average","outputs":\
[{"internalType":"int32","name":"","type":"int32"}],"payable":false,\
"stateMutability":"view","type":"function"},{"constant":true,"inputs":\
[],"name":"getAverage","outputs":[{"internalType":"int32","name":"","type":\
"int32"}],"payable":false,"stateMutability":"view","type":"function"},\
{"constant":true,"inputs":[],"name":"getMiliAverage","outputs":\
[{"internalType":"int32","name":"","type":"int32"}],"payable":false,\
"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],\
"name":"index","outputs":[{"internalType":"uint256","name":"","type":\
"uint256"}],"payable":false,"stateMutability":"view","type":"function"},\
{"constant":true,"inputs":[],"name":"measurementA","outputs":[{"internalType"\
:"int32","name":"","type":"int32"}],"payable":false,"stateMutability":"view",\
"type":"function"},{"constant":true,"inputs":[],"name":"measurementB",\
"outputs":[{"internalType":"int32","name":"","type":"int32"}],"payable":false,\
"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],\
"name":"measurementC","outputs":[{"internalType":"int32","name":"","type":\
"int32"}],"payable":false,"stateMutability":"view","type":"function"},\
{"constant":false,"inputs":[{"internalType":"int32","name":"val","type":\
"int32"}],"name":"set","outputs":[],"payable":false,"stateMutability":\
"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":\
"version","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],\
"payable":false,"stateMutability":"view","type":"function"}]'

def getAbi():
	return json.loads(abi)

from web3.middleware import geth_poa_middleware
import abi

CONTRACT_ADDRESS = "0x000000000000000000000000000000000000FFff"

class W3:
	def __init__(self, web3):
		web3.middleware_onion.inject(geth_poa_middleware, layer=0)
		self.web3 = web3
		self.ct_address = CONTRACT_ADDRESS
		self.block_filter = None
	def version(self):
		return self.web3.clientVersion
	def peerCount(self):
		return self.web3.net.peerCount
	def getBlockNumber(self):
		return self. web3.eth.blockNumber
	def contractAddress(self):
		return self.ct_address
	def createBlockFilter(self):
		self.block_filter = self.web3.eth.filter('latest')
		return self.block_filter
	def getCoinbase(self):
		return self.web3.eth.coinbase
	def getLatestBlockTimestamp(self):
		return self.web3.eth.getBlock("latest").timestamp
	def getContractVersion(self):
		ab = abi.getAbi()
		ct = self.ct_address
		smart_ct = self.web3.eth.contract(address=ct, abi=ab)
		v = smart_ct.functions.version().call()
		return v
	def getPiNumber(self):
		num = self.getCoinbase()
		num = num[2:]
		num = num[:2]
		num = int(num) - 1
		return num

if __name__ == "__main__":
	from web3 import Web3
	w3 = W3(Web3())
	print("version", w3.version())
	print("peerCount", w3.peerCount())
	print("getBlockNumber", w3.getBlockNumber())
	print("contractAddress", w3.contractAddress())
	print("createBlockFilter", w3.createBlockFilter())
	print("getCoinbase", w3.getCoinbase())
	print("getLatestBlockTimestamp", w3.getLatestBlockTimestamp())
	print("getContractVersion", w3.getContractVersion())
	print("getPiNumber", w3.getPiNumber())

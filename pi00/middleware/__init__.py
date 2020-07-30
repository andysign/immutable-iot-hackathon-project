from web3.middleware import geth_poa_middleware
try: import middleware.abi
except: import abi

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
	def getCtVersion(self):
		ab = abi.getAbi()
		ct = self.ct_address
		smart_ct = self.web3.eth.contract(address=ct, abi=ab)
		v = smart_ct.functions.version().call()
		return v
	def getMeasureAverage(self):
		ab = abi.getAbi()
		ct = self.ct_address
		smart_ct = self.web3.eth.contract(address=ct, abi=ab)
		average = smart_ct.functions.average().call()
		return average / 1000
	def setFakeReading(self, val):
		val = int(val)
		self.web3.eth.defaultAccount = self.getCoinbase()
		ab = abi.getAbi()
		ct = self.ct_address
		smart_ct = self.web3.eth.contract(address=ct, abi=ab)
		tx = smart_ct.functions.set(val).transact()
		return tx.hex()
	def getMeasurementA(self):
		ab = abi.getAbi()
		ct = self.ct_address
		smart_ct = self.web3.eth.contract(address=ct, abi=ab)
		return smart_ct.functions.measurementA().call() / 1000
	def getMeasurementB(self):
		ab = abi.getAbi()
		ct = self.ct_address
		smart_ct = self.web3.eth.contract(address=ct, abi=ab)
		return smart_ct.functions.measurementB().call() / 1000
	def getMeasurementC(self):
		ab = abi.getAbi()
		ct = self.ct_address
		smart_ct = self.web3.eth.contract(address=ct, abi=ab)
		return smart_ct.functions.measurementC().call() / 1000
	def getOtherMeasurement(self, other):
		m = 0
		if other == "A": m = self.getMeasurementA()
		if other == "B": m = self.getMeasurementB()
		if other == "C": m = self.getMeasurementC()
		return int(m)
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
	print("getCtVersion", w3.getCtVersion())
	print("getMeasureAverage", w3.getMeasureAverage())
	print("setFakeReading", w3.setFakeReading(10))
	print("getMeasurementA", w3.getMeasurementA())
	print("getPiNumber", w3.getPiNumber())

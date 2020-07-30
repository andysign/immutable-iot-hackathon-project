pragma solidity >=0.5.1 <=0.5.17;
// pragma experimental ABIEncoderV2;
// 0x000000000000000000000000000000000000FFff
contract Measure {
    uint8 public version = 1;
    // > eth.getStorageAt( ct2 , 0 )
    // "0x0000000000000000000000010394e95e108465e438fd0af870f44ca47b87df01"
    // > eth.getStorageAt( ct2 , 1 )
    // "0x00000000000000000000000002090f81fb8c98017472f13cd334ddbd2448dd73"
    // > eth.getStorageAt( ct2 , 2 )
    // "0x000000000000000000000064030f23b9f8b5adba8c0fdb58e79b398420cb9b89"
    address piA = 0x010394e95E108465E438fd0af870f44ca47B87dF;
    address piB = 0x02090F81fb8c98017472f13cD334ddbD2448DD73;
    address piC = 0x030F23b9F8b5adba8c0FdB58e79b398420cb9B89;
    int32 delta = 100;
    int32 public average = 0;
    int32 public measurementA;
    int32 public measurementB;
    int32 public measurementC;
    uint256 public index = 0;
    function set(int32 val) public {
        // let storage be set
        uint256 bn = block.number;
        uint256 mod = bn % 5;
        if (mod == 1 || mod == 2 || mod == 3) {
            address sndr = msg.sender;
            require( sndr == piA || sndr == piB || sndr == piC, "Sender not in ok list." );
            require( abs(val*1000 - average)/1000 < delta ); // if ( (val*1000-average)/1000 > delta ) val=average;
            if (sndr == piA) measurementA = val*1000;
            if (sndr == piB) measurementB = val*1000;
            if (sndr == piC) measurementC = val*1000;
            index++;
        } else {
            // create average and empty array
            average = (measurementA + measurementB + measurementC) / 3;
            measurementA = measurementB = measurementC = average;
        }
    }
    function abs(int32 v) internal pure returns (int32) {
        if (v<0) v = -v;
        return v;
    }
    function getMiliAverage () public view returns (int32) {
        return average;
    }
    function getAverage () public view returns (int32) {
        return average/1000;
    }
}

// contract c {
//     bytes public s;
//     function setStorage(bytes memory _s) public {
//         s = _s;
//     }
//     function getStorage() public view returns (bytes memory) {
//         return s;
//     }
// }

// blk 1    2
// blk 2    4
// blk 3    6
// blk 4    8 -- average
// blk 0/5 10 -- average and prepare for repeat

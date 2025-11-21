/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    for(L of nums){
      let count=0
      for(B of nums){
        if(L===B)
        count++
      }
      if(count===1){

    return L
      }
    }
};
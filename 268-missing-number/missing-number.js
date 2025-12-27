/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let max=Math.max(...nums)
    for(i=0;i<=max;i++){
        let found=false
        for(j=0;j<nums.length;j++){
            if(nums[j]===i){
                found=true
                break
            }
        }
       if(!found){
         return i
       }
    }
    return max +1
};
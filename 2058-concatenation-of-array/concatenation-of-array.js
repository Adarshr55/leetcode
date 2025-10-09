/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    let arr=[]
    for(i=0;i<nums.length;i++){
        arr.push(nums[i])
    }
        return nums.concat(arr)
    
    
};
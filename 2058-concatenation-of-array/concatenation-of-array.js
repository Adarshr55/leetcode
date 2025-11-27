/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    let arr=[]
   for(a of nums){
    arr.push(a)
   }
   return nums.concat(arr)
    
};
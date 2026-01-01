/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
let num=nums.map(m=>m*m)
num.sort((a,b)=>a-b)
return num
};
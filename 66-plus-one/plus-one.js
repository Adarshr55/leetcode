/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
let arr=(BigInt(digits.join(""))+1n).toString().split("").map(Number)  
  return arr
};
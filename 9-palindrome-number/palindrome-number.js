/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
   let s=x.toString()
let rev=s.split("").reverse().join("")
return s===rev
   
}
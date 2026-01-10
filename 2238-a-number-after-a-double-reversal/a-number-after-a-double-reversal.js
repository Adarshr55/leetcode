/**
 * @param {number} num
 * @return {boolean}
 */
var isSameAfterReversals = function(num) {
  let rev1 = parseInt(num.toString().split("").reverse().join(""));
    let rev2 = parseInt(rev1.toString().split("").reverse().join(""));
 return rev2===num
     
};
/**
 * @param {number[]} nums
 * @return {number}
 */
var returnToBoundaryCount = function(nums) {
    let number=0
    let count=0
    for(steps of nums){
    number+=steps
    if(number===0){
        count++
    }
    }
    return count
};
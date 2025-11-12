/**
 * @param {number[]} nums
 * @return {number}
 */
var differenceOfSum = function(nums) {
    let sum=0
    let dsum=0
    for(d of nums){
        sum+=d
        let str=d.toString().split("")
        for(c of str){
            dsum+=Number(c)
        }
        
    }
    return sum-dsum
    
};
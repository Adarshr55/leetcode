/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    let count=0
    let arr=[]
    for(let ele of nums){
        if(ele==1){
            count++
        }else{
            arr.push(count)
            count=0
        }
        arr.push(count)
    }
    return Math.max(...arr)
};
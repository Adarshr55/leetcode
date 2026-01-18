/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let a=[]
    let n=nums.length
    for (let i=0;i<n;i++){
        if(nums[i]==0){
        a=nums.splice(i,1)
        nums.push(...a)
        i--
        n--
    }
}
    return nums
};
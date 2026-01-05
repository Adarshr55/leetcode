/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {
     let set = new Set()
     let arr=[]
     for(n of nums){
        if(set.has(n)){
            arr.push(n)
        }
        set.add(n)
     }
     return arr

};
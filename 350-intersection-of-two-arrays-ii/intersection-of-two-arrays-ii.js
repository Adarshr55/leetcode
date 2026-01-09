/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
    let arr=[];
    for(let i=0; i<nums1.length; i++){
        let count=0;
        for(let j=0; j<nums2.length; j++){
            if(nums1[i]==nums2[j] && count==0){
                arr.push(nums1[i])
                count++;
                nums2.splice(j,1);
            }
        }
    }
    return arr;
};
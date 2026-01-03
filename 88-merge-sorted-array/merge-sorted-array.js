/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
  let arr=nums1.slice(0,m)
  for(i=0;i<n;i++){
    arr.push(nums2[i])
  }
  arr.sort((a,b)=>a-b)
  for(i=0;i<arr.length;i++){
    nums1[i]=arr[i]
  }
  return nums1
};
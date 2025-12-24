/**
 * @param {number[]} apple
 * @param {number[]} capacity
 * @return {number}
 */
var minimumBoxes = function(apple, capacity) {
     let totalapple=apple.reduce((a,b)=>a+b)
       capacity.sort((a,b)=>b-a)
       let current=0
       let boxcount=0
       for(cap of capacity){
          current+=cap
          boxcount++
          if(current>=totalapple){
            return boxcount
          }
       }
       return -1
};
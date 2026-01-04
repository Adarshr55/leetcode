/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {
   let arr=t.split("")
for( let c of s){
    for(i=0;i<arr.length;i++){
        if(c===arr[i]){
            arr.splice(i,1)
            break
        }
    }
}
return arr[0]
};
/**
 * @param {string} s
 * @return {number}
 */
var maxDepth = function(s) {
    let count=0
    let res=0
    for(str of s){
        if(str==="("){
            count++
            res=Math.max(res,count)
        }
        else if(str===")"){
            count--

        }
    }
    return res

};
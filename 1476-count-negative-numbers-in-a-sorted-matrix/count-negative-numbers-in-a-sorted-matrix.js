/**
 * @param {number[][]} grid
 * @return {number}
 */
var countNegatives = function(grid) {
    let count=0
    let g=grid.flat(Infinity)
    for(i of g){
        if(i<0)
        count++
    }
    return count
};
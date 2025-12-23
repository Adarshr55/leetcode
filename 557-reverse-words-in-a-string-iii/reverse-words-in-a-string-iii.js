/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    let word=s.split(" ")
    let result=[]
    for(let i=0;i<word.length;i++){
        let rev=""
        for(let j=word[i].length-1;j>=0;j--){
            rev+=word[i][j]
        }
        result.push(rev)
    }
    return result.join(" ")
};
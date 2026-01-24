/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    let words=s.split(" ");
    let result=[]
    for(let word of words){
        let pos=word[word.length-1];
        let cleanword=word.slice(0,-1);
        result[pos-1]=cleanword;
    }
    return result.join(" ")
};
// Last updated: 11/26/2025, 8:55:17 PM
/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    var usedOnce = false
    var result;
    return function(...args){
        if(!usedOnce) {
            result = fn(...args);
            usedOnce = true
            return result
        } else {
            return undefined
        }


        
    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */

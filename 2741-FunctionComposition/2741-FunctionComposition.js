// Last updated: 11/26/2025, 8:55:21 PM
/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x) {
        var vall = x
        for(i=functions.length-1; i >= 0; i--) {
            vall = functions[i](vall)
        }
        return vall
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
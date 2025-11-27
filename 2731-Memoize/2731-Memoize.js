// Last updated: 11/26/2025, 8:55:24 PM
/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let cache = {}
    return function(...args) {
        key = JSON.stringify(args)
        if (key in cache) {
            return cache[key]
        }
        cache[key] = fn(...args)
        return cache[key]
        
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */
import { expect } from '@jest/globals';
import { quickSort } from './sort';

function runTests(sortFn) {
    const testCases = [
        [],
        [2, 1],
        [1],
        [3, 5, 4],
        [-1, 2, -6, 3, 5, 123, 54, 2, -6, 23, 4],
    ];

    for (let i = 0; i < testCases.length; i++) {
        const array = [...testCases[i]];
        test(`test case ${i}`, () => {
            expect(sortFn([...array])).toEqual(array.sort((a, b) => a - b));
        });
    }
}

runTests(quickSort);
import { expect } from '@jest/globals';
import {
    bubbleSort,
    insertionSort,
    selectionSort,
    mergeSortTopDown,
    mergeSortBottomUp,
    quickSortLomuto,
    quickSortHoare,
    heapSort,
} from './sort';

function runTests(sortFn) {
    const testCases = [
        [],
        [2, 1],
        [1],
        [3, 5, 4],
        [-1, 2, -6, 3, 5, 123, 54, 2, -6, 23, 4],
    ];

    for (let i = 0; i < testCases.length; i++) {
        test(`test case ${i}`, () => {
            const array = [...testCases[i]];
            expect(sortFn([...array])).toEqual(array.sort((a, b) => a - b));
        });
    }
}

describe('bubbleSort', () => {
    runTests(bubbleSort);
});

describe('insertionSort', () => {
    runTests(insertionSort);
});

describe('selectionSort', () => {
    runTests(selectionSort);
});

describe('mergeSortTopDown', () => {
    runTests(mergeSortTopDown);
});

describe('mergeSortBottomUp', () => {
    runTests(mergeSortBottomUp);
});

describe('quickSortLomuto', () => {
    runTests(quickSortLomuto);
});

describe('quickSortHoare', () => {
    runTests(quickSortHoare);
});

describe('heapSort', () => {
    runTests(heapSort);
});
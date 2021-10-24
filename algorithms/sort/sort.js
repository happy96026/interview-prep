export function bubbleSort(arr) {
    for (let i = arr.length - 1; i >= 1; i--) {
        for (let j = 0; j < i; j++) {
            const lo = j;
            const hi = j + 1;
            if (arr[lo] > arr[hi]) {
                [arr[lo], arr[hi]] = [arr[hi], arr[lo]];
            }
        }
    }

    return arr;
}

export function insertionSort(arr) {
    for (let i = 1; i < arr.length; i++) {
        for (let j = i; j >= 1; j--) {
            const lo = j - 1;
            const hi = j;
            if (arr[lo] > arr[hi]) {
                [arr[lo], arr[hi]] = [arr[hi], arr[lo]];
            }
        }
    }

    return arr;
}

export function selectionSort(arr) {
    for (let i = 0; i < arr.length - 1; i++) {
        let minIndex = i;
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]];
    }

    return arr;
}

export function mergeSortTopDown(arr) {
    const copyArr = Array(arr.length);
    for (let i = 0; i < arr.length; i++) {
        copyArr[i] = arr[i];
    }

    function merge(lo, hi, srcArr, destArr) {
        if (hi - lo <= 1) {
            return;
        }

        const mid = Math.floor((lo + hi) / 2);
        merge(lo, mid, destArr, srcArr);
        merge(mid, hi, destArr, srcArr);

        let i = lo;
        let j = mid;
        for (let k = lo; k < hi; k++) {
            if (j >= hi || (i < mid && srcArr[i] <= srcArr[j])) {
                destArr[k] = srcArr[i];
                i++;
            } else {
                destArr[k] = srcArr[j];
                j++;
            }
        }
    }
    merge(0, arr.length, copyArr, arr);

    return arr;
}

export function mergeSortBottomUp(arr) {
    const copyArr = Array(arr.length);
    for (let i = 0; i < arr.length; i++) {
        copyArr[i] = arr[i];
    }

    const log = Math.ceil(Math.log2(arr.length));
    let chunkLength = 2;
    let [srcArr, destArr] = log % 2 ? [copyArr, arr] : [arr, copyArr];
    for (let level = 0; level < log; level++) {
        const iterations = Math.ceil(arr.length / chunkLength);

        for (let iteration = 0; iteration < iterations; iteration++) {
            const lo = iteration * chunkLength;
            const hi = lo + chunkLength;
            const mid = Math.floor((lo + hi) / 2);
            const upper = Math.min(hi, arr.length);

            let i = lo;
            let j = mid;
            for (let k = lo; k < upper; k++) {
                if (j >= upper || (i < mid && srcArr[i] <= srcArr[j])) {
                    destArr[k] = srcArr[i];
                    i++;
                } else {
                    destArr[k] = srcArr[j];
                    j++;
                }
            }
            
        }

        chunkLength *= 2;
        [srcArr, destArr] = [destArr, srcArr];
    }

    return arr;
}

export function quickSortLomuto(arr) {
    function partition(lo, hi) {
        const pivotIndex = hi - 1;
        let partitionIndex = lo;

        for (let i = lo; i < pivotIndex; i++) {
            if (arr[i] <= arr[pivotIndex]) {
                [arr[i], arr[partitionIndex]] = [arr[partitionIndex], arr[i]];
                partitionIndex++;
            }
        }
        [arr[partitionIndex], arr[pivotIndex]] = [arr[pivotIndex], arr[partitionIndex]];

        return partitionIndex;
    }

    function quickSort(lo, hi) {
        if (hi - lo <= 1) {
            return;
        }

        const partitionIndex = partition(lo, hi);
        quickSort(lo, partitionIndex);
        quickSort(partitionIndex + 1, hi);
    }

    quickSort(0, arr.length);
    return arr;
}

export function quickSortHoare(arr) {
    function partition(lo, hi) {
        const pivot = arr[Math.floor((lo + hi) / 2)];
        let i = lo - 1;
        let j = hi;

        while (true) {
            do {
                i++;
            } while (arr[i] < pivot);
            do {
                j--;
            } while (arr[j] > pivot);

            if (i < j) {
                [arr[i], arr[j]] = [arr[j], arr[i]];
            } else {
                break;
            }
        }

        return i;
    }

    function quickSort(lo, hi) {
        if (hi - lo <= 1) {
            return;
        }

        const partitionIndex = partition(lo, hi);
        quickSort(lo, partitionIndex);
        quickSort(partitionIndex, hi);
    }

    quickSort(0, arr.length);
    return arr;
}

export function heapSort(arr) {
    function getLeftChildIndex(i) {
        return i * 2 + 1;
    }

    function getRightChildIndex(i) {
        return i * 2 + 2;
    }

    function siftDown(i, arr, length) {
        while (true) {
            const nodes = [i, getLeftChildIndex(i), getRightChildIndex(i)]
                .map(index => ({
                    index,
                    value: index < length ? arr[index] : -Infinity,
                }));
            const maxNode = nodes.reduce((maxNode, node) => node.value > maxNode.value ? node : maxNode);

            if (maxNode.index === i) {
                break;
            } else {
                [arr[i], arr[maxNode.index]] = [arr[maxNode.index], arr[i]];
                i = maxNode.index;
            }
        }
    }

    function heapify(arr) {
        for (let i = arr.length - 1; i >= 0; i--) {
            siftDown(i, arr, arr.length);
        }
    }

    function sort(arr) {
        for (let i = arr.length - 1; i >= 1; i--) {
            [arr[i], arr[0]] = [arr[0], arr[i]];
            siftDown(0, arr, i);
        }
    }

    heapify(arr);
    sort(arr);

    return arr;
}
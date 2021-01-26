
from ldpc import encode, decode
from bitstring import BitArray
K = 128
N = 384
P = [[84, 118, 9, 104], [114, 94, 93, 17], [70, 121, 61, 31], [21, 80, 30, 64], [66, 102, 16, 71], [100, 107, 1, 37], [38, 65, 32, 60], [122, 123, 11, 85], [62, 109, 126, 39], [76, 90, 63, 22], [82, 69, 113, 67], [27, 120, 96, 55], [6, 35, 108, 10], [14, 53, 41, 99], [29, 4, 54, 127], [103, 115, 42, 88], [48, 77, 110, 12], [74, 72, 83, 56], [40, 28, 50, 86], [78, 52, 45, 87], [95, 24, 8, 25], [36, 101, 119, 68], [111, 26, 34, 59], [2, 23, 18, 20], [19, 57, 33, 5], [125, 116, 105, 15], [51, 98, 81, 112], [3, 46, 89, 92], [44, 91, 58, 13], [73, 47, 43, 79], [0, 75, 106, 124], [117, 49, 7, 97], [0, 72, 32, 117], [109, 104, 107, 55], [13, 85, 15, 49], [65, 40, 92, 111], [35, 88, 112, 83], [81, 89, 94, 36], [127, 39, 73, 7], [87, 126, 115, 59], [96, 44, 50, 119], [10, 9, 23, 42], [66, 12, 56, 100], [34, 82, 97, 71], [48, 1, 76, 26], [54, 78, 106, 51], [18, 67, 16, 46], [31, 6, 110, 47], [4, 41, 60, 64], [21, 5, 98, 116], [52, 3, 75, 123], [90, 58, 93, 77], [61, 86, 121, 45], [27, 53, 17, 80], [113, 125, 124, 8], [103, 70, 120, 28], [62, 20, 22, 74], [24, 95, 25, 57], [11, 33, 102, 43], [68, 122, 108, 30], [37, 29, 91, 63], [14, 99, 2, 19], [101, 79, 69, 118], [105, 38, 84, 114], [101, 121, 100, 15], [85, 25, 90, 24], [48, 45, 63, 91], [10, 2, 71, 108], [34, 3, 30, 120], [59, 46, 41, 62], [35, 123, 57, 5], [127, 80, 23, 114], [96, 38, 27, 113], [53, 14, 111, 29], [118, 116, 12, 70], [82, 93, 7, 78], [54, 50, 36, 52], [109, 55, 110, 124], [94, 97, 87, 105], [107, 103, 6, 11], [66, 58, 88, 112], [83, 33, 104, 21], [67, 31, 32, 122], [9, 86, 8, 20], [95, 92, 117, 119], [44, 18, 64, 79], [72, 60, 73, 40], [17, 39, 61, 81], [75, 47, 26, 126], [0, 49, 37, 115], [89, 68, 99, 69], [1, 19, 76, 4], [106, 13, 102, 56], [125, 74, 65, 84], [16, 42, 77, 22], [28, 43, 51, 98], [98, 46, 22, 116], [109, 106, 96, 75], [61, 20, 86, 13], [7, 119, 105, 71], [12, 15, 16, 99], [108, 25, 64, 49], [100, 69, 11, 47], [55, 76, 94, 88], [66, 18, 80, 44], [35, 43, 14, 42], [17, 31, 45, 115], [103, 91, 67, 10], [90, 68, 24, 48], [41, 59, 54, 3], [95, 34, 113, 92], [81, 73, 111, 62], [32, 9, 30, 74], [5, 39, 36, 127], [60, 72, 27, 126], [21, 112, 63, 19], [2, 8, 4, 56], [1, 110, 70, 58], [82, 123, 93, 53], [78, 85, 97, 87], [33, 23, 79, 125], [37, 38, 57, 117], [6, 102, 107, 121], [101, 51, 26, 104], [40, 120, 29, 50], [52, 0, 84, 28], [118, 77, 89, 122], [65, 83, 114, 124], [125, 47, 55, 70], [60, 126, 15, 113], [123, 80, 17, 67], [96, 34, 49, 41], [56, 53, 103, 90], [111, 14, 127, 81], [44, 88, 87, 30], [12, 105, 106, 83], [21, 5, 68, 36], [43, 79, 6, 52], [28, 69, 101, 25], [29, 82, 7, 1], [84, 92, 85, 93], [9, 114, 89, 65], [78, 115, 24, 35], [13, 16, 98, 91], [37, 58, 120, 4], [8, 26, 27, 76], [124, 110, 112, 64], [66, 51, 39, 94], [107, 99, 40, 18], [122, 54, 59, 116], [108, 86, 11, 19], [63, 77, 62, 20], [104, 102, 31, 38], [109, 33, 72, 74], [71, 121, 10, 0], [23, 75, 22, 46], [42, 117, 57, 118], [100, 3, 61, 119], [45, 97, 32, 48], [2, 73, 95, 50], [84, 44, 34, 104], [3, 29, 45, 87], [75, 111, 36, 76], [118, 41, 16, 51], [62, 22, 49, 83], [121, 23, 101, 40], [125, 10, 33, 8], [37, 31, 89, 124], [71, 88, 5, 109], [28, 108, 112, 15], [54, 35, 119, 11], [126, 17, 69, 64], [106, 61, 94, 19], [74, 72, 97, 123], [67, 122, 9, 63], [57, 21, 50, 65], [85, 102, 7, 68], [116, 86, 80, 14], [58, 6, 105, 81], [100, 82, 92, 77], [27, 70, 93, 103], [60, 30, 98, 32], [26, 110, 99, 25], [96, 38, 1, 12], [107, 127, 42, 47], [95, 115, 0, 114], [24, 73, 78, 43], [48, 39, 56, 52], [13, 53, 113, 79], [117, 55, 91, 2], [4, 120, 90, 18], [66, 46, 59, 20], [86, 82, 103, 89], [113, 43, 49, 106], [123, 14, 95, 88], [29, 107, 109, 37], [119, 30, 39, 101], [31, 77, 99, 91], [7, 63, 127, 124], [98, 54, 104, 67], [85, 20, 80, 66], [78, 94, 42, 19], [96, 11, 59, 100], [17, 18, 16, 57], [120, 112, 2, 9], [1, 69, 47, 12], [75, 81, 122, 114], [60, 72, 10, 32], [48, 125, 92, 5], [52, 40, 62, 15], [24, 50, 13, 46], [118, 108, 8, 97], [53, 51, 58, 93], [117, 27, 71, 44], [79, 116, 21, 55], [0, 121, 45, 111], [102, 76, 6, 110], [34, 126, 41, 35], [61, 90, 65, 22], [36, 23, 84, 38], [87, 70, 3, 64], [105, 26, 74, 25], [73, 33, 56, 115], [83, 28, 4, 68], [64, 112, 14, 55], [98, 127, 53, 32], [76, 73, 117, 124], [66, 26, 116, 100], [3, 17, 0, 2], [102, 8, 43, 72], [39, 5, 81, 107], [86, 38, 101, 105], [74, 90, 96, 28], [41, 6, 106, 57], [84, 12, 77, 48], [42, 9, 75, 49], [22, 15, 21, 108], [71, 68, 83, 92], [88, 13, 91, 58], [99, 35, 97, 40], [115, 78, 37, 27], [118, 114, 93, 33], [89, 4, 11, 30], [7, 56, 67, 45], [10, 126, 61, 1], [50, 80, 63, 20], [46, 94, 44, 121], [59, 65, 60, 95], [103, 87, 119, 125], [24, 29, 25, 109], [34, 82, 36, 113], [31, 51, 23, 70], [52, 104, 54, 120], [62, 79, 111, 122], [123, 47, 16, 85], [18, 69, 110, 19]]
w = BitArray('0b10010111011100100000110010001110100010010001011001010011001010101100010001001010111111011110000100111011101100111011111110111010')
x = encode(K, P, w)
assert x == BitArray('0b100101110111001000001100100011101000100100010110010100110010101011000100010010101111110111100001001110111011001110111111101110100100101010000001111100111101101111001111101110100000111100101000111110000101011011001100111100001110101110000010110000010110011010010110100100110100011000010100001010100011110011101000100100001100110111001111110101110100100000000000001011010010001110011100')
y = BitArray('0b100001010011000000000100100010100000000100010010000100010000101010000000010000001101000000100000000010101000000000011101001010000100100010000001100100111101001010001111001010000000000100100000000110000000000000000000010000001000101110000010000000010100001000010110100100000000011000000000000010000010010011001000100100000000010010000000000101110000000000000000001001000010000110011100')
q = BitArray('0b001110101100111110101010011101011100100001001101111000101010000001101101001010100010111111001011101101010111001110100010100101110001011000011100011000000000110101000000110100101010111001011100111000110101011011111111101100000111000001101001110001101011010011001000011010111101100101010100111100101001100000100010010011111100101101101111110010001111101000101011110010110001011000000001')
hat_y = decode(K, P, y, q)
assert hat_y is not None
hat_w = hat_y[:K]
assert hat_w == w
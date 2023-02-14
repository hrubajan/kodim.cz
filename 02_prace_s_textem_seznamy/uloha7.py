teploty = [
...   [2.1, 5.2, 6.1, -0.1],
...   [2.2, 4.8, 5.6, -1.0],
...   [3.3, 6.5, 5.9, 1.2],
...   [2.9, 5.6, 6.0, 0.0],
...   [2.0, 4.6, 5.5, -1.2],
...   [1.0, 3.2, 2.1, -2.0],
...   [0.4, 2.7, 1.3, -2.8]]

# a] 
[sum(temp)/len(temp) for temp in teploty] 
#[3.325, 2.9, 4.2250000000000005, 3.625, 2.725, 1.0750000000000002, 0.40000000000000013]

# b] 
[temp[0] for temp in teploty]
#[2.1, 2.2, 3.3, 2.9, 2.0, 1.0, 0.4]

# c] 
[temp[-1] for temp in teploty] 
#[-0.1, -1.0, 1.2, 0.0, -1.2, -2.0, -2.8]

# d] 
[[temp[0],temp[-1]] for temp in teploty] 
#[[2.1, -0.1], [2.2, -1.0], [3.3, 1.2], [2.9, 0.0], [2.0, -1]

# e] 
x=[sum(temp)/len(temp) for temp in teploty]
sum(x)/len(x)
#2.6107142857142853

# nebo
sum( [sum(temp) for temp in teploty] ) / sum ( [len(temp) for temp in teploty] )
#2.6107142857142853
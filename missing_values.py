# Columns represent years
column_header = ['2019','2020',	'2021',	'2022',	'2023',	'2024',	'2025']

# Rows represent Spending Technology Categories
row_header = ['Business Services', 'Hardware', 'IT Services', 'Software', 'Telecom Services']

# Each row in the matrix below represent one Technology and each column one Year of data
test_data = [
    [477.471,	 484.593,	 518.988,	 572.115,	 640.693,	 720.916,	 814.72],
    [2597.189,	2701.082,	3149.978,	3320.256,	3392.421,	3438.651,	3467.47],
    [2600.082,	2628.529,	2896.001,	3286.340,	    None,	4215.841,	4787.348],
    [1556.779,	1654.627,	1831.514,	2025.143,	2237.725,	2481.181,	2762.201],
    [3100.55,	3201.79,	3242.249,	    None,   3355.419,	3402.868,	2120.409]
]

# Propose a solution how to aproximate the mising points
for row in test_data:
    for elem in row:
        if elem == None:
            
            i = row.index(elem)
            row[i] = round((row[i-1]+row[i+1])/2,3)
           
            
print(test_data)

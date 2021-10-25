import pydea
import pandas as pd
inputs = pd.DataFrame([[3, 3, 2], [1, 5, 3], [6, 4, 20], [7, 6, 4]], columns=['Professors', 'Lecturers', 'Assistants'])
outputs = pd.DataFrame([[10, 5, 5, 24], [14, 9, 1, 4], [10, 15, 11, 1], [21, 11, 10, 7]], columns=['Bachelors', 'Masters', 'Doctors', 'Journal articles'])
import matplotlib.pyplot as plt

print(inputs)
print(outputs)

# Build and solve

uni_prob = pydea.DEAProblem(inputs, outputs, returns='CRS')
myresults = uni_prob.solve()

print(myresults['Status'])
print(myresults['Efficiency'])
print(myresults['Weights'])


myresults['Efficiency'].hist(bins=50)
plt.ylabel('Frequency')
plt.xlabel('Efficiency score')
plt.title('Distribution of efficiency scores')
plt.show()


# 6.3 a) MS moved

# import pydea
# import pandas as pd
# inputs = pd.DataFrame([[1, 5, 3], [6, 4, 20], [7, 6, 4]], columns=['Professors', 'Lecturers', 'Assistants'])
# outputs = pd.DataFrame([[14, 9, 1, 4], [10, 15, 11, 1], [21, 11, 10, 7]], columns=['Bachelors', 'Masters', 'Doctors', 'Journal articles'])
# import matplotlib.pyplot as plt

# print(inputs)
# print(outputs)

# # Build and solve

# uni_prob = pydea.DEAProblem(inputs, outputs, returns='CRS')
# myresults = uni_prob.solve()

# print(myresults['Status'])
# print(myresults['Efficiency'])
# print(myresults['Weights'])


# myresults['Efficiency'].hist(bins=50)
# plt.ylabel('Frequency')
# plt.xlabel('Efficiency score')
# plt.title('Distribution of efficiency scores')
# plt.show()



# # Journal articles no longr considered 6.3 b)
# # import pydea
# # import pandas as pd
# # inputs = pd.DataFrame([[3, 3, 2], [1, 5, 3], [6, 4, 20], [7, 6, 4]], columns=['Professors', 'Lecturers', 'Assistants'])
# # outputs = pd.DataFrame([[10, 5, 5], [14, 9, 1], [10, 15, 11], [21, 11, 10]], columns=['Bachelors', 'Masters', 'Doctors'])
# # import matplotlib.pyplot as plt

# # print(inputs)
# # print(outputs)

# # # Build and solve

# # uni_prob = pydea.DEAProblem(inputs, outputs, returns='CRS')
# # myresults = uni_prob.solve()

# # print(myresults['Status'])
# # print(myresults['Efficiency'])
# # print(myresults['Weights'])


# # myresults['Efficiency'].hist(bins=50)
# # plt.ylabel('Frequency')
# # plt.xlabel('Efficiency score')
# # plt.title('Distribution of efficiency scores')
# # plt.show()
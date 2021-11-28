import matplotlib.pyplot as plt
import numpy as np

sMethod = 'Hebb' #'Hebb'/'Pseudoinverse'
filename = sMethod + '_4x4_2.png'

#patterns
pat = np.matrix([[0,1,1,1,0,0,1,0,0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,0]]) #T,L
pat[pat == 0] = -1

#test image
test = np.matrix([0,1,0,1,0,0,1,0,0,0,0,0,0,0,1,0])
test[test == 0] = -1

#ploting patterns and test image
plt.figure(1)

#patterns
for iPat in range (0, len(pat)):
    vector = pat[iPat,:]
    plt.subplot(2, 2, iPat + 1)
    matrix = np.matrix.reshape(vector, 4, 4)
    plt.imshow(matrix)
    plt.axis('off')
    plt.title(f'Wzorzec {iPat + 1}')

#test image
vector = test
plt.subplot(2, 2, 3)
matrix = np.matrix.reshape(vector, 4, 4)
plt.imshow(matrix)
plt.axis('off')
plt.title('Obraz testowy')

#number of neurons
n = np.size(pat[0])

#patterns arrays transpose
d = np.transpose(pat)
d_trans = np.transpose(d)

#matrix of weight
match sMethod:
        case 'Hebb':
                w = (1/n) * d * d_trans
                p_max = 0.138 * n
        case 'Pseudoinverse':
                w = d * ((d_trans * d)**-1) * d_trans
                p_max = n - 1

#learning
test = np.transpose(test)
for i in range(1,11):
        if i == 1:
                output = np.sign(w * test)
        else:
                output = np.sign(w * output)

#result
result = np.matrix.reshape(output, 4, 4)
plt.subplot(2, 2, 4)
plt.imshow(result)
plt.axis('off')
plt.title(sMethod)

#saving to file.png
plt.savefig(filename)

#showing the result
plt.show()
import numpy as np
import matplotlib.pyplot as plt

matrix = np.column_stack((np.arange(1, 5),
np.arange(12, 16)))
print("행렬:\n", matrix)
matrix2 = np.vstack((np.arange(1, 5),
np.arange(12, 16)))


# 행렬의 크기를 재어주는 shape 속성
print("행렬의 크기:", matrix.shape)

np.zeros((5))
#list,tuple 둘 다 됨
np.zeros([4,5]) 

np.arange(1,5).reshape([2,2])
#size 크기와 와 shape 크기 일치해야함
np.arange(1,7).reshape((2,3))
np.arange(1,7).reshape((2,-1))
np.arange(1,7).reshape(-1)

#-1 통해서 크기를 자동으로 결정할 수 있음
#Q. 0에서 99까지 수 중 랜덤하게 50개 숫자를 뽑아서
#5 by 10 행렬을 만드세요.
np.random.seed(2024)
np.random.randint(0,100,50).reshape(5,-1)

mat_a = np.arange(1,21).reshape((4,5),order="F")
mat_a

mat_a[0,1]
mat_a[1,1]
mat_a[2,3]
mat_a[0:2,3]
mat_a[:,3]
mat_a[1:3,1:4]
mat_a[3,]
mat_a[:,3]
mat_a[3,::2]
#행자리,열자리 비어있는 경우 전체 행 또는 열 선택

#짝수 행만 선택하려면?
mat_b = np.arange(1,101).reshape((20,5),order="F")
mat_b
mat_b[1::2,:]
mat_b[[1,4,6,14],]
mat_b[1::3,:]

x = np.arange(1,11).reshape(5,2)*2
filtered_elements = x
x[[True,True,False,False,True],0]

mat_b[:,1]
mat_b[:,1].reshape((-1,1))
mat_b[:,[1]]
mat_b[:,(1,)]
mat_b[:,1:2]

#필터링
#7의 배수
mat_b[mat_b[:,1]%7==0,1]

img1 = np.random.rand(3,3)
print("이미지 행렬 img1:\n",img1)

plt.imshow(img1,cmap="gray",interpolation="nearest")
plt.colorbar()
plt.show()
plt.clf()

img_mat = np.loadtxt('./data/img_mat.csv', delimiter=',', skiprows=1)
# 행렬의 크기 확인
print("행렬의 크기:", img_mat.shape)
# 행렬의 일부 확인
print("행렬의 일부:\n", img_mat[:3, :4])

a = np.random.randint(0,10,20).reshape(4,-1)
a/9

print("최대값:", img_mat.max())
print("최소값:", img_mat.min())

img_mat = img_mat / 255.0

plt.imshow(img_mat, cmap='gray', interpolation='nearest')
plt.colorbar()
plt.show()


import urllib.request
import imageio
img_url = "https://bit.ly/3ErnM2Q"
urllib.request.urlretrieve(img_url, "jelly.png")
jelly = imageio.imread("jelly.png")
print("이미지 클래스:", type(jelly))
print("이미지 차원:", jelly.shape)
print("이미지 첫 4x4 픽셀, 첫 번째 채널:\n", jelly[:4, :4, 0])

jelly.shape
jelly[:,:,0].shape

plt.imshow(jelly[:,:,0].transpoes())#R
plt.imshow(jelly[:,:,1])#G
plt.imshow(jelly[:,:,2])#B
plt.imshow(jelly[:,:,3])#투명도
plt.imshow(jelly)
plt.axis("off") #축 정보 없애기
plt.show()
plt.clf()

# 두 개의 2x3 행렬 생성
mat1 = np.arange(1, 7).reshape(2, 3)
mat2 = np.arange(7, 13).reshape(2, 3)
# 3차원 배열로 합치기
my_array = np.array([mat1, mat2])
my_array.shape
print("3차원 배열 my_array:\n", my_array)

my_array2 = np.array([my_array,my_array])
my_array2[0,:,:,:]

filtered_array = my_array[:,:,:-1]
filtered_array

mat_x = np.arange(1,101).reshape((5,5,4))
mat_y = np.arange(1,101).reshape((-1,5,2))

my_array[:,:,[0,2]]
my_array[:,[0],:]
my_array[0,1,[1,2]]
my_array[0,1,1:3]
# 첫 번째 2차원 배열 선택
first_slice = my_array[0, :, :]
print("첫 번째 2차원 배열:\n", first_slice)
# 두 번째 차원의 세 번째 요소를 제외한 배열 선택
filtered_array = my_array[:, :, :-1]
print("세 번째 요소를 제외한 배열:\n", filtered_array)
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
a = np.array([[1,2,3],[4,5,6]])

a.sum()
a.sum(axis=0)
a.sum(axis=1)

a.mean()
a.mean(axis=0)
a.mean(axis=1)

np.random.seed(2024)
mat_b = np.random.randint(0,100,50).reshape((5,-1))
mat_b.shape
mat_b.max()
#행별로 가장 큰 수
mat_b.max(axis=1)
#열별로 가장 큰 수

a=np.array([1,3,2,5])
a.cumsum()
a.cumprod()
#행별 누적 값
mat_b.cumsum(axis=1)
#열별 누적 값
mat_b.cumsum(axis=0)

#flatten

mat_b.reshape((2,5,5)).flatten()
mat_b.flatten()

#clip
d = np.array([1,2,3,4,5])
d2 = np.random.randint(1,100,160)
d2.clip(20,40)


d.tolist()
e = np.array([1.1, 2.2, 3.6])
round(3.6)
print("정수형 배열:", e.astype(int))


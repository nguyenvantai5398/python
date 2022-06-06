#Input of table and make empty space around table
print('nội dung ô vuông')
n=input()
matrix=[]
space=''
st=[]
for i in range(int(n)+2):
    space+=' '
matrix.append(space)
for i in range(int(n)):
    matrix.append(' '+input()+' ')
matrix.append(space)

#Input of strings to check
print('các nội dung chuỗi chữ cái xem có thể tạo ra từ bảng hay ko')
m=input()
for i in range(int(m)):
    st.append(input())

#Check 4 directions
def check(st,i,j,matrix,r,c):
    if st[i][j]==matrix[r-1][c]:
        return [r-1,c,True,j+1]
    if st[i][j]==matrix[r+1][c]:
        return [r+1,c,True,j+1]
    if st[i][j]==matrix[r][c-1]:
        return [r,c-1,True,j+1]
    if st[i][j]==matrix[r][c+1]:
        return [r,c+1,True,j+1]
    return[r,c,False,j+1]

#Check the first characters matching of each string and table, then check around to move
for i in range(int(m)):
    t=False
    for r in range(int(n)+2):
        for c in range(int(n)+2):
            j=0
            if st[i][j]==matrix[r][c]:
                j=1
                t=True
                while j<len(st[i]) and t==True:
                    [r,c,t,j]=check(st,i,j,matrix,r,c)
            if t==True:
                break
        if t==True:
                break
    if t==True:
        print('yes')
    else:
        print('no')
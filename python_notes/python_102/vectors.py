ar1= [[2,3,6,7,2,6] , 
     [5,2,6,5,3,1], 
     [4,5,7,1,8,3]]
                                                                               ####LIST OF ARRAYS###
ar2=[[3,6,1,7,8,5] , 
    [2,6,4,8,3,5],
    [6,2,1,8,3,9]]                            
result=[]
i=0                                                                            ##i REPRESENTS ROWS###

while i <len(ar1):
    send_result=[]                                                ##EMPTY LIST FOR SENDING TO FINAL RESULT##
    c=0                                                            ##C IS THE ARGUEMENT FOR COLUMN##
    while c<len(ar1[0]):             
        send_result.append(ar1[i][c]+ar2[i][c])                   ###SENDS RESULTS TO POPULATE send_result=[]####
        c+=1                                                  ### THE SECOND 'while' ALLOWS YOU TO POPULATE THE COLUMS FIRST.
    i+=1                                                          
    result.append(send_result)                                   ###AFTER THE FIIRST LIST IS POPULATED, .APPEND TO RESULT AND
print(result)                                                      #RECOMPLETE LOOP FOR SECOND COLUMN, OR 'c'###









# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]
# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]
# # iterate through rows
# for i in range(len(X)):
#    # iterate through columns
#    for j in range(len(X[0])):
#        result[i][j] = X[i][j] + Y[i][j]
# for r in result:
#    print(r)




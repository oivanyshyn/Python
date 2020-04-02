def merger(a):

    lst=[]

    lst.append(a[0])

    for i in range(1,len(a)):

        if a[i][0]<=lst[-1][1]:

            if a[i][1]>lst[-1][1]:

                low=lst[-1][0]
                high=a[i][1]
                lst.pop()
                lst.append([low,high])

            if a[i][1]<=lst[-1][1]:

                low=lst[-1][0]
                high=lst[-1][1]
                lst.pop()
                lst.append([low,high])

            if lst[-1][0]<a[i][1]<lst[-1][1]:

                low=a[i][0]
                high=lst[-1][1]
                lst.pop()
                lst.append([low,high])



        else:
            lst.append(a[i])

    return lst

array=[[2, 10], [4, 12], [13, 16], [19,20], [20 , 24]]
print(merger(array))
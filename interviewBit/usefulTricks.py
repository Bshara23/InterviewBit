
if __name__ == "__main__":

    #swapping variables
    x = 4
    y = 3

    x, y = y, x

    print(x)
    print(y)



    
    # initializing lists 
    name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ] 
    roll_no = [ 4, 1, 3, 2 ] 
    marks = [ 40, 50, 60, 70 ] 
  
    # using zip() to map values 
    mapped = zip(name, roll_no, marks) 
    mapped = set(mapped) 

    print(mapped)


    top2 = 20
    top3 = 30
    top1 = 10
    top = 0
    top = max(top,top1,top2,top3)


    arr = [1, 2, 3, 2, -5, 6, 22, -4, 10]

    # all values false
    l = [0, False]
    print(any(l))


    # one true
    l = [0, False, 1]
    print(any(l))



    # only 0 is false
    l = [1, True, 4, -4, 0, 1]
    print(all(l))

    A = "abc"
    A = A[::-1] # reverse string / array

    from collections import Counter
    z = ["a", "b", "b", "c", "cc", "abc", "cc", "cc"]
    counter = Counter(z)
    print("count = ", counter)
    print("b = ", counter["b"])
    # print top 3 most common
    for letter, cnt in counter.most_common(3):
        print(letter, " : ", cnt)




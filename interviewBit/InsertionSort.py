

# best case O(n)
# worst case O(n^2)

# analogy from a deck of cards, image having an unsorted deck of cards
# in one hand and we want to move it to the other hand by in an increasing order
# pick the first card from the right hand and put it in the left hand
# then pick the next card from the right hand and put it below the
# first card that is higher than the current card

# Function to do insertion sort
def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i] # save this key
        
		# put the key right above first number smaller than key
        j = i - 1 # compare with the next number from the left
        while j >=0 and key < arr[j] : # move left
            arr[j+1] = arr[j] # number is higher than me
							  # then move it above me
            j -= 1

        arr[j+1] = key 

# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)

print(arr)





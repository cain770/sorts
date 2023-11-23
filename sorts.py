def bubble_sort(items):
    
    while True:
        was_swapped = False

        for i in range(len(items)-1):
            if items[i] > items[i+1]:
                was_swapped = True
                #swap them
                items[i], items[i+1] = items[i+1], items[i]

        if not was_swapped:
            break

items = [1,6,34,2,7,4,78,4]
print(items)
bubble_sort(items)
print(items)
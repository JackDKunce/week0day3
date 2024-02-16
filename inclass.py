def blender(fruit1, fruit2):
    print('...blending...')
    smoothie = 'You made a ' + fruit1 + ' and ' + fruit2 + ' smoothie!'
    return smoothie


s1 = blender('strawberry', 'banana')
s2 = blender('kiwi', 'mango')
s3 = blender('blueberry', 'raspberry')

print(s1)
print(s2)
print(s3)

print(blender('passionfruit', 'watermelon'))


def print_up_to(num):
    for num in range(num + 1):
        print(num)
    
print_up_to(1)



def area(length, width):
    return length * width

print(area(11, 11))
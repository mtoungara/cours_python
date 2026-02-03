###
blocks = int(input("Enter the number of blocks: "))

height = 0 # Completed layers.
layerBlock_requirement = 1

while blocks >= layerBlock_requirement:
    layerBlock_progress = 0
while layerBlock_progress != layerBlock_requirement:
    blocks -= 1
    layerBlock_progress += 1
    if layerBlock_progress == layerBlock_requirement:
        height += 1
    layerBlock_requirement += 1

print("The height of the pyramid:", height)
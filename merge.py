import sys
from PIL import Image

output = sys.argv[-1]
images = [Image.open(x) for x in sys.argv[1:-1]]

widths, heights = zip(*(i.size for i in images))
total_width = max(widths)
# add border space
border = 20
total_height = sum(heights) + border * (len(images) - 1)

new_im = Image.new('RGB', (total_width, total_height), color='white')
y_offset = 0
for im in images:
    x_offset = (total_width - im.width) // 2
    new_im.paste(im, (x_offset, y_offset))
    y_offset += im.height + border

new_im.save(output)
print("Merge Success!")

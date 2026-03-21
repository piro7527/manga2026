import shutil
import sys
import os

out_dir = "/Users/aoyamahiroki/Desktop/manga2026/output/2026-03-21_長い休み"
os.makedirs(out_dir, exist_ok=True)

files = [
    ("/Users/aoyamahiroki/.gemini/antigravity/brain/46baa5b4-7ab1-4226-b99b-680989ce00a2/manga_panel_one_revised_1774100825648.png", f"{out_dir}/2026-03-21_長い休み_panel_1.png"),
    ("/Users/aoyamahiroki/.gemini/antigravity/brain/46baa5b4-7ab1-4226-b99b-680989ce00a2/manga_panel_two_1774099802586.png", f"{out_dir}/2026-03-21_長い休み_panel_2.png"),
    ("/Users/aoyamahiroki/.gemini/antigravity/brain/46baa5b4-7ab1-4226-b99b-680989ce00a2/manga_panel_three_1774099818355.png", f"{out_dir}/2026-03-21_長い休み_panel_3.png"),
    ("/Users/aoyamahiroki/.gemini/antigravity/brain/46baa5b4-7ab1-4226-b99b-680989ce00a2/manga_panel_four_revised_1774100840480.png", f"{out_dir}/2026-03-21_長い休み_panel_4.png")
]

for src, dst in files:
    print(f"Copying {src} to {dst}")
    shutil.copy(src, dst)

try:
    from PIL import Image
    images = [Image.open(dst) for _, dst in files]
    widths, heights = zip(*(i.size for i in images))
    total_width = max(widths)
    border = 20
    total_height = sum(heights) + border * (len(images) - 1)

    new_im = Image.new('RGB', (total_width, total_height), color='white')
    y_offset = 0
    for im in images:
        x_offset = (total_width - im.width) // 2
        new_im.paste(im, (x_offset, y_offset))
        y_offset += im.height + border

    output = f"{out_dir}/2026-03-21_長い休み_final.png"
    new_im.save(output)
    print("Merge Success!")
except ImportError as e:
    print(f"PIL not installed: {e}")
except Exception as e:
    print(f"Error merging: {e}")

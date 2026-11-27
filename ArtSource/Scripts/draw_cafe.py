"""Draw the CityLife cafe as two registered RGBA sprites.

Run with Python and Pillow. The interior is the base sprite. The exterior
overlay covers it with the roof and street facade while the player is outside.
"""

import argparse
from pathlib import Path
from random import Random

from PIL import Image, ImageDraw


SIZE = (192, 160)
INK = "#252c31"
MORTAR = "#6a534c"
CREAM = "#f2d9a5"
WOOD = "#b67b4c"
WOOD_DARK = "#69463c"
LEAF = "#49765c"
LEAF_LIGHT = "#78a66b"
TEAL = "#376b6d"
TEAL_LIGHT = "#548589"
BRASS = "#f2bf70"
OUTPUT = (
    Path(__file__).resolve().parents[2]
    / "Game/Assets/CityLife/Art/Props/Cafe"
)

LETTERS = {
    "A": ("010", "101", "111", "101", "101"),
    "C": ("011", "100", "100", "100", "011"),
    "E": ("111", "100", "110", "100", "111"),
    "F": ("111", "100", "110", "100", "100"),
    "H": ("101", "101", "111", "101", "101"),
    "L": ("100", "100", "100", "100", "111"),
    "O": ("010", "101", "101", "101", "010"),
    "Z": ("111", "001", "010", "100", "111"),
}


def pixel_text(draw, position, label, color, scale=1):
    left, top = position
    for index, letter in enumerate(label):
        for row, pattern in enumerate(LETTERS[letter]):
            for column, bit in enumerate(pattern):
                if bit == "1":
                    x = left + (index * 4 + column) * scale
                    y = top + row * scale
                    draw.rectangle((x, y, x + scale - 1, y + scale - 1), color)


def plant(draw, x, y, pot="#b76c53"):
    draw.ellipse((x - 5, y + 4, x + 6, y + 8), "#65504a")
    draw.polygon(
        ((x - 4, y), (x + 4, y), (x + 3, y + 6), (x - 3, y + 6)),
        fill=pot, outline=INK,
    )
    draw.line((x - 2, y + 4, x + 1, y + 4), fill="#e8a479")
    draw.polygon(
        ((x, y + 2), (x - 6, y - 3), (x - 6, y - 6), (x - 2, y - 5),
         (x, y - 9), (x + 3, y - 8), (x + 3, y - 4), (x + 6, y - 6),
         (x + 6, y - 2)),
        fill=LEAF, outline=INK,
    )
    draw.line((x - 4, y - 5, x - 2, y - 3), fill=LEAF_LIGHT)
    draw.line((x + 1, y - 7, x, y - 2, x + 4, y - 4), fill=LEAF_LIGHT)


def draw_entry(draw):
    draw.rounded_rectangle((12, 37, 181, 145), 10, "#5e5353")
    draw.rounded_rectangle((14, 34, 177, 141), 8, "#856d60")
    draw.rectangle((17, 121, 175, 137), "#aa8d75", outline=MORTAR)
    draw.rectangle((18, 123, 174, 133), "#c7ac8e")
    draw.line((18, 134, 174, 134), fill="#e5c4a1")
    draw.line((19, 129, 174, 129), fill="#b49a83")
    for x in range(26, 172, 16):
        draw.line((x, 123, x, 128), fill="#aa9079")
        draw.line((x + 5, 130, x + 5, 133), fill="#aa9079")
    draw.rectangle((84, 126, 107, 139), "#b49a83", outline=MORTAR)
    draw.rectangle((85, 128, 106, 135), "#e5c4a1")
    draw.line((85, 136, 106, 136), fill="#a9876f")
    draw.line((87, 137, 104, 137), fill="#f0d2ab")
    plant(draw, 29, 135)
    plant(draw, 162, 135)


def draw_floor(draw):
    draw.rectangle((24, 29, 167, 125), INK)
    draw.rectangle((27, 36, 164, 121), "#d5a276")
    plank_colors = ("#d9ac7e", "#d3a275", "#deb286", "#ca986d")
    random = Random(26)
    for row, y in enumerate(range(48, 120, 5)):
        draw.rectangle((28, y, 163, min(y + 4, 119)), plank_colors[row % 4])
        draw.line((28, y + 4, 163, y + 4), fill="#bc865e")
        seam_start = 37 + (row * 9) % 24
        for x in range(seam_start, 164, 24):
            draw.line((x, y + 1, x, y + 3), fill="#be8d63")
            draw.point((x + 1, y + 1), fill="#f0c395")
        for _ in range(4):
            x = random.randrange(31, 160)
            draw.line((x, y + 2, x + 2, y + 2), fill="#c89366")

    draw.rectangle((80, 112, 111, 121), "#a96d56", outline=WOOD_DARK)
    draw.rectangle((82, 113, 109, 119), "#c18968")
    for x in range(84, 110, 4):
        draw.line((x, 114, x, 118), fill="#edb68a")
    draw.rectangle((26, 120, 83, 125), "#8b624e", outline=INK)
    draw.rectangle((108, 120, 165, 125), "#8b624e", outline=INK)
    draw.line((27, 121, 82, 121), fill="#efcf9b")
    draw.line((109, 121, 164, 121), fill="#efcf9b")
    draw.line((84, 124, 107, 124), fill="#815f51", width=2)


def draw_back_wall(draw):
    draw.rectangle((24, 29, 167, 55), "#f5d8a4", outline=INK)
    draw.rectangle((26, 30, 165, 33), "#936851")
    draw.line((27, 30, 164, 30), fill="#d99c69")
    draw.rectangle((27, 45, 164, 53), "#d6ad7d")
    draw.line((26, 46, 165, 46), fill="#f3e0b8")
    for x in range(29, 165, 5):
        draw.line((x, 49, x, 52), fill="#bb986f")
    draw.rectangle((24, 54, 29, 120), "#aa7a5f", outline=INK)
    draw.rectangle((162, 54, 167, 120), "#aa7a5f", outline=INK)
    draw.line((26, 55, 26, 119), fill="#eec997")
    draw.line((165, 55, 165, 119), fill="#eec997")

    draw.rectangle((39, 35, 79, 47), WOOD_DARK, outline=INK)
    draw.rectangle((41, 37, 77, 45), "#344447")
    pixel_text(draw, (48, 39), "COFFEE", CREAM)
    draw.point((43, 40), fill=BRASS)
    draw.point((75, 40), fill=BRASS)
    draw.rectangle((87, 35, 109, 49), WOOD_DARK, outline=INK)
    draw.rectangle((89, 37, 107, 47), "#597c7d")
    draw.rectangle((90, 38, 106, 41), "#9db6a1")
    draw.line((98, 37, 98, 47), fill="#3a5153")
    draw.line((89, 42, 107, 42), fill="#3a5153")
    draw.line((86, 49, 110, 49), fill="#ead3aa")

    draw.rectangle((124, 36, 153, 51), WOOD_DARK, outline=INK)
    for y in (38, 44):
        draw.rectangle((126, y, 151, y + 4), "#a67958")
        for index, color in enumerate(("#ddd2a1", "#6f8d83", "#deb874", "#ba7b68")):
            x = 127 + 6 * index
            draw.rectangle((x, y, x + 2, y + 2), color)
            draw.point((x + 1, y), fill="#f8e7b2")
        draw.line((125, y + 4, 152, y + 4), fill="#62443a")


def draw_counter(draw):
    draw.rounded_rectangle((34, 58, 84, 82), 4, "#986f56")
    draw.rectangle((34, 62, 82, 78), WOOD_DARK, outline=INK)
    draw.rectangle((36, 70, 80, 77), "#855747")
    for x in range(41, 80, 8):
        draw.line((x, 71, x, 76), fill="#6e4b40")
        draw.point((x + 2, 73), fill=BRASS)
    draw.rectangle((33, 59, 83, 70), "#f0be82", outline=INK)
    draw.line((35, 60, 81, 60), fill="#ffe0a2")
    draw.line((35, 68, 81, 68), fill="#c68955")

    draw.rectangle((38, 54, 52, 66), "#6a8280", outline=INK)
    draw.rectangle((39, 55, 51, 57), "#b8c4ad")
    draw.rectangle((40, 59, 50, 64), "#38484a")
    draw.line((41, 60, 49, 60), fill="#a3b8a6")
    draw.rectangle((43, 62, 47, 65), "#f0d4a4")
    draw.point((48, 62), fill=BRASS)
    for x in (54, 58, 62):
        draw.rectangle((x, 62, x + 2, 64), CREAM)
        draw.point((x + 1, 62), fill="#8d5c47")
    draw.rectangle((69, 58, 77, 65), "#3a5557", outline=INK)
    draw.rectangle((70, 59, 76, 61), "#92b49d")
    draw.line((70, 63, 76, 63), fill="#d7c595")
    draw.line((62, 52, 67, 52), fill="#fff1b4")
    draw.point((64, 53), fill=BRASS)


def chair(draw, x, y, upholstery):
    draw.ellipse((x - 5, y - 3, x + 5, y + 5), WOOD_DARK, outline=INK)
    draw.rectangle((x - 3, y + 4, x - 2, y + 6), WOOD_DARK)
    draw.rectangle((x + 2, y + 4, x + 3, y + 6), WOOD_DARK)
    draw.ellipse((x - 4, y - 3, x + 4, y + 2), upholstery)
    draw.line((x - 2, y - 2, x + 2, y - 2), fill="#b2bd8e")


def round_table(draw, x, y):
    draw.ellipse((x - 11, y - 4, x + 13, y + 9), "#ab7b5b")
    draw.rectangle((x - 1, y + 4, x + 1, y + 9), WOOD_DARK)
    draw.ellipse((x - 11, y - 6, x + 11, y + 6), WOOD_DARK, outline=INK)
    draw.ellipse((x - 10, y - 6, x + 10, y + 3), "#e5b079")
    draw.line((x - 5, y - 5, x + 5, y - 5), fill="#f8cd8f")
    draw.line((x - 8, y, x - 1, y), fill=WOOD)
    draw.ellipse((x - 5, y - 3, x - 1, y + 1), "#bf8d67")
    draw.rectangle((x - 5, y - 3, x - 3, y - 1), "#fff2c7")
    draw.point((x - 2, y - 2), fill=CREAM)
    draw.point((x - 4, y - 3), fill="#8c5b42")
    draw.rectangle((x + 4, y - 2, x + 6, y + 1), "#709375")
    draw.point((x + 5, y - 3), fill="#d9ac70")


def draw_seating(draw):
    draw.rectangle((114, 60, 151, 68), WOOD_DARK, outline=INK)
    draw.rectangle((115, 59, 150, 62), LEAF, outline=INK)
    draw.rectangle((116, 63, 149, 66), "#79a080")
    draw.line((126, 62, 126, 66), fill=LEAF)
    draw.line((138, 62, 138, 66), fill=LEAF)

    chair(draw, 133, 87, TEAL)
    round_table(draw, 133, 75)

    draw.rectangle((42, 88, 77, 115), "#856252")
    draw.rectangle((43, 89, 76, 114), "#a7795d")
    draw.rectangle((45, 91, 74, 112), "#c08967")
    draw.rectangle((47, 93, 72, 110), outline="#dba683")
    for x in range(47, 73, 5):
        draw.point((x, 90), fill="#f0c49a")
        draw.point((x, 113), fill="#f0c49a")
    chair(draw, 45, 100, LEAF)
    chair(draw, 74, 101, LEAF)
    round_table(draw, 58, 100)

    chair(draw, 124, 107, LEAF)
    chair(draw, 151, 110, LEAF)
    round_table(draw, 137, 105)
    plant(draw, 37, 115)
    plant(draw, 156, 57, "#bb8c54")


def draw_interior():
    interior = Image.new("RGBA", SIZE)
    draw = ImageDraw.Draw(interior)
    draw_entry(draw)
    draw_floor(draw)
    draw_back_wall(draw)
    draw_counter(draw)
    draw_seating(draw)
    return interior


def draw_front_window(draw, x):
    draw.rectangle((x, 99, x + 39, 123), WOOD_DARK, outline=INK)
    draw.rectangle((x + 2, 102, x + 37, 119), "#47656a")
    draw.rectangle((x + 3, 104, x + 36, 117), "#69817b")
    draw.rectangle((x + 4, 109, x + 35, 117), "#d9a36b")
    draw.polygon(
        ((x + 8, 104), (x + 11, 104), (x + 4, 116), (x + 4, 111)),
        fill="#9dae99",
    )
    draw.polygon(
        ((x + 28, 104), (x + 30, 104), (x + 22, 117), (x + 19, 117)),
        fill="#a7ad87",
    )
    for y in (106, 114):
        draw.line((x + 2, y, x + 37, y), fill="#3e5657")
    draw.line((x + 19, 102, x + 19, 119), fill=INK, width=2)
    draw.rectangle((x - 1, 120, x + 40, 122), "#f5d7a0", outline=WOOD_DARK)


def draw_facade(draw):
    draw.rectangle((24, 86, 167, 125), "#d7a276", outline=INK)
    draw.rectangle((27, 89, 164, 120), "#ebc990")
    draw.rectangle((27, 91, 164, 95), "#b78261")
    draw.rectangle((25, 120, 166, 125), "#91624f", outline=INK)
    draw.line((26, 124, 165, 124), fill="#bf8d68")
    for x in (29, 72, 115, 158):
        draw.rectangle((x, 96, x + 3, 120), "#bf8962")
        draw.line((x + 1, 97, x + 1, 117), fill="#f1d29c")
    draw_front_window(draw, 33)
    draw_front_window(draw, 119)

    draw.rectangle((83, 96, 108, 126), WOOD_DARK, outline=INK)
    draw.rectangle((85, 99, 106, 122), "#46686c", outline=INK)
    draw.rectangle((87, 106, 104, 120), "#bb8a67")
    draw.rectangle((87, 106, 104, 111), "#789089")
    draw.line((88, 108, 91, 104), fill="#c1bd96")
    draw.line((95, 99, 95, 122), fill=INK, width=2)
    for x in (92, 99):
        draw.line((x, 113, x, 115), fill=BRASS)
    draw.rectangle((84, 123, 107, 126), "#6c554a", outline=INK)
    draw.line((86, 124, 105, 124), fill="#e4bc8d")

    draw.polygon(
        ((81, 94), (110, 94), (114, 101), (114, 104),
         (77, 104), (77, 101)),
        fill=TEAL, outline=INK,
    )
    for x in (84, 94, 104):
        draw.polygon(((x, 95), (x + 4, 95), (x + 5, 101), (x - 1, 101)), fill=CREAM)
        draw.line((x - 1, 102, x + 5, 102), fill="#c39369")
    draw.line((78, 103, 113, 103), fill="#345252")

    for x in (77, 114):
        draw.line((x, 108, x, 113), fill=INK, width=2)
        draw.rectangle((x - 2, 111, x + 2, 114), BRASS, outline=WOOD_DARK)
        draw.point((x, 112), fill="#fff0b2")
    for x in (31, 174):
        draw.line((x, 127, x, 128), fill="#a78166")


def draw_roof(draw):
    draw.polygon(
        ((23, 17), (168, 17), (173, 23), (173, 89), (169, 95),
         (22, 95), (18, 90), (18, 23)),
        fill=INK,
    )
    draw.rectangle((22, 20, 169, 83), "#396466", outline="#203e43")
    draw.rectangle((25, 23, 166, 79), TEAL)
    draw.line((24, 22, 167, 22), fill="#649293")
    draw.line((22, 25, 22, 79), fill="#558485")
    draw.line((168, 25, 168, 79), fill="#294749")

    for index, x in enumerate(range(29, 165, 12)):
        draw.rectangle((x, 25, x + 9, 79), "#49787b" if index % 3 == 1 else "#407174")
        draw.line((x, 25, x, 79), fill="#31585c")
        draw.line((x + 1, 27, x + 1, 78), fill=TEAL_LIGHT)
        draw.line((x + 4, 34 + index % 4 * 7, x + 7, 34 + index % 4 * 7), fill="#558186")
        draw.point((x, 79), fill="#86a49a")

    draw.rectangle((20, 82, 171, 91), "#4f7473", outline=INK)
    draw.line((22, 83, 169, 83), fill="#8fa89a")
    draw.line((22, 88, 169, 88), fill="#345759")
    draw.line((24, 91, 167, 91), fill="#233b40")
    draw.line((28, 93, 163, 93), fill="#ba8d66")

    draw.rectangle((133, 38, 152, 50), "#33565b")
    draw.rectangle((132, 36, 149, 47), "#536d6b", outline=INK)
    draw.rectangle((131, 33, 150, 39), "#a2a492", outline=INK)
    draw.line((133, 34, 148, 34), fill="#d4c4a3")
    for x in range(134, 148, 3):
        draw.line((x, 36, x, 37), fill="#657d78")

    draw.rectangle((60, 65, 131, 85), "#29474c")
    draw.rectangle((62, 64, 129, 84), WOOD_DARK, outline=INK)
    draw.rectangle((64, 66, 127, 81), "#ede0b5")
    draw.line((65, 67, 126, 67), fill="#fff0c3")
    draw.line((65, 80, 126, 80), fill="#ba9671")
    pixel_text(draw, (77, 69), "HAZEL", "#35535a", scale=2)
    for x in (69, 121):
        draw.line((x - 1, 74, x + 1, 74), fill="#b68052")
        draw.line((x, 73, x, 75), fill="#b68052")


def draw_exterior_overlay():
    exterior = Image.new("RGBA", SIZE)
    draw = ImageDraw.Draw(exterior)
    draw_facade(draw)
    draw_roof(draw)
    return exterior


def save_preview(path, interior, exterior):
    outside = Image.alpha_composite(interior, exterior)
    background = "#e7e0d2"
    preview = Image.new("RGB", (424, 184), background)
    draw = ImageDraw.Draw(preview)
    draw.rounded_rectangle((12, 9, 207, 172), 8, "#f6f0e3")
    draw.rounded_rectangle((216, 9, 411, 172), 8, "#f6f0e3")
    preview.paste(outside, (14, 11), outside)
    preview.paste(interior, (218, 11), interior)
    path.parent.mkdir(parents=True, exist_ok=True)
    preview.resize((1272, 552), Image.Resampling.NEAREST).save(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--preview", type=Path, help="Optional comparison PNG")
    args = parser.parse_args()
    interior = draw_interior()
    exterior = draw_exterior_overlay()

    args.output.mkdir(parents=True, exist_ok=True)
    interior.save(args.output / "cafe_interior.png")
    exterior.save(args.output / "cafe_exterior_overlay.png")
    if args.preview:
        save_preview(args.preview, interior, exterior)


if __name__ == "__main__":
    main()

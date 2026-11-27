"""Draw the registered CityLife café sprites and furniture atlas with Pillow."""

import argparse
from pathlib import Path
from random import Random

from PIL import Image, ImageDraw


SIZE = (224, 192)
ATLAS_SIZE = (192, 128)
INK = "#282b31"
CREAM = "#f6deac"
WOOD = "#ba8459"
WOOD_DARK = "#68463d"
TEAL = "#376b6d"
TEAL_LIGHT = "#598b88"
BRASS = "#efbc72"
SHADOW = (80, 45, 44, 62)
OUTPUT = Path(__file__).resolve().parents[2] / "Game/Assets/CityLife/Art/Props/Cafe"

LETTERS = {
    "A": ("010", "101", "111", "101", "101"),
    "E": ("111", "100", "110", "100", "111"),
    "H": ("101", "101", "111", "101", "101"),
    "L": ("100", "100", "100", "100", "111"),
    "M": ("101", "111", "111", "101", "101"),
    "N": ("1001", "1101", "1011", "1001", "1001"),
    "U": ("101", "101", "101", "101", "111"),
    "Z": ("111", "001", "010", "100", "111"),
}


def pixel_text(draw, position, label, color, scale=1):
    left, top = position
    for letter in label:
        glyph = LETTERS[letter]
        for row, pattern in enumerate(glyph):
            for column, bit in enumerate(pattern):
                if bit == "1":
                    x = left + column * scale
                    y = top + row * scale
                    draw.rectangle((x, y, x + scale - 1, y + scale - 1), color)
        left += (len(glyph[0]) + 1) * scale


def cup(draw, x, y, color=CREAM):
    draw.line((x, y + 4, x + 5, y + 4), fill="#a87d5f")
    draw.point((x + 5, y + 1), fill=color)
    draw.rectangle((x, y, x + 4, y + 3), color)
    draw.line((x + 1, y, x + 3, y), fill="#87553f")
    draw.point((x + 2, y + 1), fill=BRASS)


def plant(draw, x, y, pot):
    draw.ellipse((x - 7, y + 4, x + 8, y + 9), SHADOW)
    draw.polygon(((x - 5, y), (x + 5, y), (x + 3, y + 7), (x - 3, y + 7)), pot, INK)
    draw.line((x - 3, y + 3, x + 2, y + 3), fill="#e6a57a")
    draw.polygon(
        ((x, y + 2), (x - 7, y - 3), (x - 7, y - 7), (x - 3, y - 6),
         (x - 2, y - 3), (x - 3, y - 10), (x + 1, y - 13), (x + 4, y - 9),
         (x + 2, y - 3), (x + 7, y - 7), (x + 7, y - 3)),
        "#47765b", INK,
    )
    draw.line((x - 5, y - 5, x, y - 1, x + 1, y - 10), fill="#82a86b")
    draw.line((x + 3, y - 2, x + 5, y - 5), fill="#a9b978")


def draw_entry(draw):
    draw.rounded_rectangle((12, 125, 213, 181), radius=8, fill="#514950")
    draw.rounded_rectangle((12, 127, 210, 177), radius=7, fill="#82706c")
    draw.rounded_rectangle((15, 134, 207, 175), radius=6, fill="#b9a28a", outline="#735e59")
    for index, y in enumerate(range(151, 175, 6)):
        draw.line((17, y, 205, y), fill="#9e8577")
        draw.line((18, y + 1, 204, y + 1), fill="#ccae91")
        for x in range(27 + index % 2 * 8, 203, 16):
            draw.line((x, y + 2, x, min(174, y + 5)), fill="#a58b7b")

    draw.rectangle((94, 151, 129, 173), "#8e7166", outline="#6b544f")
    draw.rectangle((96, 153, 127, 168), "#d6b79a")
    draw.line((96, 162, 127, 162), fill="#b09684")
    draw.line((96, 163, 127, 163), fill="#eed0ac")
    draw.line((96, 170, 127, 170), fill="#ebcba6")
    draw.line((98, 172, 125, 172), fill="#9c7d70")

    draw.rectangle((17, 57, 206, 154), "#776261")


def draw_floor(draw):
    draw.rectangle((20, 27, 203, 152), INK)
    draw.rectangle((25, 51, 198, 149), "#d6a679")
    planks = ("#dcb184", "#d7a77c", "#dcb084", "#d1a076", "#d9a87a")
    random = Random(26)
    for row, y in enumerate(range(53, 148, 5)):
        draw.rectangle((25, y, 198, y + 4), planks[row % len(planks)])
        draw.line((25, y + 4, 198, y + 4), fill="#bd8d67")
        for x in range(32 + (row * 11) % 24, 198, 24):
            draw.line((x, y + 1, x, y + 3), fill="#c29068")
            draw.point((x + 1, y + 1), fill="#e8bd90")
        for _ in range(5):
            x = random.randrange(28, 192)
            draw.line((x, y + 2, x + random.randint(1, 4), y + 2), fill="#cd9b71")

    draw.rectangle((26, 55, 101, 100), "#546662")
    for row, y in enumerate(range(56, 98, 6)):
        for column, x in enumerate(range(27, 101, 6)):
            color = "#a7ab91" if (row + column) % 2 == 0 else "#879688"
            draw.rectangle((x, y, min(x + 4, 100), y + 4), color)
            draw.line((x, y, min(x + 4, 100), y), fill="#b1b69f")
    draw.line((27, 99, 100, 99), fill="#ebc991")

    draw.rounded_rectangle((29, 107, 94, 146), radius=3, fill="#b68061", outline="#95624e")
    draw.rectangle((32, 110, 91, 143), outline="#dfab7c")
    draw.rounded_rectangle((132, 102, 195, 145), radius=3, fill="#a76458", outline="#8c5a51")
    draw.rectangle((134, 104, 193, 143), "#b87d68", outline="#dbaa83")
    for y in range(107, 143, 4):
        for x in range(136 + y % 3, 191, 5):
            draw.line((x, y, x + 1, y), fill="#c38b73")

    draw.rectangle((99, 139, 124, 151), "#6f7970", outline="#59605b")
    draw.rectangle((101, 141, 122, 149), outline="#aeab8a")
    for x in range(103, 122, 3):
        draw.line((x, 143, x, 147), fill="#899487")
    draw.line((97, 152, 126, 152), fill="#bd9a7c")

    for left, right in ((20, 96), (127, 203)):
        draw.rectangle((left, 148, right, 153), "#865c46", outline=INK)
        draw.line((left + 1, 149, right - 1, 149), fill="#e8c497")
        draw.line((left + 1, 152, right - 1, 152), fill="#a5775a")


def draw_back_wall(draw):
    draw.rectangle((20, 27, 203, 55), "#efd1a0", outline=INK)
    draw.rectangle((22, 28, 201, 31), "#8e674f")
    draw.line((23, 28, 200, 28), fill="#dea372")
    draw.rectangle((23, 47, 200, 54), "#c8a178")
    draw.line((24, 47, 199, 47), fill="#f8e3ba")
    for x in range(27, 200, 5):
        draw.line((x, 50, x, 53), fill="#af8b69")

    for left in (20, 198):
        draw.rectangle((left, 54, left + 5, 148), "#9a725b", outline=INK)
        draw.line((left + 2, 55, left + 2, 147), fill="#e9c296")

    draw.rectangle((31, 34, 72, 47), WOOD_DARK, outline=INK)
    draw.rectangle((33, 36, 70, 45), "#344f50")
    pixel_text(draw, (36, 38), "MENU", CREAM)
    for y, width in ((38, 12), (41, 8), (44, 10)):
        draw.line((55, y, 55 + width, y), fill="#91a895")

    draw.rectangle((77, 34, 99, 49), WOOD_DARK, outline=INK)
    for y in (36, 43):
        draw.rectangle((79, y, 97, y + 4), "#a07758")
        for x, color in ((81, "#dcac75"), (87, "#769589"), (93, "#bf7e69")):
            draw.rectangle((x, y + 1, x + 2, y + 3), color)
            draw.point((x + 1, y + 1), fill=CREAM)
        draw.line((78, y + 4, 98, y + 4), fill=WOOD_DARK)

    draw.ellipse((109, 34, 123, 46), "#aa784f", outline=WOOD_DARK)
    draw.ellipse((111, 36, 121, 44), CREAM)
    cup(draw, 114, 38, TEAL)
    draw.line((110, 50, 121, 50), fill="#e0bc90")

    draw.rectangle((133, 32, 192, 54), WOOD_DARK, outline=INK)
    draw.rectangle((135, 34, 190, 51), "#718f88")
    draw.rectangle((136, 35, 189, 41), "#a5b8a7")
    draw.polygon(((139, 36), (145, 36), (136, 48), (136, 41)), "#cfccae")
    draw.polygon(((172, 35), (178, 35), (165, 51), (159, 51)), "#b8c3ac")
    draw.polygon(((136, 51), (145, 45), (153, 48), (169, 45), (189, 49), (189, 51)), "#64887e")
    for x in (153, 171):
        draw.line((x, 34, x, 51), fill="#3b5958", width=2)
        draw.line((x + 2, 35, x + 2, 51), fill="#c2b59a")
    draw.line((135, 43, 190, 43), fill="#516f69")
    draw.rectangle((132, 51, 193, 54), "#e8ba84", outline=WOOD_DARK)
    draw.line((134, 52, 191, 52), fill="#f5d7a1")


def draw_prep_counter(draw):
    draw.rounded_rectangle((29, 62, 97, 72), radius=3, fill=SHADOW)
    draw.rectangle((30, 53, 95, 69), "#9a664b", outline=INK)
    draw.rectangle((31, 61, 94, 68), "#875842")
    for x in range(34, 94, 10):
        draw.rectangle((x, 62, x + 6, 67), "#a57151")
        draw.line((x + 2, 63, x + 4, 63), fill=BRASS)
    draw.rectangle((29, 53, 96, 61), "#e1b787", outline=WOOD_DARK)
    draw.line((31, 54, 94, 54), fill="#f4d29e")
    draw.line((31, 60, 94, 60), fill="#ac7c5b")

    draw.rectangle((34, 49, 54, 59), "#5c7777", outline=INK)
    draw.rectangle((35, 50, 53, 52), "#bdd1bc")
    draw.rectangle((37, 53, 50, 57), "#3f5053")
    draw.line((38, 53, 49, 53), fill="#e5ceb0")
    draw.point((52, 53), fill=BRASS)
    cup(draw, 41, 55)
    draw.line((35, 58, 53, 58), fill="#9eb2a4")

    draw.rectangle((59, 55, 66, 59), "#426466", outline=INK)
    draw.polygon(((59, 48), (66, 48), (65, 54), (60, 54)), "#9d775a", INK)
    draw.line((60, 49, 65, 49), fill="#d5b38b")

    draw.rectangle((75, 54, 89, 59), "#879b96", outline="#5b6d68")
    draw.rectangle((77, 55, 87, 57), "#56777a")
    draw.line((82, 55, 82, 51, 85, 51, 85, 52), fill="#cad2b9")
    cup(draw, 90, 54)


def draw_service_counter(draw):
    draw.rounded_rectangle((29, 91, 100, 105), radius=4, fill=SHADOW)
    draw.rectangle((31, 85, 98, 103), "#2b4549", outline=INK)
    draw.rectangle((33, 91, 96, 100), TEAL)
    for x in range(35, 97, 4):
        draw.line((x, 92, x, 99), fill="#4f7c77")
    draw.line((33, 101, 96, 101), fill="#bc8f59")
    draw.rectangle((67, 93, 82, 98), "#314e50", outline="#c49b64")
    draw.line((72, 95, 77, 95), fill=CREAM)

    draw.rectangle((29, 82, 100, 91), WOOD_DARK, outline=INK)
    draw.rectangle((30, 82, 99, 88), "#e3b580")
    draw.line((31, 83, 98, 83), fill="#f1d19c")
    draw.line((30, 89, 99, 89), fill="#c39162")

    draw.rounded_rectangle((33, 73, 61, 88), radius=2, fill="#566f70", outline=INK)
    draw.rectangle((35, 75, 59, 83), "#a0b1a1")
    draw.rectangle((35, 76, 59, 77), "#b6c1ab")
    draw.rectangle((35, 83, 59, 85), "#d4ad79")
    for x in (36, 43, 50):
        draw.ellipse((x, 79, x + 5, 83), "#a66652")
        draw.line((x + 1, 79, x + 3, 79), fill="#f1cd8c")
        draw.point((x + 3, 81), fill="#ce9363")
    draw.line((58, 75, 54, 81), fill="#e2e3c4")
    draw.line((35, 86, 59, 86), fill="#566765")

    draw.rectangle((67, 83, 78, 87), "#4b6567", outline=INK)
    draw.polygon(((68, 82), (68, 77), (76, 77), (77, 82)), "#34494c", INK)
    draw.line((69, 78, 75, 78), fill="#b8c8a5")
    draw.point((75, 80), fill=BRASS)

    draw.rectangle((83, 85, 94, 88), "#a87857", outline="#955f48")
    for x in (84, 90):
        draw.polygon(((x, 82), (x + 4, 82), (x + 3, 86), (x + 1, 86)), "#f2d8aa", "#c09770")
        draw.line((x, 82, x + 4, 82), fill="#fff1c9")


def table_flowers(draw, x, y):
    draw.rectangle((x, y, x + 3, y + 3), "#708e80")
    draw.point((x + 1, y), fill="#b5b498")
    draw.line((x + 2, y, x + 2, y - 2), fill="#54785e")
    draw.point((x + 3, y - 2), fill="#c17968")
    draw.point((x + 1, y - 3), fill="#f6ce83")


def chair(draw, x, y, upholstery, facing_back=False):
    draw.ellipse((x - 5, y + 3, x + 5, y + 8), SHADOW)
    draw.rectangle((x - 4, y + 4, x - 3, y + 7), WOOD_DARK)
    draw.rectangle((x + 3, y + 4, x + 4, y + 7), WOOD_DARK)
    draw.rounded_rectangle((x - 5, y - 3, x + 5, y + 5), radius=2, fill=WOOD_DARK, outline=INK)
    draw.rectangle((x - 4, y - 2, x + 4, y + 2), upholstery)
    draw.line((x - 3, y - 2, x + 3, y - 2), fill="#bbc5a0")
    back = y + 3 if facing_back else y - 4
    draw.rounded_rectangle((x - 5, back, x + 5, back + 3), radius=1, fill=WOOD, outline=WOOD_DARK)
    draw.line((x - 3, back + 1, x + 3, back + 1), fill="#edbb84")


def banquette(draw, left, y, cushion_widths):
    right = left + sum(cushion_widths) + 3
    draw.rounded_rectangle((left, y + 8, right + 1, y + 15), radius=3, fill=SHADOW)
    draw.rounded_rectangle((left, y, right, y + 13), radius=2, fill=WOOD_DARK, outline=INK)
    draw.line((left + 2, y + 12, right - 2, y + 12), fill="#b2825d")
    x = left + 2
    for width in cushion_widths:
        draw.rectangle((x, y + 1, x + width - 1, y + 6), "#466b64")
        draw.line((x + 1, y + 2, x + width - 2, y + 2), fill="#88a18a")
        draw.rectangle((x, y + 7, x + width - 1, y + 10), "#739482")
        draw.point((x + width // 2, y + 4), fill="#a9ad8c")
        draw.line((x + width - 1, y + 1, x + width - 1, y + 10), fill="#395755")
        x += width


def wood_table(draw, left, top, right, center_support=False):
    draw.rounded_rectangle((left - 1, top + 5, right + 1, top + 14), radius=3, fill=SHADOW)
    if center_support:
        x = (left + right) // 2
        draw.rectangle((x - 1, top + 7, x + 1, top + 13), WOOD_DARK)
    else:
        for x in (left + 3, right - 5):
            draw.rectangle((x, top + 7, x + 2, top + 13), WOOD_DARK)
    draw.rounded_rectangle((left, top, right, top + 9), radius=2, fill=WOOD_DARK, outline=INK)
    draw.rounded_rectangle((left + 1, top + 1, right - 1, top + 6), radius=2, fill="#dfa872")
    draw.line((left + 3, top + 1, right - 3, top + 1), fill="#f8ce91")
    draw.line((left + 2, top + 7, right - 2, top + 7), fill=WOOD)


def draw_booth(draw):
    banquette(draw, 31, 108, (14, 14, 14, 14))
    for left in (36, 65):
        wood_table(draw, left, 123, left + 23, center_support=True)
        cup(draw, left + 4, 126)
        table_flowers(draw, left + 16, 126)
        chair(draw, left + 4, 137, "#7e9482", facing_back=True)
        chair(draw, left + 18, 137, "#7e9482", facing_back=True)


def draw_window_seating(draw):
    banquette(draw, 137, 55, (24, 24))
    wood_table(draw, 141, 72, 184)
    cup(draw, 147, 75)
    table_flowers(draw, 162, 75)
    draw.rectangle((174, 74, 180, 78), "#9a6658")
    draw.line((175, 76, 179, 76), fill="#dba981")
    chair(draw, 151, 89, "#6a8984", facing_back=True)
    chair(draw, 174, 89, "#6a8984", facing_back=True)


def draw_bistro(draw, x, upholstery):
    chair(draw, x, 108, upholstery)
    draw.ellipse((x - 11, 117, x + 11, 129), SHADOW)
    draw.rectangle((x - 1, 122, x + 1, 129), WOOD_DARK)
    draw.ellipse((x - 10, 115, x + 10, 125), WOOD_DARK, outline=INK)
    draw.ellipse((x - 9, 115, x + 9, 122), "#e2af79")
    draw.line((x - 5, 116, x + 5, 116), fill="#f9cf94")
    cup(draw, x - 5, 118)
    table_flowers(draw, x + 3, 118)
    chair(draw, x, 134, upholstery, facing_back=True)


def draw_menu_sign(draw):
    draw.ellipse((136, 165, 161, 172), SHADOW)
    draw.polygon(((139, 147), (154, 147), (160, 170), (152, 168)), "#79533f", INK)
    draw.line((154, 151, 158, 168), fill="#b4835a")
    draw.polygon(((139, 146), (157, 146), (155, 168), (136, 168)), "#aa7350", INK)
    draw.polygon(((140, 148), (155, 148), (153, 165), (138, 165)), "#344b4b", WOOD_DARK)
    draw.line((138, 169, 138, 171), fill=WOOD_DARK)
    draw.line((153, 169, 153, 171), fill=WOOD_DARK)
    for x, y in ((140, 149), (153, 149), (139, 164), (152, 164)):
        draw.point((x, y), fill=BRASS)
    draw.line((144, 152, 150, 152), fill="#f7daa1")
    draw.line((144, 153, 145, 155, 149, 155, 150, 153), fill="#f7daa1")
    draw.line((141, 158, 151, 158), fill="#acba9c")
    draw.line((142, 160, 150, 160), fill="#90ab96")
    draw.line((141, 162, 147, 162), fill="#cad0ab")


def draw_planter(draw):
    plant(draw, 29, 163, "#b86f54")


def draw_front_window(draw, x):
    draw.rectangle((x, 117, x + 49, 148), WOOD_DARK, outline=INK)
    draw.rectangle((x + 2, 120, x + 47, 145), "#506a6b")
    draw.rectangle((x + 4, 121, x + 45, 143), "#789088")
    draw.rectangle((x + 4, 131, x + 45, 143), "#cd9b6b")
    draw.polygon(
        ((x + 9, 121), (x + 16, 121), (x + 4, 139), (x + 4, 128)),
        "#a5b19d",
    )
    draw.polygon(
        ((x + 39, 121), (x + 43, 121), (x + 29, 143), (x + 25, 143)),
        "#a9b098",
    )
    draw.line((x + 2, 130, x + 47, 130), fill="#425c5d", width=2)
    draw.line((x + 24, 120, x + 24, 144), fill=INK, width=2)
    draw.rectangle((x - 1, 145, x + 50, 148), "#ead3a0", outline=WOOD_DARK)
    draw.line((x + 1, 146, x + 48, 146), fill="#f8ddb0")


def draw_facade(draw):
    draw.rectangle((20, 103, 203, 153), "#d2a076", outline=INK)
    draw.rectangle((23, 107, 200, 147), "#e9c38d")
    draw.rectangle((22, 148, 201, 153), "#946750", outline=INK)
    draw.line((23, 151, 200, 151), fill="#bc906c")
    for x in (26, 87, 132, 193):
        draw.rectangle((x, 114, x + 4, 147), "#b58260")
        draw.line((x + 1, 115, x + 1, 145), fill="#f0d29c")
        draw.rectangle((x - 1, 145, x + 5, 148), "#c4966a", outline="#9a6d52")
    draw_front_window(draw, 34)
    draw_front_window(draw, 140)

    draw.rectangle((96, 115, 127, 153), WOOD_DARK, outline=INK)
    draw.rectangle((98, 118, 125, 150), "#426366", outline=INK)
    draw.rectangle((100, 123, 123, 142), "#799189")
    draw.polygon(((105, 123), (109, 123), (100, 135), (100, 130)), "#abb5a0")
    draw.polygon(((119, 123), (123, 123), (115, 136), (111, 136)), "#a1ad9a")
    draw.rectangle((100, 140, 123, 148), "#b38159")
    draw.line((100, 140, 123, 140), fill="#d4a476")
    draw.line((111, 118, 111, 149), fill=INK, width=2)
    for x in (107, 116):
        draw.line((x, 137, x, 139), fill=BRASS)
    draw.line((98, 152, 125, 152), fill="#dfb789")

    draw.polygon(
        ((94, 113), (129, 113), (135, 122), (135, 125),
         (88, 125), (88, 122)),
        TEAL, INK,
    )
    for x in (97, 109, 121):
        draw.polygon(((x, 114), (x + 5, 114), (x + 6, 122), (x - 1, 122)), CREAM)
        draw.line((x - 1, 123, x + 6, 123), fill="#c6986e")
    draw.line((89, 124, 134, 124), fill="#335456")

    for x in (91, 132):
        draw.line((x, 129, x, 136), fill=INK, width=2)
        draw.rectangle((x - 2, 132, x + 2, 137), BRASS, outline=WOOD_DARK)
        draw.point((x, 134), fill="#fff0b2")


def draw_roof(draw):
    draw.polygon(
        ((21, 13), (202, 13), (209, 20), (209, 106), (204, 113),
         (19, 113), (14, 107), (14, 20)),
        INK,
    )
    draw.rectangle((18, 17, 205, 100), "#3c6061", outline="#244146")
    draw.rectangle((21, 20, 202, 97), TEAL)
    draw.line((21, 19, 202, 19), fill="#6e9893")

    for index, x in enumerate(range(25, 197, 12)):
        draw.rectangle((x, 22, x + 9, 97), "#4b7879" if index % 3 == 1 else "#407174")
        draw.line((x, 22, x, 97), fill="#31575a")
        draw.line((x + 1, 24, x + 1, 96), fill=TEAL_LIGHT)
        y = 33 + index % 5 * 9
        draw.line((x + 3, y, x + 6, y), fill="#568488")
        draw.point((x, 96), fill="#86a69a")

    draw.rectangle((16, 99, 207, 110), "#4d7473", outline=INK)
    draw.line((18, 100, 205, 100), fill="#94ab9c")
    draw.line((18, 106, 205, 106), fill="#325557")
    draw.line((20, 110, 203, 110), fill="#263e42")
    draw.line((23, 112, 200, 112), fill="#bf9169")

    draw.rectangle((164, 38, 186, 51), "#345b5d")
    draw.rectangle((162, 34, 183, 49), "#667f77", outline=INK)
    draw.rectangle((161, 32, 184, 39), "#a1aa93", outline=INK)
    draw.line((163, 33, 182, 33), fill="#c8c5a4")
    for x in range(164, 183, 3):
        draw.line((x, 36, x, 37), fill="#607873")
    draw.rectangle((164, 41, 181, 46), "#586e69")

    draw.rectangle((70, 81, 154, 103), "#29494d")
    draw.rectangle((72, 78, 151, 101), WOOD_DARK, outline=INK)
    draw.rectangle((75, 80, 148, 98), "#efdfb1")
    draw.line((76, 81, 147, 81), fill="#fff0c7")
    draw.line((76, 97, 147, 97), fill="#bb9671")
    pixel_text(draw, (93, 84), "HAZEL", "#36565b", scale=2)
    for x in (82, 141):
        draw.line((x - 2, 89, x + 2, 89), fill="#b88053")
        draw.line((x, 87, x, 91), fill="#b88053")


# Scene-space crop boxes, atlas positions, and painters in back-to-front order.
# Match the atlas rectangles in cafe_furniture.png.meta when moving a crop.
INDOOR_PROPS = (
    ((28, 47, 98, 73), (1, 1), draw_prep_counter),
    ((134, 53, 193, 100), (70, 39), draw_window_seating),
    ((28, 72, 101, 106), (74, 1), draw_service_counter),
    ((132, 103, 162, 144), (132, 39), lambda draw: draw_bistro(draw, 144, "#739085")),
    ((167, 103, 197, 144), (1, 81), lambda draw: draw_bistro(draw, 185, "#a47b66")),
    ((29, 107, 95, 146), (1, 39), draw_booth),
)
PLANTER_BOUNDS = (21, 150, 38, 173)
PORCH_PROPS = (
    ((135, 145, 162, 173), (150, 1), draw_menu_sign),
    (PLANTER_BOUNDS, (34, 81), draw_planter),
)


def draw_interior():
    interior = Image.new("RGBA", SIZE)
    draw = ImageDraw.Draw(interior)
    draw_entry(draw)
    draw_floor(draw)
    draw_back_wall(draw)
    return interior


def draw_exterior_overlay():
    exterior = Image.new("RGBA", SIZE)
    draw = ImageDraw.Draw(exterior)
    draw_facade(draw)
    draw_roof(draw)
    return exterior


def draw_furniture():
    atlas = Image.new("RGBA", ATLAS_SIZE)
    furniture = Image.new("RGBA", SIZE)
    porch = Image.new("RGBA", SIZE)
    for preview, props in ((furniture, INDOOR_PROPS), (porch, PORCH_PROPS)):
        for bounds, atlas_position, paint in props:
            layer = Image.new("RGBA", SIZE)
            paint(ImageDraw.Draw(layer))
            prop = layer.crop(bounds)
            atlas.paste(prop, atlas_position)
            preview.alpha_composite(prop, bounds[:2])
    porch.alpha_composite(porch.crop(PLANTER_BOUNDS), (186, 150))
    return atlas, furniture, porch


def save_preview(path, interior, exterior, furniture, porch):
    outside = Image.alpha_composite(interior, exterior)
    outside.alpha_composite(porch)
    inside = Image.alpha_composite(interior, furniture)
    inside.alpha_composite(porch)

    preview = Image.new("RGB", (488, 212), "#e7e0d2")
    draw = ImageDraw.Draw(preview)
    for x, layer in ((12, outside), (248, inside)):
        draw.rounded_rectangle((x, 9, x + 228, 202), radius=8, fill="#f6f0e3")
        preview.paste(layer, (x + 2, 10), layer)
    path.parent.mkdir(parents=True, exist_ok=True)
    preview.resize((1464, 636), Image.Resampling.NEAREST).save(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--preview", type=Path, help="Optional comparison PNG")
    args = parser.parse_args()

    interior = draw_interior()
    exterior = draw_exterior_overlay()
    atlas, furniture, porch = draw_furniture()
    args.output.mkdir(parents=True, exist_ok=True)
    interior.save(args.output / "cafe_interior.png")
    exterior.save(args.output / "cafe_exterior_overlay.png")
    atlas.save(args.output / "cafe_furniture.png")
    if args.preview:
        save_preview(args.preview, interior, exterior, furniture, porch)


if __name__ == "__main__":
    main()

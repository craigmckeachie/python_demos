html_colors = {
    "AliceBlue": "#FOF8FF",
    "AntiqueWhite": "#FAEBD7",
    "Aqua": "00FFFF"
}


# Copy a dictionary

# html_colors2 = html_colors.copy()

# print(html_colors2)
# print(html_colors2 == html_colors)
# print(html_colors2 is html_colors)
# print(id(html_colors2), id(html_colors))

# Update a dictionary

# html_colors.update({
#     "Aquamarine": "#7FFFD4",
#     "Azure": "#F0FFFF"
# })

# print(html_colors)

# Merge Dictionaries

html_colors2 = {
    "Aquamarine": "#7FFFD4",
    "Azure": "#F0FFFF"
}

# html_colors_merged = html_colors | html_colors2  # Python 3.9+ only
html_colors_merged = {**html_colors, ** html_colors2}

print(html_colors_merged)
print(id(html_colors), id(html_colors2), id(html_colors_merged))

# Reference about different merge syntaxes: https://stackoverflow.com/a/26853961/48175

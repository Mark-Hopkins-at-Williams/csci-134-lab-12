BASIC = {
    'window width': 440,
    'window height': 600,
    'initial y velocity': 5.0,
    'min x velocity': 1.0,
    'max x velocity': 3.0,
    'num balls': 3,
    'time step': 10
}

SIMPLE = BASIC | {
    'color map': {"R": "#FF0000", 
                  "G": "#00FF00", 
                  "B": "#0000FF", 
                  "X": None},
    'color matrix': ["BRXG",
                     "GBRB"],
    'outline bricks': True
}

CLASSIC = BASIC | {
    'color map': {"O": "orange", "G": "green", "B": "blue",
                  "R": "red", "C": "cyan"},
    'color matrix': ['R'*10, 'R'*10, 'O'*10, 'O'*10, 'G'*10, 'G'*10,
                     'C'*10, 'C'*10, 'B'*10, 'B'*10],                     
    'outline bricks': True
}

BUNSEN = BASIC | {
    'color map': {"G": "#A9C353", "P": "#9E7A3F", 
                  "B": "#000000", "X": None},
    'color matrix': ['XGGGGGGGGGX',
                     'BGBBBGBBBGB',
                     'BBBGBBBGBBB',
                     'GGBBBGBBBGG',
                     'GGGGGGGGGGG',
                     'GGGGGPGGGGG',
                     'XGGGGGGGGGX'],
    'outline bricks': False
}

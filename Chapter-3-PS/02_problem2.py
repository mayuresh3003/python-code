letter = ''' Dear <|Name|>, 
             Your are selected! 
             <|Date|> '''

print(letter.replace("<|Name|>", "Kaal").replace("<|Date|>", "03-Nov-2021"))
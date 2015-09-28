a = "  <list> " # <put your EMAIL ID list here>
count = 0
for i in a:
    if i == ',': # <change the ',' to '@' if the emailIDs are not comma separated>
        count+=1
print count # <run program in terminal by typing -> " python <filename>.py " (do not include quotes) >

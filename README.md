
# discord channel downloader

downloads all images sent to a channel. its that easy.

## how do i set it up

get discord bot token. put it in file called `tokenfile`. run `main.py` using `./main.py <CHANNEL ID> [PATH]`. `PATH` is optional. CHANNEL ID is the channel from which it downloads all images.

## what does it do

downloads files. the file name format is `<PATH>/<AUTHOR NAME FIXED>-<MESSAGE CONTENT FIXED>.png`. FIXED meaning it changes all character that cannot be in a file name on windows.
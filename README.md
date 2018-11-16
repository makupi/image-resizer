## RESIZE

A small tool to potentially help emote artists resize their images faster/easier.

## Config

The folders and sizes can be configured in the `config.json` file.   
Structure of the file:
```json
{
    "twitchEmotes": {
        "sizes": [112, 56, 28],
        "inputFolder": "in_emotes", 
        "outputFolder": "out_emotes"
    },
    "subBadges": {
        "sizes": [72, 36, 18],
        "inputFolder": "in_badges",
        "outputFolder": "out_badges"
    }    
}
```
`twitchEmotes` and `subBadges` are the default configurations.    
Each key has an object with the `sizes` as an array of intergers and two strings with `inputFolder` and `outputFolder`.

## Usage

- Put all your .png files that you want to be resized in the `in_emotes` folder and run the `resize.exe`.     
- It will automatically resize them to the sizes mentioned above and put them into the `out_emotes` folder named as `file_size.png` (e.g. Kappa_112.png).

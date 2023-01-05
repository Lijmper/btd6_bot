Download and unzip everything into a single folder, does not matter where.

Run
pip install -r requirements.txt
inside of your vscode terminal (or path terminal, whichever you're using).

Open main.py and run it, a gui will now open. Make sure you have the right hero selected if a hero name is mentioned in the strategy and start on an empty run while the game is unpaused. Run main.py and alttab to BTD6 and wait 3 seconds.

Syntax for making your own strategy:

build('monkeytype', x-coordinate, y-coordinate, 'upgrade path as a string', targeting option (1 for last, 2 for close, 3 for strong and 0 or nothing for first)
build('alchemist', 736, 593, '402', 2)

monkeys = {
'hero':'u',
'dart':'q','boomerang':'w','bomb':'e','tack':'r','ice':'t','glue':'y',
'sniper':'z','sub':'x','buccaneer':'c','ace':'v','heli':'b','mortar':'n','dartling':'m',
'wizard':'a','super':'s','ninja':'d','alchemist':'f','druid':'g',
'spac':'j','village':'k','engineer':'l'
}
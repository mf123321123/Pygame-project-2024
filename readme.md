# Pygame project

### Programming level 1

#### Instructions to run
* The way to play the game is to dodge the monsters in the cave
* Left arrow key is to move left, right arrow key is to move right, and the up arrow key is to jump, there is gravity, and you can double jump
* You will respawn 5 seconds after you die

#### Bugs
* You hop once when you run the game (I don't know why)

* When you hold the left arrow key, the character does a weird thing where it turns left and right very quickly, it's probably because I made it implemented moving left as times the velocity negative, so when you hold it it times the negative and the positive both, which causes it to turn left and right. (I kept it though because I thought it was cool)

* You die when it didn't look like you touched the monster. (I have no clue how to fix it)

* Game freezes when you die for like a few seconds then black screen with texts comes out after (I don't know why)

* After you respawn, your first contact with the creatures doesn't show the black screen when you die, the player position just gets reseted (I don't know why)

#### Attribution

* Used OpenAI's ChatGPT for attempting to change hitbox & have some help with lines 313 to 355
* Used the game examples to add background image

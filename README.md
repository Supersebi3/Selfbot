**Selfbotting is not allowed as per Discord's Terms of Service. This repo is not maintained and not in use by anyone I know of. I will keep it up merely as an example. I do not encourage anyone to use this.**

# My selfbot (no specific name)
## Introduction
This is my discord.py selfbot. It's pretty small and simple, but in my opinion it is pretty useful for everyday Discord chatting. If you have any suggestions, please contact me in Discord (Supersebi3#3525) as I'm not really used to GitHub yet. Thanks!

## Setting up
After getting all the files, install discord.py by entering `pip install discord.py` into a command prompt. Then just fill in the `config.json` file with your Discord user token and your desired prefix for the bot (I recommend `/`). Now run `main.py`, wait for it to log that the bot is ready, and you can start using your new selfbot!

## How to use
The usage of this selfbot is split into 3 parts: **Commands**, **Replacements** and **Expressions**.

### Commands
There is a number of simple commands this selfbot provides, which help you manage your Discord life easily (In the following chart, `<p>` denotes your prefix):

Command | Usage | Description | Notes
------- | ----- | ----------- | -----
help | `<p>help` | Lists all the commands. | This shows in chat, be careful!
nickme | `<p>nickme New nickname` | Changes your nickname in the current server. | This is basically the `/nick` from Desktop Discord, but it works on mobile, too.
d | `<p>d` | Deletes the last message you sent. | This works cross-servers.
e | `<p>e New content` | Edits your last message. | This works cross-servers.
(un)load | `<p>(un)load ExtensionName` | Loads/Unloads a discord.py extension file. | All the other commands are in the extension `SelfbotUtility`.

### Replacements
Replacements are a list of special character sequences in your messages that, if present, get replaced with other strings using an instant edit.

The following chart shows all of them:

Before | After | Notes
------ | ----- | -----
`{shrug}` | The shrug emoji | Similar to Discord built-in `/shrug`, except usable anywhere in your message
`{tableflip}` | The tableflip emoji | Similar to Discord built-in `/tableflip`, except usable anywhere in your message
`{unflip}` | The unflip emoji | Similar to Discord built-in `/unflip`, except usable anywhere in your message
`{lenny}` | The lenny emoji | Discord should add `/lenny`
`{time}` | The current time (HH:MM:SS) | Timezone depends on where your running bot is located
`{date}` | The current date (Monthname DD, YYYY) | See above
`{timestamp}` | Equivalent to `{date} at {time}` | See above
`{year}` | Current year (YYYY) | See above
`{month}` | Full name of the current month | See above
`{mon}` | Short name of the current month | See above
`{weekday}` | Name of the current day of the week (e.g. Monday) | See above
`{wday}` | Short name of the current weekday (e.g. Mon) | See above
`{day}` | Number of the current day (DD) | See above
`{timezone}` | The timezone you're in (e.g. CEST) | See above
`@me` | A mention to you | Useful in DMs (Self-mentions are bugged there)
`:skin-tone-1:`-`:skin-tone-5:` | The corresponding skin tone modifier | Meant for use on mobile (write `:ok_hand::skin-tone-5:`)
*Your user token* | woah I almost told you my token | Protection against token leak

### Expressions
Expressions are, in my opinion, the most powerful thing in this selfbot.
Expressions always take the shape of `{{exprname:exprvalue}}` where `exprname` is the name of an expression (chart below) and `exprvalue` is the value to pass. After being evaluated, results get edited into the messages where the expressions used to be.

Name | Effect | Notes
---- | ------ | -----
eval | The passed value is treated as a raw Python statement, which is evaluated using the `eval` function. | Expressions that look the same will be replaced with the same values in a single message, so be careful with random numbers or other changing values!
char | Takes a mathematical Python expression as value, evaluates it and then returns the unicode character at that codepoint. | Make sure that the entered expression returns an integer number, otherwise you will get an error!
vapor | Turns the entered value into vaporwave text. | No notes needed

## Ending notes
I hope you have fun with this selfbot, if you have any suggestions please contact me on Discord, as stated in the introduction. See you soon!

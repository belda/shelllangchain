# GPT for your terminal

* Do you want to use ChatGPT in your terminal? Well, now you can!
* Do you always forget the syntax for a for loop? Well, now you can ask GPT to write it for you! 
* It is a superfast way to get your commands quickly written for you.
* Use ChatGPT in bash or zsh.

Unleash the Power of GPT in Your Terminal. A Python-based tool that integrates OpenAI's GPT models into your command line, enabling you to quickly generate shell commands and automate tasks. Whether you need help remembering syntax or crafting complex commands, ShellLangChain streamlines your workflow by bringing AI assistance right to your terminal. Easy to install, and customizable with support for various GPT models, this tool is perfect for developers, system administrators, and anyone looking to enhance their terminal experience with cutting-edge AI technology.

## How it works
Using langchain the command takes all the arguments and passes that to the OpenAI API. 
The response is then parsed and the command is printed to the terminal including a short description of what it does. 
The command is also copied to your clipboard and so you can paste it in your terminal.

NOTE: no data is shared from your system, only the natural language you pass it is sent to the OpenAI API.

```
$ slc list all files in current folder
ls

To list all files in a folder, you can simply use the ls command without any options. This will display the names of all files and directories in the current directory.
$
```
After that the command is ready in your clipboard and you can paste it in your terminal.

## Requirements
- OpenAI API key (https://help.openai.com/en/articles/4936850-where-do-i-find-my-api-key)

## Installation

### Using pip
```
pip install --user shelllangchain
```
Depending on your shell you might need to add the following line to your .bashrc or .zshrc file:
```
export OPENAI_API_KEY=<your_openai_api_key>
```
You can now use the `slc` command in your terminal.


### From source
If you want to modify this script, or replace chat-gpt-3.5 with another model, you can do so by cloning this repo and 
modifying the scripts.

Clone this repo and add the scripts to your PATH variable (bin folder should be on your $PATH).
create a .env file in the root of this repo and add the following line:

```
OPENAI_API_KEY=your_openai_api_key
```

### Tip
You can also make _slc_ your fallback command, when you type a command that is not found in your PATH, it will be passed to _slc_.
To do that you add the following line to your .bashrc file:
```
command_not_found_handle () {
    slc "$1"
    return $?
}
```


## Examples

```
$ slc get all images in folder and crop them to square while preserving aspec ratio

mogrify -path <output_directory> -resize '500x500^' -gravity center -extent 500x500 <input_directory/*.jpg>

To get all images in a folder and crop them to a square while preserving the aspect ratio, you can use the mogrify command from the ImageMagick package.

Here's how the command works:

- mogrify is a command-line tool used to resize and modify images.
- -path <output_directory> specifies the output directory where the modified images will be saved.
- -resize '500x500^' resizes the images to fit within a 500x500 square, preserving the aspect ratio. The '^' symbol is used to only resize images that are larger than the specified dimensions.
- -gravity center -extent 500x500 crops the resized images to a 500x500 square by adding whitespace or extending the image if necessary.
- <input_directory/*.jpg> specifies the input directory where the original images are located. Replace '.jpg' with the appropriate file extension if needed.

Make sure to replace <input_directory> and <output_directory> with the actual directory paths on your system.
$ 
```

```
$ slc find all photos larger than 5MB and resize them so their dimensions are at most 2k resolution while preserving aspect ratio
find . -type f -size +5M -exec convert {} -resize '2000x2000>' {} \;

To find all photos larger than 5MB, we can use the find command with the following options:
        . represents the current directory
        -type f filters only regular files
        -size +5M specifies files larger than 5MB

The -exec option allows us to run a command on each file found. In this case, we use the convert command (part of ImageMagick) to resize the photos.
        {} is a placeholder that represents each file found
        -resize '2000x2000>' resizes the image to a maximum width or height of 2000 pixels while preserving the aspect ratio
        {} is again used as a placeholder for the output file

Finally, we end the command with \; to indicate the end of the -exec command.
$ 
```

```
$ slc take all the .txt files in a given folder and join them in alphabetically to file out.txt
cat `ls -1v /path/to/folder/*.txt` > out.txt

The command ls -1v /path/to/folder/*.txt lists all the .txt files in the given folder in alphabetical order.

The output of the ls -1v /path/to/folder/*.txt command is passed as arguments to the cat command. The cat command concatenates the contents of all the input files and outputs the result to the out.txt file.

So, all the .txt files in the given folder are joined in alphabetical order and saved in the out.txt file.

```
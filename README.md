# GPT for your terminal

Do you want to use ChatGPT in your terminal? Well, now you can!
Do you always forget the syntax for a for loop? Well, now you can ask GPT to write it for you!
It is a super fast way to get your commands quickly written for you.

## Usage
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


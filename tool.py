import click, os
from collections import defaultdict


@click.group()
def cli():
    pass


# removes comments
@cli.command()
@click.argument("file", type=click.Path(exists=True), required=1)

def rem(file):
    
    
    check_type = find_type(file)
    if check_type == '':
        click.echo('Not A Supported language')
        return 1;
    

    with open(file, "r") as fileR:
        NewText = fileR.read()
    CleanText = ""
    NewText = NewText.splitlines("\n")
    for lines in range(len(NewText)):
        
        for num, letter in enumerate(NewText[lines]):
            if letter == check_type:
                CleanText += '\n'
                break
            CleanText += letter
    
    #adding the clean out text into the original file
    with open(file, "w") as fileW:
        fileW.write(CleanText)

    click.echo("Successful clean")
def find_type(file):
    
    lang_dict = defaultdict(str)
    lang_dict['js'] = '//'
    lang_dict['py'] = '#'
    
    for i in range(len(file)):
        if file[i] == '.':
            return lang_dict[file[i+1:]]
    
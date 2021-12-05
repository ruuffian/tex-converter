# tex-converter

This is a pretty simple python script to convert a .md file from dollar sign latex syntax to a github img link as a 
workaround for to display beautiful latex in your github READMEs.

### Use

Invoke the script using ./main.py -i inputfile -o outputfile
> -o is an optional flag, if you dont specify an output file the script will over
write the input file.

### Example

This is the latex syntax used by most latex parsers:

>$a\cdot a = \lvert a \rvert$

As you can see, it doesn't display in a regular markdown file. However, github has an inline latex renderer that you can
'hack' to display any latex, as long as you encode it. For example, 

><img src="https://render.githubusercontent.com/render/math?math=a%5Ccdot%20a%20%3D%20%5Clvert%20a%20%5Crvert">

renders perfectly! This is achieved by encoding and inserting the above latex into a markdown image tag.

This script also works with with latex that follows double $ syntax to create the image on a newline:

>$$\boxed{\vec{v}\cdot\vec{u} = ax+by+cz}$$

renders to 

><img src="https://render.githubusercontent.com/render/math?math=%5Cboxed%7B%5Cvec%7Bv%7D%5Ccdot%5Cvec%7Bu%7D%20%3D%20ax%2Bby%2Bcz%7D">


It should also support any kind of **\beginarray**  latex as long as it is wrapped in dollar signs.


###Contributing

This is a fun little sideproject I have, so feel free to make any changes that you would like to see. Feel free to make a pull
request!
### License

This software is under the MIT License as seen in [LICENSE](LICENSE.md)

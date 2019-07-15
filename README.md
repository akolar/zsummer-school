# Summer school - Package Installation



## Installation



### Prerequisites

#### Git

If you don't have Git installed on your system, you should follow the official installation guide (<https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>).

#### Mac

Brew: <https://brew.sh/>

#### Linux

Package manager distributed by your OS (apt, pacman+AUR, etc.)

#### Windows

/



**Note regarding shells**: You should preferably have `sh` or `bash` or `zsh` installed on your systems. For the puroposes of this tutorial, try avoiding `fish` due to a slightly different syntax.


### PyEnv

Mac: Install using brew: `brew install pyenv`

Arch: Install from AUR (<https://www.archlinux.org/packages/community/any/pyenv/>)

Ubuntu: <https://gist.github.com/jmvrbanac/8793985>

Windows: <https://github.com/pyenv-win/pyenv-win>



```
pyenv 1.2.9
Usage: pyenv <command> [<args>]

Some useful pyenv commands are:
   commands    List all available pyenv commands
   local       Set or show the local application-specific Python version
   global      Set or show the global Python version
   shell       Set or show the shell-specific Python version
   install     Install a Python version using python-build
   uninstall   Uninstall a specific Python version
   rehash      Rehash pyenv shims (run this after installing executables)
   version     Show the current Python version and its origin
   versions    List all Python versions available to pyenv
   which       Display the full path to an executable
   whence      List all Python versions that contain the given executable

See `pyenv help <command>' for information on a specific command.
For full documentation, see: https://github.com/pyenv/pyenv#readme
```

You should also let pyenv initialize itself everytime you spawn a new terminal session by adding  `eval "$(pyenv init -)"`  to your `.bashrc` (or similar).

Pyenv allows you to have multiple python versions installed on your system and is able to switch between them based on working directory.



```
❯ pyenv install 3.7.2

❯ pyenv versions
  system
* 3.7.1 (set by /Users/anze/.pyenv/version)
  3.7.2
```

**Note for Mac users**: Should the build fail with , install `zlib` (`brew install zlib`) and run the command again using `❯ LDFLAGS="${LDFLAGS} -L/usr/local/opt/zlib/lib" CFLAGS="${CFLAGS} -I$(xcrun --show-sdk-path)/usr/include" CPPFLAGS="${CPPFLAGS} -I/usr/local/opt/zlib/include" PKG_CONFIG_PATH="${PKG_CONFIG_PATH} /usr/local/opt/zlib/lib/pkgconfig" pyenv install 3.7.2`



Create a new directory -- you will use it for your Summer School projects.

```
~
❯ mkdir summer_school

~
❯ cd summer_school

~/summer_school
❯ pyenv local 3.7.2
```



This will create a new file `.python-version` in `$PWD`. Python inside this directory now points to the one installed by pyenv.

```
~/summer_school
❯ which python
/Users/anze/.pyenv/shims/python
```



Next, we install `pipenv` which will be used for managing our project and initialize our workspace (virtual environment). Virtual environments allow you to have multiple self-contained sets of packages installed. They use python binary made available by your system (which is why it's good to manage them using pyenv so you can upgrade the system version independently without breaking all your virtual environments).

 

```
❯ pip install -U pipenv

~/summer_school
❯ pipenv install
Creating a virtualenv for this project…
Pipfile: /Users/anze/summer_school/Pipfile
Using /Users/anze/.pyenv/versions/3.7.2/bin/python3.7 (3.7.2) to create virtualenv…
⠙ Creating virtual environment...
[...]
```



This will create Pipfile and Pipfile.lock in your `$PWD` which are used for managing dependencies.

**Sidenote**: Pipenv is the officially recommended way of managing project dependencies. No more requirements.txt and manually managed virtualenvs.

To activate your virtual environment execute the following command `pipenv shell`. You will have to do this everytime you want to enter your virtual environment (and interact with your installed packages).



Tip: check out `direnv`, a tool that will allow you to automatically run commands based on the directory you are in.



### Install packages



**Note**: You can clone <https://github.com/akolar/zemanta-summer-school> to get the pipenv we prepared for you. To get it setup, run

```
git clone https://github.com/akolar/zemanta-summer-school summer-school
cd summer-school
pipenv install
```



We'll use many different packages this week. At the very least, you should install the following:



- jupyter
- numpy
- scikit-learn
- pandas
- scipy
- matplotlib
- requests



```
pipenv install jupyter numpy scikit-learn pandas scipy matplotlib requests
```



### Shell

**Note for Windows users**: you will either have to access the Ubuntu Sub System or install <https://www.cygwin.com/>.

**Note**: we'll be trying out the following commands: `cat`, `awk`, `tr`, `cut`, `jq`, `sort`, `uniq`, `gzip`, `wc`. You should check if they are installed on your system (`which <command>`) and install them using `apt/pacman/...j` if you don't have them yet.





## Demo



Launch a jupyter notebook from your virtual environment.

```
❯ pipenv shell
Launching subshell in virtual environment…
 . /Users/anze/.virtualenvs/summer_school-kd1XxMt2/bin/activate
 
 summer_school-kd1XxMt2 ❯ jupyter notebook
 [I 16:20:41.211 NotebookApp] Serving notebooks from local directory: /Users/anze/summer_school
[I 16:20:41.211 NotebookApp] The Jupyter Notebook is running at:
[I 16:20:41.211 NotebookApp] http://localhost:8888/?token=5674e61d20b3b7529ce9237f5b37b5c92bc138df0909abd0
[I 16:20:41.211 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 16:20:41.316 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///Users/anze/Library/Jupyter/runtime/nbserver-84984-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/?token=5674e61d20b3b7529ce9237f5b37b5c92bc138df0909abd0
```



You can either follow along the provided notebook or create your own.





## Shell



Contrary to popular belief, bash scripts are one of the most important tools in a data scientist's arsenal. They allow for quick ad-hoc analysis, have streaming capabilities (useful when filtering terabytes of data) and are easy to use once you get a hang of the workflow.



We've prepared three simple tasks for you which should provide you with an oportunity to leverage the power of those tools to your advantage. Although the sample data we give you is small, the exact same concepts could be used on files hundred times the size.



**Note**: Eventhough these exercises might seem like something you get to do at college for homework, they do have real-life applications. All of them are based on solutions we used to analyze our production inputs and outputs in the past few months.



### Most useful commands

#### `grep`

`grep` can be used to filter lines based on their content. For example, if you want to only select lines that contain the word "foo", you could do:

```
echo "
foo,1
bar,2
baz,3
" | grep "foo"
```

Obviously, this doesn't work if you have "foobar" in one of the lines. In such cases it's useful to know how your data looks like -- in our case, we're only interested in the line if the word "foo" appears in the first column:

```
echo "
foo,1
foobar,1
foobar,foobar
bar,2
baz,3
" | grep "^foo,"
```

If you only want to select examples that _do not_ include "foo", pass `-v` flag.

```
echo "
foo,1
bar,2
" | grep -v "^foo,"
```

For case-insnsitive matching, pass the `-i` flag.

```
echo "
foo,1
FOO,3
bar,2
" | grep -i "^FOO,"
```


#### `sort`

`sort` internally uses a variation of bucket sort so it can work with data of arbitrary sizes.


```
echo "
3
20
1
0
a" | sort
```

If you're only sorting numbers, you should pass either `-g` or `-n` flag:

```
echo "
3
20
1
0" | sort -n
```

You can select the column used as a sorting key by specifing `-k <n>` flag, where `n` is the index of the column.

```
echo "
1,3
2,20
3,1
4,0" | sort -k2 -t ',' -n
```

#### `uniq`

`uniq` only select unique rows from the output. Input must (on most systems) be sorted.

```
echo "1
1
2" | sort | uniq
```

If you pass `-c` as a flag, `uniq` will also report the number of occurances.

```
echo "a
b
a" | sort | uniq -c
```

#### `head` and `tail`

`head` and `tail` report the first and last `n` lines in a file, respectively.

```
echo "a
b
a" | tail -n 1
```

#### `tr`

`tr` is used for substituting characters in the input.


```
echo "string    with many    spaces" | tr -s ' '
```

```
echo "a b c d e f" | tr ' ' '_'
```

```
echo "a b c d e f" | tr -d ' '
```

#### `cut`

`cut` allows you to split and select columns from the input text.

```
echo "1 2 3 4 5 6 7 8 9 10" | cut -d ' ' -f1,2 -f5,7 -f10,10
```




### Tasks

Data generators are provided inside `generators/`.


#### Task 1

You are given an input in a JSON format; each line contains a JSON with the following structure: `{}`. Extract `feature1,feature2,class` and transform the input to a CSV format. Select only lines with class either `2` or `10`. Sort the output by class and save it to a file.

<details><summary>Solution</summary><p>

```
cat data.txt |
    jq -r '[.class,.feature1,.feature2] | @csv' |
    grep -E '^(2|10),' |
    sort -n > out.txt
```

</p>
</details>



#### Task 2

You are given a list of labeled samples (`classes = [0,1]`). Find out how many of examples belong to each of the classes. If number of examples in class 1 is greater than the number of examples in class 0, print `ERROR`.



<details><summary>Solution</summary><p>

```
cat data.txt |
    tr -s ' ' |
    cut -d ' ' -f 2,2 |
    sort |
    uniq -c |
    sort -n |
    tee /dev/tty |
    tail -n 1 |
    grep 0 >> /dev/null && echo "ERROR"
```

Alternatively, you could -- instead of `tr | cut` -- also use `awk '{print $2}'` (`awk` handles multiple spaces as a single field separator out of the box).

</p>
</details>





#### Task 3

Find all unique IDs (numerical) with factors greater or equal to 1.5. Output each in name and factor in a the following format: `ID,factor`. Preferably, all IDs will be unique with only them maximum factors displayed. Sort them in descending order by the factor column.


<details><summary>Solution</summary><p>

```
cat factors.txt |
    awk '{if($2 > 1.5 && $2 > data[$1]) { data[$1]=$2 } } END { for (k in data) { printf "%4d   %.03f\n", k, data[k] } }' |
    sort -grk2
```

</p>
</details>


#### Task 4

Write a script that monitors changes in an arbitrary text file (e.g. `file.log`) and when it changes `tail`s the last line of `file.log` to `changes.log` along with the current time. At the same time (using the same script or a different one) also save system's free memory to `mem.log` every second.

Try doing this both using `fswatch`/`inotify` as well as manually.



<details><summary>Solution</summary><p>

```
file="file.log"
while true; do
	hash=$(md5sum "$file")
	if [ "$hash" != "$hash_old" ]; then
		echo "$(date): $(tail -n 3 "$file")" > changes.txt
	fi
	
	echo "$(date): $(vm_stat | grep 'Pages active' | tr -s ' ' | cut -d ' ' -f 3,3 | read pages && python -c "print($pages * 4096 / 1024**2)")" >> mem.log
	hash_old="$hash"
	sleep 1
done
```

</p>
</details>

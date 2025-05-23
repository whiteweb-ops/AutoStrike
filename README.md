# AutoStrike

I developed this project to easily automate manual tools.
It's very easy to use. Specify the path and parameters of the tools in your inventory.

tools.txt example:
/usr/bin/nmap -p- -T3 -Pn {target} --open
/usr/bin/whois --verbose {target}

When you run the autostrike.py file and specify the target, it pulls the parameters from the tools.txt file and runs it, and the output is saved to the output.txt file.
Write your target as example.com when you run the py file
If the tool you are using asks you to specify http or https, write the following in the tools.txt file: http://{target} or https://{target}

# Usage

python3 autostrike.py | set your target url/ip

# YouTube Video

https://youtu.be/8ngbGEdg_wc

# License

This project is licensed under the MIT License

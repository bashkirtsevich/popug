# Python parrot cli args echo lib

Installing:

`pip install git+https://github.com/bashkirtsevich/popug.git`

Example:

```
root@b819542c6d4a:~# pip install git+https://github.com/bashkirtsevich/popug.git
Collecting git+https://github.com/bashkirtsevich/popug.git
  Cloning https://github.com/bashkirtsevich/popug.git to /tmp/pip-req-build-9ut6lyd0
  Running command git clone -q https://github.com/bashkirtsevich/popug.git /tmp/pip-req-build-9ut6lyd0
Building wheels for collected packages: popug
  Building wheel for popug (setup.py) ... done
  Created wheel for popug: filename=popug-0.0.1-py3-none-any.whl size=14455 sha256=3458d4d73d381955e5a980627c0e23e27df7adc4b076b4ad613003c2059cc524
  Stored in directory: /tmp/pip-ephem-wheel-cache-h2liz35r/wheels/b2/8e/ae/3c178a6215851fba4128ff1f528230f55cc90b0848497b4d6e
Successfully built popug
Installing collected packages: popug
Successfully installed popug-0.0.1
WARNING: You are using pip version 21.0.1; however, version 22.3.1 is available.
You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
root@b819542c6d4a:~# 
root@b819542c6d4a:~# popug foo bar baz

              ██████████                                            
            ██░░░░░░░░░░████                                        
          ██░░░░░░░░░░░░░░░░██                                      
        ██░░░░░░░░░░░░░░░░░░░░██                                    
      ██░░░░░░██░░░░░░░░░░░░████                                    
    ██░░░░░░░░██░░████████░░██░░██                                  
    ██░░░░░░░░░░░░██░░░░░░██░░░░██                                  
  ████░░░░░░░░░░░░██░░░░░░██░░░░░░██                                
  ██░░░░░░░░░░░░░░██░░░░░░██░░░░░░░░██                              
██░░░░░░░░░░░░░░░░██░░░░████░░░░░░░░██                              
██░░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░██                              
██░░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░██                              
  ██░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░██                              
    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                            
    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████                        
    ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                      
    ██░░██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                    
    ██░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                  
    ████████████████████████████████████████████████                
----------------------------------------------------
Popug lib demo
    
Arg: 0 	value: /usr/local/bin/popug
Arg: 1 	value: foo
Arg: 2 	value: bar
Arg: 3 	value: baz

```

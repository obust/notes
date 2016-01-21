
# Server

Scyfer has a remote server called ***train-k80***.

NVIDIA Tesla K80 dual-GPU Accelerator

- Two Kepler GK210 chips
- 4992 CUDA cores (2496 per chip)
- 24Gb GDDR5 memory (12Gb per chip)
- 480Gb/s aggregate memory bandwidth
- 8.74 TFLOPS single precision, 2.91 TFLOPS double precision with GPU Boost


Tesla K80 dual-GPU is the new flagship offering of the Tesla Accelerated Computing Platform, the leading platform for accelerating data analytics and scientific computing. It combines the world's fastest GPU accelerators and the widely used CUDA parallel computing model.


with **1 cpu** and **4 gpu** available for calculation. 


## SSH Connection

Secure Shell (SSH) is a UNIX-based command interface and protocol for securely getting access to a remote computer.

### Connection

To **access the remote server** from the terminal, run:

    $ ssh <username>@159.8.221.88
    Password:

If it is the first time you are connecting to the server, you will receive a confirmation. Type "yes" to continue, then enter your password to finalize the connection.

	Welcome to Ubuntu 14.04.2 LTS (GNU/Linux 3.13.0-53-generic x86_64)
	
	<username>@train-k80:~$

You are now connected to the server "train-k80".

	<username>@train-k80:~$ pwd
	/home/<username>

Your remote user directory	is located at `/home/<username>`.  
This is where you will host all your project files.

### Configuration

Since you are going to access the server quite often, it is wise to edit the ssh config file to **automate the connection**.

First, access the `config` file in the `.ssh/` folder:

	$ cd
	$ nano .ssh/config
    
Then add these lines:

    Host <servername>
        HostName 159.8.221.88
        User <username>

Now to connect to the server, simply run :

    $ ssh <servername>
    Password:

### Disconnect

To disconnect, run `logout`, `exit` or use `CTRL+D`:

	<username>@train-k80 $ logout
	Connection to 159.8.221.88 closed.


## GPU

To launch a computation on a certain gpu, use THEANO_FLAGS as follows, choosing from gpu0 to gpu3. Before launching computations you should check if the gpu you plan on using is not used (either ask on #server on Slack or just ask around). 

    $ THEANO_FLAGS='device=gpu0' python yourawesomescript.py

See the GPU usage

	$ nvidia-smi

	
## PyCharm Deployment Configuration

### Creating a Remote Server Configuration
https://www.jetbrains.com/pycharm/help/creating-a-remote-server-configuration.html

Preferences > Build, Execution, Deployment > Deployment

Then click the "+" button to create a Deployment Configuration :

- Name : e.g. `scyfer`

**Connection**

- SFTP Host : `159.8.221.88`
- Port : `22`
- Root path : `/home/<remote_username>`
- User name : `<remote_username>`
- Password : `<remote_password>`

**Mapping**

- Local path : e.g. `/home/<local_username>/Projects/scyfer`
- Deployment path on server : `/`

Finally, in Tools > Deployment , check in "Automatic Upload".

With this deployment configuration, a file or directory from `/home/<local_username>/Projects/scyfer` will be uploaded to your user remote root path `/home/<remote_username>` :

- when you save it within PyCharm
- when you right click on it in the file structure on the left sidebar and select "Upload to *scyfer*".

## Remote Run Control files

### .bashrc

### .theanorc

default device cpu, gpu0, gpu1, gpu2, gpu3
default variable type

### .rc

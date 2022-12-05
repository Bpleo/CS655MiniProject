## CS655MiniProject
***

### Team Memeber
+ Zeyu Su
+ Haijun He
+ Chen Gong
+ Chen Qin
***
### How to compile and run
   
1. **Install Anaconda**
   + Step 1: Download the Anaconda Bash Script
    ```
    cd /tmp
   curl -O https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh
   ```
   + Step 2: Run the Anaconda Script
   ````
   bash Anaconda3-2021.05-Linux-x86_64.sh
   ````
   You’ll receive the following output to review the license agreement by pressing ENTER until you reach the end.
   ```
   Output
   
   Welcome to Anaconda3 2021.05
   
   In order to continue the installation process, please review the license agreement.
   Please, press ENTER to continue
   >>>
   ...
   Do you approve the license terms? [yes|no]
   ```
   When you get to the end of the license, type yes then press ENTER as long as you agree to the license to complete installation.

   Once you agree to the license, you will be prompted to choose the location of the installation. You can press ENTER to accept the default location, or specify a different location.
   ```
   Output
   Anaconda3 will now be installed into this location:
   /home/sammy/anaconda3
   
     - Press ENTER to confirm the location
     - Press CTRL-C to abort the installation
     - Or specify a different location below
   
   [/home/sammy/anaconda3] >>>
   ```
   Once installation is complete, you’ll receive the following output:
   ```
   Output
   ...
   installation finished.
   Do you wish the installer to initialize Anaconda3
   by running conda init? [yes|no]
   [no] >>>
   ```
   It is recommended that you type *yes* to use the conda command.
   
   After entering *yes*, please close the connection and start another ssh connection to the node. Then you can start setting up the environment.
   

2. **Environment setup**
   + Step 1: Download setup.sh from our github and run: 
   
   ````
   wget https://raw.githubusercontent.com/Bpleo/CS655MiniProject/main/setup.sh
   bash setup.sh
   ````
   + Step 2: Activate your conda environment. (Here our environment name is *cs655*.)
   
   ```
   conda activate cs655
   ```
   + Step 3: Download install.sh from our github and run:
    
   ```
   wget https://raw.githubusercontent.com/Bpleo/CS655MiniProject/main/install.sh
   bash install.sh
   ```
    (We highly recommend leave it running and do something else, it can take more than 1 hour to build up the environment)

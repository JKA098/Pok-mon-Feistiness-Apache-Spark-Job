# 🏆 Pokémon Feistiness Apache Spark Job

![Big Data](https://img.shields.io/badge/domain-Big%20Data%20-red)
![Analytics](https://img.shields.io/badge/focus-Data%20Analytics-blueviolet)
![Big Data Stack](https://img.shields.io/badge/tech%20stack-Hadoop%2FMapReduce%2FStreaming-lightblue)
![Environment](https://img.shields.io/badge/setup-Virtual%20Environment-important)
![Isolation](https://img.shields.io/badge/dependency%20isolation-Virtualenv%20%2F%20venv-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Focus](https://img.shields.io/badge/focus-Big%20Data%20Feistiness%20Analysis-blueviolet)
![Theme](https://img.shields.io/badge/theme-Pok%C3%A9mon%20Feistiness-brightgreen)
![Data](https://img.shields.io/badge/data%20source-pokemon.csv-lightgrey)
![Statistics](https://img.shields.io/badge/statistical%20metrics-Attack%2FWeight%20Ratio-blue)
![ML](https://img.shields.io/badge/execution%20mode-Local%20%7C%20YARN-orange)
![Framework](https://img.shields.io/badge/framework-Apache%20Spark-informational)
![Notebook](https://img.shields.io/badge/editor-PySpark%20Script-orange)
![Editor](https://img.shields.io/badge/report-MS%20Excel-blue)


## **1. Prerequisites**
The following readme file, assume that before running the Spark analytic job, you have already installed the correct versions of **Java**, **Hadoop**, **Spark** and that you are inside **Ubuntu**.
Required Software Versions:
- **Ubuntu 24.04** (Recommended inside VirtualBox)
- **Java: Java-8-openjdk-amd64** 
- **Hadoop: hadoop-3.2.3**
- **Apache Spark: spark-3.5.0-bin-hadoop3**


To verify installations:

```bash
java -version
hadoop version
spark-submit --version 
```

---


## **2. Installation Steps**

### Step 1: Install Java
To install the correct version of **Java**, run:

```bash
sudo apt install openjdk-8-jdk
```


To switch between **Java** versions, use:

```bash
sudo update-alternatives --config java # select the desired version and press enter
```


Verify the installation:
```bash
java -version
```

✅ Expected Output:

```bash
openjdk version "1.8.0_442"
```

### If hadoop is not already installed the following link should be helpful:

- https://arjunkrish.medium.com/step-by-step-guide-to-setting-up-hadoop-on-ubuntu-installation-and-configuration-walkthrough-60e493e9370d



---
### Step 2: Install Apache Spark
Follow the following links for installation:
- https://trentu.blackboard.com/ultra/courses/_65448_1/cl/outline
- https://spark.apache.org/docs/latest/api/python/getting_started/install.html
- https://www.youtube.com/watch?v=ei_d4v9c2iA
- https://www.youtube.com/watch?v=lvEN48bWO0o

Go to the website for downloading **Apache Spark**. 

- Or issue the following command in your terminal inside **Ubuntu**:

  - 2.1. Navigate to the /opt directory and download Spark:
```bash
cd /opt # first command

sudo wget https://dlcdn.apache.org/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz # second  command


```

  - - 2.2. Extract the downloaded archive and set up the directory:
```bash
# one at a time

sudo tar -xvzf spark-3.5.0-bin-hadoop3.tgz # first command
sudo mv spark-3.5.0-bin-hadoop3 spark # second  command

```


- After downloading and extracting **Spark**, update your environment variables.

  - 2.3.Modify the .bashrc file:

```bash
sudo nano ~/.bashrc
```

- - 2.4.Add the following lines at the bottom:

```bash
export SPARK_HOME=/opt/spark/spark-3.5.0-bin-hadoop3
export PATH=$SPARK_HOME/bin:$PATH
export PYSPARK_PYTHON=python3
```

- - 2.5.Save and exit (CTRL + X, then Y, then Enter).

- - 2.6.Apply the changes:
```bash
source ~/.bashrc
```

At this point if you have been watching the following video: 
- https://trentu.blackboard.com/ultra/courses/_65448_1/cl/outline

You probably might have been prompted to issue the following command:

```bash
sudo -i
```

Which makes a switch from a **normal user** mode to a **root user** mode that looks like the following:

```bash
root@ubuntu 
```
And you probably have downloaded everything in the **root user**.
This will cause some confusion as you continue, because you will notice that you cannot use **hadoop** in the **root user**. The best thing to do would be to move your **spark** installation from **root user** to  **normal user**.


Unless, you download and configure **hadoop** to be in the **root user** as well, otherwise the following could be useful:

- 1. Assuming you have already finished with the steps above, and you just started your virtual machine and logged into Ubuntu. Go to the terminal and issue the command:

```bash
sudo -i

```

- 2. Move Spark to the Normal User’s Home Directory:
```bash
mv /opt/spark /home/ubuntu25/
```

- 3. Change Ownership to the Normal User
```bash
chown -R ubuntu25:ubuntu25 /home/ubuntu25/spark

```

- 4. Update Environment Variables for the Normal User

      - 4.1. Switch to the normal user

```bash
su - ubuntu25
# or
Ctrl + d
```


- - 4.2. Open `.bashrc` and edit 


```bash
nano ~/.bashrc
```

- - 4.3. Add the following spark variables at the bottom

```bash
# Spark Variables
# the only change is the `/home/ubuntu25/`
export SPARK_HOME=/home/ubuntu25/spark
export PATH=$SPARK_HOME/bin:$PATH
export PYSPARK_PYTHON=python3
export PYSPARK_DRIVER_PYTHON=python3
```


- - 4.4. Save & reload the environment
```bash
source ~/.bashrc
```

- - 4.5. Verify Spark installation

```bash
spark-submit --version
```

✅ Expected Output:
```bash
SPARK version 3.5.0
```

- - 4.6. Test if spark works.
```bash
pyspark --master yarn
```

✅ Expected Output:
```bash
>>>

```

Or you can run the following:

    ```bash
    spark-shell
    ```

    ✅ Expected Output:
    ```bash
    scala>>>
    ```

To exit, type:

    ```bash
    :quit

    # or

    Ctrl + d # wichever works
    ```

Either works just fine.

~~~~~~~~~~~~~
Now you should be back to normal user mode. And hopefully everything should be working correctly.
~~~~~~~~~~~~~



---
## **3. Running Spark Job**


~~~~~~~~~~~~~~~~~~~~~~~~~~~
The following assume that you are working in normal user mode as opposed to root user. However, as already stated, if all your installation and configuration have been done in root user. You should be fine.
~~~~~~~~~~~~~~~~~~~~~~~~~~~

####  **0. Start Hadoop first**

Run the following command in order:
```bash 
start-dfs.sh
jps
```
✅ Expected output:
```bash 
NameNode
DataNode
SecondaryNameNode
```
- If `NameNode` not showing continue with yarn.

Run the following command to start YARN:

```bash
start-yarn.sh
jps
```

✅ Expected output:
```bash 
ResourceManager
NodeManager
```
- Now run the following for namenode:
```bash
hdfs namenode -format 
hdfs --daemon start namenode 
jps
```

✅ Expected output:
```bash 
- ResourceManager
- NodeManager
- Jps
- NameNode
- DataNode
- SecondaryNameNode
```
Extra:
```bash
hdfs dfsadmin -report
```
✅ Expected output: 
```bash 
No errors and showing available storage.
```
The following is something that I found while digging for spark. You can manually start the spark history server just in case it is not on. This is so that you can see your past spark jobs:

```bash
# one of the following command will work. If not try them both
start-history-server.sh 
$SPARK_HOME/sbin/start-history-server.sh 
```
---

#### **Let's run the spark job**

The following information were taken from the following sources:
- https://spark.apache.org/docs/latest/submitting-applications.html
- https://spark.apache.org/docs/latest/running-on-yarn.html
- https://spark.apache.org/docs/latest/spark-standalone.html


#### **A. Running a Local Spark Job**

1. **Prepare the script(before hand) & dataset**: Place `local_code_test_A2-pyspark-sql` and `pokemon.csv` in the same directory(`local`; in my case).
---

2. **Run the script locally**:
   ```bash
   spark-submit --master local local_code_test_A2-pyspark-sql
   ```

---
3. **Output is stored locally** in my case, in the following: `output/local_feistiest_pokemon.csv`.
---

4. **Issue encountered**: Spark sometimes writes multiple part files, so rename the desired one manually:

   ```bash
   mv output/part-00000-*.csv output/local_feistiest_pokemon.csv
   ```


This will usually result in the desired csv file. Also, you might need to modify the script to make sure it works for you.

---

#### **B. Running a PySpark Job on YARN**

1. **Few changes**: **Move files to HDFS**. For the yarn job, in my case, I created a different folder(a second one:`yarn`), so that I can avoid any mistakes:
```bash
   hdfs dfs -mkdir -p /user/ubuntu25/yarn
   hdfs dfs -put pokemon.csv /user/ubuntu25/yarn/
```
---
2. **Modify script to read from HDFS** (`yarn_code_test_A2-pyspark-sql.py`):
   ```python
   pokemon_df = spark.read.csv("hdfs:///user/ubuntu25/yarn/pokemon.csv", header=True, inferSchema=True) # this is a crucial modification. 
   #For the local job, instead of `hdfs` you would have `file`.
   ```
---
3. **Run the job on YARN**:
   ```bash
   spark-submit --master yarn yarn_code_test_A2-pyspark-sql.py # another difference. for yarn you use `--master yarn` instead of `--master local`
   ```


---


4. **Lastly, retrieve output from HDFS**:
   ```bash
   hdfs dfs -get /user/ubuntu25/yarn/output output/
   mv output/part-00000-*.csv output/feistiest_pokemon_yarn.csv
   ```

---




## **Key Differences Between Local and YARN Jobs**

| Feature           | Local Job   | YARN Job   |
|------------------|---------------------------------|----------------------------|
| **Execution Mode**  | `--master local` | `--master yarn` |
| **Data Location** | Reads/writes local files `file://` | Reads/writes from HDFS `hdfs://` |
| **Use Case**  | Good for testing | Good for large datasets |







________________________________________
## **5. Summary**


### 1️⃣ Setup & Installation  
- Install **Java 8**, **Hadoop 3.2.3**, and **Apache Spark 3.5.0**, for better compatibility.
  - Although, a different **Hadoop** version and **Apache Spark** versions have been used, as far as the **code** goes, so long as **Hadoop**, **Apache Spark** and **Java** are configured properly and are compatible, the **code** should work. 
- Configure environment variables for **Spark** and **Hadoop**.  
- Ensure Spark runs under a **normal user** (not root).  

### 2️⃣ Running a Spark Job Locally
- Execute the PySpark job with:
  ```bash
  spark-submit --master local local_code_test_A2-pyspark-sql.py
  ```
- Output is stored locally in `output/local_feistiest_pokemon.csv`.

### 3️⃣ Running a Spark Job on YARN
- Move dataset to **HDFS**:
  ```bash
  hdfs dfs -mkdir -p /user/ubuntu25/yarn
  hdfs dfs -put pokemon.csv /user/ubuntu25/yarn/
  ```

- Modify the script to read from HDFS:
  ```python
  pokemon_df = spark.read.csv("hdfs:///user/ubuntu25/yarn/pokemon.csv", header=True, inferSchema=True)
  ```

- Submit job to YARN:
  ```bash
  spark-submit --master yarn yarn_code_test_A2-pyspark-sql.py
  ```

- Retrieve output from HDFS:
  ```bash
  hdfs dfs -get /user/ubuntu25/yarn/output output/
  mv output/part-00000-*.csv output/feistiest_pokemon_yarn.csv
  ```

### 4️⃣ File retrieval

- To get file from my virtual machine to my local machine, I uploaded them to google drive, and downloaded them.

________________________________________
🚀 Additional Debugging Steps

1️⃣ If at any point you encounter errors or bugs, google and stack overflow are your best friends.

________________________________________

📜 All resources used have been referenced, and the links are in this readme file and others are in a different pdf document.

---

📂 **Dataset Reference**  
This project uses the Pokémon dataset available on Kaggle:  
🔗 [https://www.kaggle.com/datasets/rounakbanik/pokemon](https://www.kaggle.com/datasets/rounakbanik/pokemon)





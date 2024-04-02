import subprocess
import os

name = input("Enter the name of the server: ")
version = input("Enter the version of the server: ")
ram = input("Ram to allocate to the server (in GB): ")
port = input("Port to run the server on: ")

dir_name = f"server_{name}_{version}"
os.mkdir(dir_name)

os.chdir(dir_name)

minor_version = int(version.split(".")[1])

if minor_version >= 9:
    # after version 1.9 minecraft server jar changed from java 8 to java 17
    use_java_8 = False
else:
    use_java_8 = True

with open("start.sh", "w") as f:
    f.write("#!/bin/sh\n")
    #f"java -Xmx{ram}G -Xms{ram}G -jar server.jar nogui"
    if not use_java_8:
        java_cmd = "java"
    else:
        java_cmd = "/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java"
    f.write(f"{java_cmd} -Xmx{ram}G -Xms{ram}G -jar server.jar nogui")

server_jar_url = f"https://www.mcjars.com/get/vanilla-{version}.jar"
subprocess.run(["wget", server_jar_url, "-O", "server.jar"])

subprocess.run(["chmod", "+x", "start.sh"])

subprocess.run("./start.sh")

eula_lines = []
with open("eula.txt") as f:
    eula_lines = f.readlines()

with open("eula.txt", "w") as f:
    for line in eula_lines:
        if "eula=false" in line:
            f.write("eula=true\n")
        else:
            f.write(line)


server_properties_lines = []
with open("server.properties") as f:
    server_properties_lines = f.readlines()

with open("server.properties", "w") as f:
    for line in server_properties_lines:
        if "server-port=" in line:
            f.write(f"server-port={port}\n")
        else:
            f.write(line)

subprocess.run("./start.sh")
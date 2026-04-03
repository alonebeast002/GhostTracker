#!/bin/bash


G='\033[32;1m'
Y='\033[33;1m'
R='\033[31;1m'
RESET='\033[0m'

clear
echo -e "${G}--- GHOSTTRACK PRO INSTALLER ---${RESET}"


if [ -f "GhostTracker.py" ]; then
    PY_FILE="GhostTracker.py"
elif [ -f "ghosttrack.py" ]; then
    PY_FILE="ghosttrack.py"
else
    echo -e "${R}[!] Error: No python script found!${RESET}"
    echo -e "${Y}Make sure either 'GhostTracker.py' or 'ghosttrack.py' exists here.${RESET}"
    ls
    exit 1
fi

echo -e "${G}[✔] Found script: $PY_FILE${RESET}"


echo -e "${Y}[*] Creating Global Command...${RESET}"


cat <<EOF > GhostTracker
#!/bin/bash
python3 $(pwd)/$PY_FILE
EOF

chmod +x GhostTracker
chmod +x $PY_FILE

# 3. Bin folder mein move karna
if [ -d "/data/data/com.termux" ]; then
    mv GhostTracker $PREFIX/bin/
    echo -e "${G}[✔] Command 'GhostTracker' installed in Termux!${RESET}"
else
    sudo mv GhostTracker /usr/local/bin/
    echo -e "${G}[✔] Command 'GhostTracker' installed in Linux!${RESET}"
fi

echo -e "${Y}[!] Now just type: ${G}GhostTracker${RESET} from anywhere!"

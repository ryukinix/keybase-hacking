USERNAME=lerax

echo "[mkdir] create session/ directory"
mkdir -p session

echo "[python] generate guesses into session/commands.txt"
python guesses.py \
    | xargs -L 1 -I{} echo keybase oneshot -u $USERNAME --paperkey \'{}\' > session/commands.txt

echo "[python] spawn crack session!"
python crack.py

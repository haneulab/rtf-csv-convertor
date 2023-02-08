function rtf() {
    python main.py "--no-test" "$1"
}
function rtftest() {
    python -m unittest "$1"
}

function envon() {
    source env/bin/activate
}
function envoff() {
    deactivate
}
